"""
Created_on: 28-01-2020

Author: Satya Kommuri
Author id : sk2vk

Description: Patient progression project work - SQL's for census gathering
"""
''' Start of block
current_census_query = """WITH recent_load_times AS (
                            SELECT DISTINCT
                                unit.Unit
                                ,MAX(unit.Load_Dtm) max_load_dtm
                            FROM
                                {0} unit
                            GROUP BY
                                unit.Unit)
                            select unit.MRN_int,
                                   unit.Bed_Nme,
                                   unit.Unit,
                                   unit.Name,
                                   unit.Load_Dtm,
                                   unit.Unit_ID                                   
                            from {0} unit
                                join recent_load_times rlt
                                on unit.Load_Dtm = rlt.max_load_dtm
                                and unit.Unit = rlt.Unit"""


ods_unit_query = """SELECT [EPIC_DEPARTMENT_ID] as Unit_ID
                  ,[EPIC_DEPT_NAME] as Epic_Dept_Name
                  ,[HS_AREA_ID] as Hs_Area_ID
                  ,[HS_AREA_NAME] as Hs_Area_Name
              FROM {0}
              where (EPIC_DEPT_NAME like 'UVHE%' and HS_AREA_ID=1) or 
                EPIC_DEPT_NAME like 'TCIR TC%'  """

get_all_data = """select * from {0}"""

get_acuity_data = """ select sk_Fact_Pt_Enc_Clrt,
                             PAT_ENC_CSN_ID,
                             MRN_int,
                             PAT_NAME,
                             Bed_Nme,
                             Ordering_Department,
                             Boarders,
                             Map_Attending_Service_Line,
                             Clrt_DEPt_Nme,
                             DEPARTMENT_ID,
                             Load_Dtm                       
                    from {0}"""

ods_transfers = """SELECT EntryTime
                        , TransferID
                        , ProtocolNme
                        , Diagnosis
                        , Disposition
                        , XTPlacementStatusName
                        , ReferringFacilityID
                        , Referring_Facility
                        , PatientMR 
                        , Accepting_MD
                        , DestinationUnitID
                        , DestinationUnit
                        , AcceptingMD_ServiceLine
                        , Load_Dtm
                    FROM {0}
                    WHERE XTPlacementStatusName = 'Accepted' """

yest_census_query = """SELECT main.EVENT_ID,
       main.ADT_PATIENT_STAT,
       main.sk_Adm_Dte,
       main.HOSP_ADMSN_TYPE_C,
       main.HOSP_ADMSN_TYPE,
       main.sk_Dsch_Dte,
       main.DEPARTMENT_ID,
       main.Clrt_DEPt_Typ,
       main.ED_DISPOSITION,
       main.Clrt_DEPt_Nme,
       main.IN_DTTM,
       main.next_IN_DTTM,
       main.PAT_ENC_CSN_ID,
       main.ADMIT_CONF_STAT,
       main.adt_pt_cls,
       main.MRN_Clrt,
       main.[As of],
       main.Load_Dtm_ODS

  FROM (--main
		SELECT ca.EVENT_ID
		  ,peh.ADT_PATIENT_STAT
		  ,peh.sk_Adm_Dte
		  ,admt.HOSP_ADMSN_TYPE_C
		  ,admt.HOSP_ADMSN_TYPE
		  ,peh.sk_Dsch_Dte
		  ,dep.DEPARTMENT_ID
		  ,dep.Clrt_DEPt_Typ
		  ,peh.ED_DISPOSITION
		  ,dep.Clrt_DEPt_Nme
		  ,ca.IN_DTTM
		  ,LEAD(ca.IN_DTTM) OVER (PARTITION BY ca.PAT_ENC_CSN_ID ORDER BY ca.IN_DTTM) AS next_IN_DTTM
		  ,ca.PAT_ENC_CSN_ID
		  ,peh.ADMIT_CONF_STAT
		  ,peh.adt_pt_cls 
		  ,peh.MRN_Clrt
		  ,DATEADD(SECOND, 1, CAST(CAST(GETDATE() AS DATE) AS DATETIME)) AS 'As of'
		  ,ca.Load_Dtm_ODS

		FROM dbo.Fact_Clrt_ADT AS ca	--ADT event table
		INNER JOIN dbo.Fact_Pt_Enc_Hsp_Clrt AS peh ON ca.PAT_ENC_CSN_ID = peh.PAT_ENC_CSN_ID	--join for admission and discharge dates, MRN
		INNER JOIN dbo.Dim_Clrt_DEPt dep ON dep.sk_Dim_Clrt_DEPt = ca.sk_Dim_Clrt_DEPt --join for department
		INNER JOIN dbo.Dim_Date AS dd ON peh.sk_Dsch_Dte = dd.date_key	--for easy conversion of disch_dte
		INNER JOIN dbo.Dim_Clrt_Admt_Chrcstc AS admt ON admt.sk_Dim_Clrt_Admt_Chrcstc = peh.sk_Dim_Clrt_Admt_Chrcstc --for admission type, added 2/2/16 by KAC
		LEFT OUTER JOIN dbo.Dim_Clrt_Pt pt ON pt.sk_Dim_Pt = peh.sk_Dim_pt

		WHERE CONVERT(DATE, CONVERT(CHAR(8),peh.sk_adm_dte)) < DATEADD(SECOND, 1, CAST(CAST(GETDATE() AS DATE) AS DATETIME)) --looking at patients who admitted before today
		  AND ((peh.ADT_PATIENT_STAT = 'Admission' OR peh.ADT_PATIENT_STAT IS NULL) OR (peh.ADT_PATIENT_STAT = 'Discharged' AND CAST(CAST(dd.day_date AS DATE) AS SMALLDATETIME) +
		  CAST(CAST(peh.Dsch_Tm AS TIME)AS SMALLDATETIME) > DATEADD(SECOND, 1, CAST(CAST(GETDATE() AS DATE) AS DATETIME)))) --either admission or discharged after 12:00:01 AM of current date
		  AND (peh.ADMIT_CONF_STAT <> 'Pending' OR peh.admit_conf_stat IS NULL)
		  AND dep.DEPARTMENT_ID NOT IN ('10221007','10243079','10243050','10243002','10221001','10221002','10221007')	
		  --exclude patients in UVHE INOUT SURGERY, UVHE CARDIAC TRANSITN, UVHE ADMIT, TCH
		  AND (pt.TEST = 0 OR pt.TEST IS NULL)
		  AND NOT (dep.DEPARTMENT_ID = 10243026 AND peh.ED_DISPOSITION = 'Admitted' 
				AND peh.ED_DISP_TIME > DATEADD(SECOND, -1, CAST(CAST(GETDATE() AS DATE) AS DATETIME))) --Remove Patients that become ED Boarders After Midnight
		) AS main

WHERE DATEADD(SECOND, 1, CAST(CAST(GETDATE() AS DATE) AS DATETIME)) BETWEEN main.IN_DTTM AND main.next_IN_DTTM --on unit at 12:00:01 AM of current date
OR (DATEADD(SECOND, 1, CAST(CAST(GETDATE() AS DATE) AS DATETIME)) > main.IN_DTTM AND main.next_IN_DTTM IS NULL) 

"""

unit_groups_query = """SELECT
	Unit_Group, Clrt_DEPt_Nme
  FROM
	DS_HSODS_App.Rptg.Ref_Throughput_Unit_Groups AS temp
	group by Unit_Group, Clrt_DEPt_Nme"""


y_census_query = """select  UOS_DTTM , count(*) as value from  DS_HSDM_App.TabRptg.Dash_Midnight_Census_DV 
where UOS_DTTM = DATEADD(dd, -1, DATEDIFF(dd, 0, GETDATE()))
and (DATEDIFF(dd,event_date,UOS_DTTM))=0
group by UOS_DTTM"""

y_discharges_query = """select * from DS_HSDM_Prod.Rptg.DASH_TILE_DISCHARGES
where DATEDIFF(dd, 0, event_Date) = DATEADD(dd, -1, DATEDIFF(dd, 0, GETDATE()))
and DATEADD(dd, 0, event_Date)<>getdate()"""

y_admissions_query = """select * from DS_HSDM_Prod.Rptg.DASH_TILE_ADMITS
where DATEDIFF(dd, 0, event_Date) = DATEADD(dd, -1, DATEDIFF(dd, 0, GETDATE()))"""
'''
'''
y_ed_arrivals_query = """select CSN, [LOS in Hours] as LOS, Disposition from DS_HSDM_App.Stage.Throughput_ED_Arrivals_and_Dispo
where DATEDIFF(dd, 0, [Arrival Dt]) = DATEADD(dd, -1, DATEDIFF(dd, 0, GETDATE()))
and (DATEDIFF(dd,[Arrival Dt],Load_Dte))=1 and (Disposition <> 'Registered in Error' or Disposition is null)"""
'''
'''

y_ed_arrivals_query = """select person_id, LOS_in_Hours as LOS, Disposition  from [DS_HSDM_App].[TabRptg].[Dash_DailyHuddle_ED_Arrival_Tiles]
where DATEDIFF(dd, 0, event_date) = DATEADD(dd, -1, DATEDIFF(dd, 0, GETDATE()))"""

y_ed_admissions_query = """select * from DS_HSDM_App.Stage.Throughput_ED_Arrivals_and_Dispo
where DATEDIFF(dd, 0, [Discharge Disposition Dt]) = DATEADD(dd, -1, DATEDIFF(dd, 0, GETDATE()))
and (DATEDIFF(dd,[Discharge Disposition Dt],Load_Dte))=1
and Disposition = 'Admitted'
"""
# TRANSFER Status query
trans_stats_query = """SELECT  top(1) [open_to_transfer], [tier_1], [restricted_tier_1] FROM {0} order by load_dtm desc"""
''' # End of block

get_test_data = """select * from {0}"""