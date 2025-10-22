"""
Created_on: 05-02-2020

Author: Satya Kommuri
Author id : sk2vk

Description: Utilities file to help patient progression app
"""

import os
import config
import logging
import pandas as pd
from datetime import datetime, timedelta


def datetime_gmt():
    '''
    Function to check UTC time zone and convert to EST. Covers Day light saving conversion as well.
    :return:
    '''
    if datetime.now() == datetime.utcnow():
        return datetime.now() - timedelta(hours=5)
    elif datetime.now() == (datetime.utcnow() + timedelta(hours=1)):
        return datetime.now() - timedelta(hours=5)
    else:
        return datetime.now()


def read_from_csv(path=None):
    if not path:
        curr_dir = os.getcwd()
        path = os.path.join(curr_dir, 'Documents/xxxxx.csv')

    if os.path.exists(path):
        try:
            df = pd.read_csv(path, keep_default_na=False)
            return df
        except Exception as ex:
            logging.exception(f'Error occurred while read csv file {path}: {ex}')
            raise Exception(f'Error occurred while read csv file {path}: {ex}')


def retry(func, max_retries=1, retry_msg=None):
    for i in range(max_retries):
        try:
            data = func()
            if data.empty:
                continue
            return data
        except AttributeError:
            if retry_msg:
                logging.warning(retry_msg + f" : {i + 1} time.")
            continue
        except Exception as ex:
            logging.exception(ex)
            continue



