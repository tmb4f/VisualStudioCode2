"""
Created_on: 12-01-2020

Author: Satya Kommuri
Author id : sk2vk
"""

import os
import logging
from dotenv import load_dotenv

load_dotenv(verbose=False)

user_id = os.getenv("INTERCONNECT_USERID")
passwd = os.getenv("INTERCONNECT_PASSWD")
iconnect_server = os.getenv("INTERCONNECT_SERVER_PROD")
client_ID = os.getenv("CLIENT_ID_PROD")
iconnect_retries = 3

# Blocked beds DB config
dialect = "mssql+pyodbc"
db_driver = "ODBC+Driver+17+for+SQL+Server"
trusted_connection = 'yes'
server_name = os.getenv("SS_DB_SERVER")
server_name_t = os.getenv("SS_DB_SERVER_T")
db_name = os.getenv("SS_DB_NAME")
service_user = os.getenv("SS_DB_USERID")
service_pass = os.getenv("SS_DB_PASSWD")

blocked_beds_tbl = os.getenv("SQL_SERVER_BLOCKED_BEDS_TABLE")

# CENSUS config
census_server = os.getenv("CENSUS_DB_SERVER")
census_db = os.getenv("CENSUS_DB_NAME")
census_userid = os.getenv("DB_USERID")
census_pass = os.getenv("DB_PASSWD")

# TABLEAU config
tab_server = os.getenv("TABLEAU_SERVER")
tab_site = os.getenv("TABLEAU_SITE_NAME")
tab_project = os.getenv("TABLEAU_PROJECT")
tab_token_name = os.getenv("TABLEAU_TOKEN_NAME")
tab_token = os.getenv("TABLEAU_TOKEN_KEY")

#ODS config
ods_server = os.getenv("ODS_DB_SERVER")
ods_db = os.getenv("ODS_DB_NAME")
ods_userid = os.getenv("DB_USERID")
ods_pass = os.getenv("DB_PASSWD")

# Table config
current_unit_census = 'dbo.Fact_Census_Unit'
mdm_unit_tbl = 'Rptg.vwRef_MDM_Location_Master'
um_current_census = 'Stage.PtProg_All_Beds_Census'
ods_curr_inputs_dschgs_brders_ED_Acuity = 'DS_HSDM_App.Rptg.vwPtProg_Current_Inpts_Dschgs_Brders_ED_Acuity'
ods_transfers = 'DS_HSDM_Prod.Rptg.vwTransferCenter_Teletrack_External_Transfers'
current_transfers = 'Stage.PtProg_Transfers_Pending_Accepted'
current_ed_boarders = 'Stage.PtProg_ED_Boarders'
current_post_op = 'Stage.PtProg_Bed_Planning'
pt_prog_history = 'Stage.PtProg_Dash_Data_Archive'
transfer_status_tbl = 'DS_HSDM_App.Stage.PtProg_Transfer_Status'
current_discharges = 'Stage.PtProg_Discharge_Today'


unit_list = [
    {'Unit_ID': 10243051, 'Unit_Name': 'UVHE 3 CENTRAL', 'From_IConnect': True, 'Alias_Name': '3 CENTRAL', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243052, 'Unit_Name': 'UVHE 3 EAST', 'From_IConnect': True, 'Alias_Name': '3 EAST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243089, 'Unit_Name': 'UVHE 3 NORTH', 'From_IConnect': True, 'Alias_Name': '3 NORTH ICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243142, 'Unit_Name': 'UVHE 3 NORTH ACUTE', 'From_IConnect': True, 'Alias_Name': '3 NORTH ACUTE', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243053, 'Unit_Name': 'UVHE 3 WEST', 'From_IConnect': True, 'Alias_Name': '3 WEST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243122, 'Unit_Name': 'UVHE 3 SOUTH', 'From_IConnect': False, 'Alias_Name': '3 SOUTH', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243132, 'Unit_Name': 'UVHE 3 SOUTH ONC', 'From_IConnect': True, 'Alias_Name': '3 SOUTH ONC',
     'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243130, 'Unit_Name': 'UVHE 3 SOUTH PALIATIVE', 'From_IConnect': False, 'Alias_Name': '3 SOUTH PALIATIVE', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243038, 'Unit_Name': 'UVHE MEDICAL ICU', 'From_IConnect': True, 'Alias_Name': 'MICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243054, 'Unit_Name': 'UVHE 4 CENTRAL CV', 'From_IConnect': True, 'Alias_Name': '4 CENTRAL CV', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243055, 'Unit_Name': 'UVHE 4 EAST', 'From_IConnect': True, 'Alias_Name': '4 EAST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243091, 'Unit_Name': 'UVHE 4 NORTH', 'From_IConnect': True, 'Alias_Name': '4 NORTH/TCVICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243110, 'Unit_Name': 'UVHE 4 CENTRAL TXP', 'From_IConnect': True, 'Alias_Name': '4 CENTRAL TXP', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243057, 'Unit_Name': 'UVHE 4 WEST', 'From_IConnect': True, 'Alias_Name': '4 WEST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243123, 'Unit_Name': 'UVHE 4 SOUTH CVICU', 'From_IConnect': True, 'Alias_Name': '4 SOUTH CVICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243136, 'Unit_Name': 'UVHE 4 SOUTH ACUTE', 'From_IConnect': False, 'Alias_Name': '4 SOUTH ACUTE', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243058, 'Unit_Name': 'UVHE 5 CENTRAL', 'From_IConnect': True, 'Alias_Name': '5 CENTRAL', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243059, 'Unit_Name': 'UVHE 5 EAST', 'From_IConnect': True, 'Alias_Name': '5 EAST', 'Unit_Group': 'Psych'},
    {'Unit_ID': 10243090, 'Unit_Name': 'UVHE 5 NORTH', 'From_IConnect': True, 'Alias_Name': '5 NORTH', 'Unit_Group': 'Adult IMU'},
    {'Unit_ID': 10243119, 'Unit_Name': 'UVHE 5 NORTH SSU', 'From_IConnect': True, 'Alias_Name': 'SHORT STAY', 'Unit_Group': 'Short Stay Unit'},
    {'Unit_ID': 10243060, 'Unit_Name': 'UVHE 5 WEST', 'From_IConnect': True, 'Alias_Name': '5 WEST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243124, 'Unit_Name': 'UVHE 5 SOUTH', 'From_IConnect': True, 'Alias_Name': '5 SOUTH', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243061, 'Unit_Name': 'UVHE 6 CENTRAL', 'From_IConnect': True, 'Alias_Name': '6 CENTRAL', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243062, 'Unit_Name': 'UVHE 6 EAST', 'From_IConnect': True, 'Alias_Name': '6 EAST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243092, 'Unit_Name': 'UVHE 6 NORTH', 'From_IConnect': True, 'Alias_Name': '6 NORTH', 'Unit_Group': 'Adult IMU'},
    {'Unit_ID': 10243063, 'Unit_Name': 'UVHE 6 WEST', 'From_IConnect': True, 'Alias_Name': '6 WEST', 'Unit_Group': 'Adult Acute'},
    {'Unit_ID': 10243120, 'Unit_Name': 'UVHE 6 EAST SSU', 'From_IConnect': True, 'Alias_Name': 'SHORT STAY', 'Unit_Group': 'Short Stay Unit'},
    {'Unit_ID': 10243064, 'Unit_Name': 'UVHE 7 CENTRAL', 'From_IConnect': True, 'Alias_Name': '7 ACUTE', 'Unit_Group': 'Peds Acute'},
    {'Unit_ID': 10243093, 'Unit_Name': 'UVHE 7 NORTH', 'From_IConnect': True, 'Alias_Name': '7 ACUTE', 'Unit_Group': 'Peds Acute'},
    {'Unit_ID': 10243118, 'Unit_Name': 'UVHE 7 NORTH NICU', 'From_IConnect': False, 'Alias_Name': 'NEWBORN ICU', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243108, 'Unit_Name': 'UVHE 7 CIMU', 'From_IConnect': True, 'Alias_Name': '7 ACUTE', 'Unit_Group': 'Peds Acute'},
    {'Unit_ID': 10243065, 'Unit_Name': 'UVHE 7 WEST', 'From_IConnect': True, 'Alias_Name': '7 ACUTE', 'Unit_Group': 'Peds Acute'},
    {'Unit_ID': 10243101, 'Unit_Name': 'UVHE 7 EAST ACUTE', 'From_IConnect': True, 'Alias_Name': '7 ACUTE', 'Unit_Group': 'Peds Acute'},
    {'Unit_ID': 10243103, 'Unit_Name': 'UVHE 7 NORTH ACUTE', 'From_IConnect': False, 'Alias_Name': '7 ACUTE', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243113, 'Unit_Name': 'UVHE 7 NORTH OB', 'From_IConnect': True, 'Alias_Name': 'WOMENS (7N/8C/8N)', 'Unit_Group': 'Womens (7N/8C/8N)'},
    {'Unit_ID': 10243066, 'Unit_Name': 'UVHE 8 CENTRAL OB', 'From_IConnect': True, 'Alias_Name': 'WOMENS (7N/8C/8N)', 'Unit_Group': 'Womens (7N/8C/8N)'},
    {'Unit_ID': 10243094, 'Unit_Name': 'UVHE 8 NORTH OB', 'From_IConnect': True, 'Alias_Name': 'WOMENS (7N/8C/8N)', 'Unit_Group': 'Womens (7N/8C/8N)'},
    {'Unit_ID': 10243115, 'Unit_Name': 'UVHE 8 NORTH ONC', 'From_IConnect': False, 'Alias_Name': '8 NORTH ONC', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243068, 'Unit_Name': 'UVHE 8 WEST', 'From_IConnect': False, 'Alias_Name': '8 WEST', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243096, 'Unit_Name': 'UVHE 8 WEST STEM CELL', 'From_IConnect': True, 'Alias_Name': '8 WEST STEM CELL', 'Unit_Group': 'Adult IMU'},
    {'Unit_ID': 10243012, 'Unit_Name': 'UVHE CARDIAC CATH LAB','From_IConnect': False, 'Alias_Name': 'CARDIAC CATH LAB', 'Unit_Group': 'Post-Op'},
    {'Unit_ID': 10243050, 'Unit_Name': 'UVHE CARDIAC TRANSITN','From_IConnect': False, 'Alias_Name': 'CARDIAC TRANSITN', 'Unit_Group': 'Post-Op'},
    {'Unit_ID': 10243035, 'Unit_Name': 'UVHE CORONARY CARE', 'From_IConnect': True, 'Alias_Name': 'CORONARY CARE', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243026, 'Unit_Name': 'UVHE EMERGENCY DEPT', 'From_IConnect': False, 'Alias_Name': 'ED', 'Unit_Group': 'ED'},  # TODO: distinguish b/w ED Boarder and in lobby
    {'Unit_ID': 10243911, 'Unit_Name': 'UVHE ENDOBRONC PROC','From_IConnect': False, 'Alias_Name': 'ENDOBRONC PROC', 'Unit_Group': 'Post-Op'},
    {'Unit_ID': 10243037, 'Unit_Name': 'UVHE LABOR & DELIVERY', 'From_IConnect': True, 'Alias_Name': 'LABOR & DELIVERY',
     'Unit_Group': 'Labor & Delivery'},
    {'Unit_ID': 10243041, 'Unit_Name': 'UVHE NEUR ICU', 'From_IConnect': True, 'Alias_Name': 'NEUR ICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243025, 'Unit_Name': 'UVHE NEURORADIOLOGY', 'From_IConnect': False, 'Alias_Name': 'NEURORADIOLOGY','Unit_Group': 'Post-Op'},
    {'Unit_ID': 10243040, 'Unit_Name': 'UVHE NEWBORN ICU', 'From_IConnect': True, 'Alias_Name': 'NEWBORN ICU', 'Unit_Group': 'NICU'},
    {'Unit_ID': 10243043, 'Unit_Name': 'UVHE PEDIATRIC ICU', 'From_IConnect': True, 'Alias_Name': 'PEDIATRIC ICU', 'Unit_Group': 'Peds ICU'},
    {'Unit_ID': 10243900, 'Unit_Name': 'UVHE PERIOP', 'From_IConnect': False, 'Alias_Name': 'PERIOP', 'Unit_Group': 'Post-Op'},
    {'Unit_ID': 10354900, 'Unit_Name': 'UVBB OPSC', 'From_IConnect': False, 'Alias_Name': 'OPSC', 'Unit_Group': 'Post-Op'},
    {'Unit_ID': 10243102, 'Unit_Name': 'UVHE PICU 7EAST', 'From_IConnect': True, 'Alias_Name': 'PEDIATRIC ICU', 'Unit_Group': 'Peds ICU'},
    {'Unit_ID': 10243100, 'Unit_Name': 'UVHE PICU 7NORTH', 'From_IConnect': True, 'Alias_Name': 'PEDIATRIC ICU', 'Unit_Group': 'Peds ICU'},
    {'Unit_ID': 10243047, 'Unit_Name': 'UVHE SHORT STAY UNIT', 'From_IConnect': False, 'Alias_Name': 'SHORT STAY', 'Unit_Group': 'Not used'},
    {'Unit_ID': 10243046, 'Unit_Name': 'UVHE SURG TRAM ICU', 'From_IConnect': True, 'Alias_Name': 'SURG TRAM ICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10243049, 'Unit_Name': 'UVHE TCV POST OP', 'From_IConnect': True, 'Alias_Name': '4 NORTH/TCVICU', 'Unit_Group': 'Adult ICU'},
    {'Unit_ID': 10221001, 'Unit_Name': 'TCIR TC2B', 'From_IConnect': True, 'Alias_Name': 'TCIR TC2B', 'Unit_Group': 'TCH'},
    {'Unit_ID': 10221002, 'Unit_Name': 'TCIR TC3A', 'From_IConnect': True, 'Alias_Name': 'TCIR TC3A', 'Unit_Group': 'TCH'},
    {'Unit_ID': 10221007, 'Unit_Name': 'TCIR TC2A', 'From_IConnect': True, 'Alias_Name': 'TCIR TC2A', 'Unit_Group': 'TCH'},
    {'Unit_ID': 10243002, 'Unit_Name': 'P1HE INOUT SURGERY', 'From_IConnect': False, 'Unit_Group': 'Post-Op'},
    {'Unit_ID': 10379900, 'Unit_Name': 'UVML ENDOBRONC PROC', 'From_IConnect': False, 'Unit_Group': 'Post-Op'},
]

COVID_UNITS = [10243124,  # 5 South
               10243123,  # 4 South CVICU
               10243136]  # 4 South Acute

BED_SPECIFIC_GROUPS = {#'5309A': 'COVID Acute',
                       }

service_line_config = [
    {'ID': 1, 'SL_Name': 'Digestive Health'},
    {'ID': 2, 'SL_Name': 'Heart and Vascular', 'Alias_Name': 'Heart & Vascular'},
    {'ID': 3, 'SL_Name': 'Medical Subspecialties', 'Alias_Name': 'Primary Care'},
    {'ID': 4, 'SL_Name': 'Musculoskeletal'},
    {'ID': 5, 'SL_Name': 'Neurosciences and Behavioral Health', 'Alias_Name': 'Neurosciences & Behavioral Health'},
    {'ID': 6, 'SL_Name': 'Oncology'},
    {'ID': 9, 'SL_Name': 'Surgical Subspecialties', 'Alias_Name': 'Ophthalmology'},
    {'ID': 10, 'SL_Name': 'Transplant'},
    {'ID': 11, 'SL_Name': 'Womens and Childrens', 'Alias_Name': "Women's & Children's"}]

curr_env = os.getenv('SERVER_PROD_STATUS')


def get_curr_env(env=curr_env):
    if env and env.lower() == 'prod':
        return 'production'
    elif env and env.lower() == 'test':
        return 'test'
    else:
        return 'development'


env = get_curr_env()
if  env and env.lower() == 'production':
    log_dir = os.getenv('ERROR_LOGS')
    logging_level = logging.WARNING
else:
    log_dir = os.getcwd()
    logging_level = logging.INFO

logging.basicConfig(filename=os.path.join(log_dir, "patient_progression.log"), level=logging_level,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
