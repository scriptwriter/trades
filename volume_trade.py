#!/usr/bin/python

import requests


API_KEY='3ggX5z2Ftps6ozsoMNVX'
START_DAY='2015-01-01'
COMPANY_LIST_FILE='./company_list'
QUERY="https://www.quandl.com/api/v3/datasets/NSE/COMPANY.json?column_index={}&start_date={}&api_key={}".format(6,START_DAY,API_KEY)
#<>&start_date=2017-01-01&<>

with open(COMPANY_LIST_FILE) as f:
    COMPANY_LIST = f.read().splitlines()


for COMPANY in COMPANY_LIST:
    try:
        datapoints = requests.get(QUERY.replace('COMPANY', COMPANY)).json()['dataset']['data']
        vols = [int(datapoint[1]) for datapoint in datapoints]
        if vols[0] == max(vols):
            print COMPANY*20
    except:
        print "Error - " + COMPANY
        pass
