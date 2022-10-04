
import os
import pandas as pd
import datetime
from sqlalchemy import create_engine  
import pymysql

csvFile = '/Users/apple/Desktop/python/my_accounting_system/電子發票明細.csv'

with open(csvFile) as file:
    data = file.read()
    data = data.split('M|')
    del data[:2]

    temp_receipts = [] 
    for comb in data:
        comb = comb.split('D|')
        temp_receipts.append(comb)

    temp_info = []
    for receipt in temp_receipts:
        receipt = receipt[0]
        temp_info.append(receipt)

    info = []
    for i in temp_info:
        i = i.split('|')
        info.append(i)           
    
    temp_details = []
    for receipt in temp_receipts:
        receipt = receipt[1:]
        temp_details.append(receipt)       

    details = []
    for detail in temp_details:
        for d in detail:
            d = d.split('|')
            details.append(d)


info_data = pd.DataFrame(info, columns = ['','','invoice_date','seller_id',
'seller_name','invoice_number','amount','invoice_status',''])
info_data = info_data.drop('',axis=1)

details_data = pd.DataFrame(details, columns = ['invoice_number','expense','item',''])
details_data = details_data.drop('',axis=1)

print(info_data)
print()
print(details_data)

