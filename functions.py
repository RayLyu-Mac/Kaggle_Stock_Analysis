import polars as pl
import requests
# to enrich the examples in this quickstart with dates
from datetime import datetime, timedelta 
# to generate data for the examples
import numpy as np 
from os import listdir
import matplotlib.pyplot as plt

def get_tag(stock_tag):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res=requests.get(f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{stock_tag}?formatted=true&crumb=ATn%2FOzVhnFV&lang=en-CA&region=CA&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CesgScores%2Cdetails&corsDomain=ca.finance.yahoo.com",headers=headers)
    stockSummary=res.json()['quoteSummary']['result'][0]['summaryProfile']
    return stockSummary["industry"],stockSummary["sector"]

def get_price(stock_tag,range):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res=requests.get(f"https://query2.finance.yahoo.com/v8/finance/chart/{stock_tag}?formatted=true&crumb=ATn%2FOzVhnFV&lang=en-CA&region=CA&events=capitalGain%7Cdiv%7Csplit&includeAdjustedClose=true&interval=1d&range={range}y&useYfid=true&corsDomain=ca.finance.yahoo.com",headers=headers)
    return res.json()["chart"]['result'][0]['timestamp'],res.json()["chart"]['result'][0]['indicators']['quote'][0]['close']