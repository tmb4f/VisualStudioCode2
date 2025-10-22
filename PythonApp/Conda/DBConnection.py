"""
Created_on: 12-01-2020

Author: Satya Kommuri
Author id : sk2vk
"""
"""
import os
import logging
from dotenv import load_dotenv

load_dotenv(verbose=False)

# user_id = os.getenv("INTERCONNECT_USERID")
# passwd = os.getenv("INTERCONNECT_PASSWD")
# iconnect_server = os.getenv("INTERCONNECT_SERVER_PROD")
# client_ID = os.getenv("CLIENT_ID_PROD")
# iconnect_retries = 3

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
# census_server = os.getenv("CENSUS_DB_SERVER")
# census_db = os.getenv("CENSUS_DB_NAME")
# census_userid = os.getenv("DB_USERID")
# census_pass = os.getenv("DB_PASSWD")

# TABLEAU config
# tab_server = os.getenv("TABLEAU_SERVER")
# tab_site = os.getenv("TABLEAU_SITE_NAME")
# tab_project = os.getenv("TABLEAU_PROJECT")
# tab_token_name = os.getenv("TABLEAU_TOKEN_NAME")
# tab_token = os.getenv("TABLEAU_TOKEN_KEY")

#ODS config
# ods_server = os.getenv("ODS_DB_SERVER")
# ods_db = os.getenv("ODS_DB_NAME")
# ods_userid = os.getenv("DB_USERID")
# ods_pass = os.getenv("DB_PASSWD")

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

"""
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
"""
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
"""

"""
Created_on: 20-01-2020

Author: Satya Kommuri
Author id : sk2vk

Description: SQL server Database connection functions
"""

import config
import logging
import sqlalchemy as sa
import pandas as pd
import numpy as np
import math


class DBConnector:
    def __init__(self,
        dialect=config.dialect,
        # server=config.server_name,
        server=config.server_name_t,
        db_name=config.db_name,
        service_user=config.service_user,
        service_pass=config.service_pass):
        self.conn = None
        self.dialect = dialect
        self.server = server
        self.db_name = db_name
        self.service_user = service_user
        self.service_pass = service_pass

    def connect(self):
        dbconnstr = f'{self.dialect}://{self.service_user}:{self.service_pass}@{self.server}/{self.db_name}'\
                            f'?driver={config.db_driver}&trusted_connection={config.trusted_connection}'
        try:
            logging.info("Establishing connection to DB. . .")
            self.conn = sa.create_engine(dbconnstr, convert_unicode=True, fast_executemany=True)
            logging.info("Connected to DB.")
        except Exception as ex:
            logging.exception(f'Error occurred while establishing DB connection : {ex}')
            raise Exception(f'Error occurred while establishing DB connection : {ex}')

    def close_engine(self):
        self.conn.dispose()

    def execute(self, sql, params=None):
        try:
            self.conn.execute(sql, params=params)
            logging.info("Successfully executed query!")
        except Exception as ex:
            logging.exception(f'Error occurred while executing query: {ex}')
            raise Exception(f'Error occurred while executing query: {ex}')

    def get_data(self, sql, params=None):
        try:
            df = pd.read_sql(sql, self.conn, params=params)
            return df
        except Exception as ex:
            logging.exception(f'Error while retriving data : {ex}')
            raise Exception(f'Error while retriving data : {ex}')

    def insert_data(self, df, table, schema):
        try:
            chunk_size = math.floor(2100/len(df.columns)) - 1
            df.to_sql(table, con=self.conn, schema=schema, if_exists='append', index=False, method='multi',
            chunksize=chunk_size)
        except Exception as ex:
            logging.exception(f'Error while inserting data to DB: {ex}')
            raise Exception(f'Error while inserting data to DB: {ex}')

"""
Created_on: 26-01-2020

Author: Satya Kommuri
Author id : sk2vk

Description: Connect to MDM DB and get department/Unit details.
"""

import re
import config
import logging
from utils import datetime_gmt
from db_connector import DBConnector
# from sql import ods_unit_query
from sql import get_test_data

# def get_units():
#     start_time = datetime_gmt()
#     try:
#         conn = DBConnector(server=config.ods_server,
#         db_name=config.ods_db,
#         service_user=config.ods_userid,
#         service_pass=config.ods_pass)
#         conn.connect()
#         data = conn.get_data(ods_unit_query.format(config.mdm_unit_tbl))
#         conn.close_engine()
#         logging.info(
#             f"PERFORMANCE DETAILS: Time taken for getting units : {(datetime_gmt() - start_time).total_seconds()} seconds")
#         return data

#     except Exception as ex:
#         logging.exception(f"Error occurred while gathering unit/department list from ODS server: {ex}")
#         raise Exception(f"Error occurred while gathering unit/department list from ODS server: {ex}")


def get_dbdata():
    start_time = datetime_gmt()
    try:
        conn = DBConnector(server=config.server_name_t,
        db_name=config.db_name,
        service_user=config.service_user,
        service_pass=config.service_pass)
        conn.connect()
        data = conn.get_data(get_test_data.format(config.test_tbl))
        conn.close_engine()
        logging.info(
            f"PERFORMANCE DETAILS: Time taken for getting units : {(datetime_gmt() - start_time).total_seconds()} seconds")
        return data

    except Exception as ex:
        logging.exception(f"Error occurred while gathering unit/department list from ODS server: {ex}")
        raise Exception(f"Error occurred while gathering unit/department list from ODS server: {ex}")
"""
def get_patient_groups(unit_grp):
    if 'Adult' in unit_grp:
        return 'Adult'
    elif 'COVID' in unit_grp:
        return 'COVID'
    elif unit_grp in ['NICU', 'PICU', 'Peds ICU', 'Peds Acute']:
        return 'Peds'
    else:
        return unit_grp


def get_admitted_pat_group(pat_grp, active_flag):
    if ((pat_grp in ['Adult', 'COVID', 'Peds', 'Psych']) or ('Women' in pat_grp)) and (active_flag == True):
        return 'Patient in Beds'
    return pat_grp


def women_and_children(bed_name, unit_grp):
    child_bed_pattern = "([0-9]+)([a-zA-Z][a-zA-Z]+)"
    pattern = re.compile(child_bed_pattern)
    if pattern.findall(bed_name) and 'Women' in unit_grp:
        return True
    else:
        return False


def bed_unit_config(bed_name, unit_id, active_flag):
    if (((bed_name in ('7125B', '7126B', '7127B', '7128B')) and unit_id == 10243100) or
            ((bed_name in ('7131B', '7132B', '7196B', '7197B', '7198B')) and unit_id == 10243043) or
            ((bed_name in ('8144A', '8144B', '8145A', '8145B', '8146A')) and unit_id == 10243066) or
            ((bed_name in ('8130B', '8132B')) and unit_id == 10243094) or
            (bed_name == '5196A' and unit_id == 10243046) or
            ((bed_name in ('4328X0', '4328X1','4328X2','4328X3','4328X4')) and unit_id == 10243123)):
        return False
    return active_flag


def covid_active_flag(bed_name, unit_grp, bed_available, unit_id, active_flag):
    '''
    :param bed_name:
    :param unit_grp:
    :param bed_available:
    :param unit_id:
    :param active_flag:
    :return: False for 1. COVID 4 south CVICU beds moved to Acute,
    2. All 'B' COVID beds in 3 South and 5 South
    3. 4306B - 4325B in 4 sSouth Acute - since they are part of 4 South CVICU
    '''
    if ((('covid' in unit_grp.lower()) and ('b' in bed_name.lower()) and (unit_id == 10243122)) or \
        # Moving 5 South to semi private to private function (('b' in bed_name.lower()) and (unit_id == 10243124)) or \
        ((bed_name in (
        '4301A', '4302A', '4303A', '4304A', '4305A', '4326A', '4327A', '4328A')) and unit_id == 10243123) or \
        ((bed_name not in (
        '4301B', '4302B', '4303B', '4304B', '4305B', '4326B', '4327B', '4328B')) and unit_id == 10243136)) and \
            (bed_available != 'Occupied'):
        return False
    return active_flag


def peds_transformations(df):
    df_n = df[df['Bed_Name'].isin(['7191A', '7191B', '7191C'])].copy()
    df_rest = df[~df['Bed_Name'].isin(['7191A', '7191B', '7191C'])].copy()

    if 'Occupied' in df_n.values:
        df_n['Active_Flag'] = df_n[['Bed_Available', 'Active_Flag']] \
            .apply(lambda x: True if x['Bed_Available'] == 'Occupied' else False, axis=1)
        return df_rest.append(df_n)
    elif 'Not allocated' in df_n.values:
        df_n['Active_Flag'] = df_n[['Bed_Available', 'Active_Flag']] \
            .apply(lambda x: True if x['Bed_Available'] == 'Not allocated' else False, axis=1)
        return df_rest.append(df_n)
    return df


bed_ranks = {'Occupied': 3,
'Not allocated': 2,
'Unavailable': 1}


def semi_private_to_private(df):
    '''
    This function filters one bed per room to be active. Semi private rooms have multiple beds and private rooms have
    only one bed allocated or used at once.
    :param df:
    :return :df
    '''
    room_pattern = "([0-9]+)([a-zA-Z]+)"
    pattern = re.compile(room_pattern)
    df['Derived_Room'] = df['Bed_Name'].apply(lambda x: pattern.match(x).groups()[0] if pattern.match(x) else x)
    df['rank'] = df['Bed_Available'].apply(lambda x: bed_ranks.get(x))

    def dyn_func(df, unit_id):
        df_1 = df[(df['Unit_ID'] == unit_id) & (df['Newborn_Bed'] == False) & (df['Event_Type'] != 'Discharges')].copy()
        df_rest = df[~((df['Unit_ID'] == unit_id) & (df['Newborn_Bed'] == False) & (df['Event_Type'] != 'Discharges'))].copy()
        df_1 = df_1.sort_values(['rank'], ascending=False)
        m1 = df_1['Bed_Available'].eq('Occupied')
        m2 = (~df_1.duplicated(['Derived_Room']))
        m3 = df_1['Derived_Room'].map(df_1['Derived_Room'].value_counts()).eq(1)
        df_1['Active'] = m1 | m2 | m3
        df_1['Active_Flag'] = df_1[['Active_Flag', 'Active']].apply(
            lambda x: x['Active_Flag'] if x['Active'] else False, axis=1)
        return df_rest.append(df_1.sort_index())

    unit_list = [10243068, 10243066, 10243124]

    for unit_id in unit_list:
        df = dyn_func(df, unit_id)
    return df


def moved_unmanaged_beds(df):
    '''
    This filter deactivates all beds that are moved to different units from original unit and are not captured in config.
    :return:
    '''
    # df['rank'] = df['Bed_Available'].apply(lambda x: bed_ranks.get(x))
    df_rest = df[
        df['Bed_Name'].isin([None, '']) | df['Event_Type'].isin(['ED Boarders', 'Transfers', 'Post-Op', 'Discharges'])].copy()
    df_1 = df[~(df['Bed_Name'].isin([None, '']) | df['Event_Type'].isin(
        ['ED Boarders', 'Transfers', 'Post-Op', 'Discharges']))].copy()
    df_1 = df_1.sort_values(['rank', 'Active_Flag'], ascending=False)
    duplicates = (~df_1.duplicated('Bed_Name'))
    df_1['Active_Flag'] = df_1['Active_Flag'] & duplicates
    return df_rest.append(df_1.sort_index())


# Tableau calculations
def get_adults_peds_unit_group(unt_grp):
    if unt_grp in ('Adult Acute', 'Adult ICU', 'Adult IMU', 'Psych', 'COVID Acute', 'COVID ICU'):
        return 'Adult'
    elif 'Womens' in unt_grp:
        return 'Adult'
    elif unt_grp in ('NICU', 'Peds Acute', 'Peds ICU'):
        return 'Peds'
    else:
        return 'Other'


# Tableau calculations
adult_unt_group_config = {'Adult Acute': 'Acute',
'Adult ICU': 'ICU',
'Adult IMU': 'IMU'}


def get_adults_unit_group(unt_grp):
    return adult_unt_group_config.get(unt_grp) or ''


def get_unit_group_categories(unt_grp, unit):
    if (unt_grp in (None, '', 'Not used')) or (unit == '3 South'):
        return 'Not used'
    elif unt_grp in ('COVID Acute', 'COVID ICU'):
        return 'COVID'
    elif unt_grp in ('Adult Acute', 'Adult ICU', 'Adult IMU'):
        return 'Adult'
    elif unt_grp in ('NICU', 'Peds Acute', 'Peds ICU'):
        return 'Peds'
    elif 'Womens' in unt_grp:
        return 'Womens'
    else:
        return unt_grp
"""

if __name__ == '__main__':
    get_dbdata()
