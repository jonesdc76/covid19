import sqlite3
from datetime import datetime as dt
import pandas as pd
import os
from pandas import DataFrame
fname = 'covid19.db'
os.remove(fname)
os.system('python3 makeDB.py')
conn = sqlite3.connect(fname)
c= conn.cursor()

readcov = pd.read_csv (r'COVID19cases.csv')
readcov['Date'] = pd.to_datetime(readcov['Date'],format = "%m/%d/%y").dt.date
print(readcov['Date'])        
readcov.to_sql('covid_data', conn, if_exists='replace', index = False)
