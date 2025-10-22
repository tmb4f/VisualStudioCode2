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
                 server=config.server_name,
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
