import pandas as pd
import sqlite3 as sq

sInputFileName = 'utility.db'
sInputTable = 'employee'

conn=sq.connect(sInputFileName)
sSql='select * from ' + sInputTable + ';'
InputData=pd.read_sql_query(sSql,conn)
print(InputData)
print(InputData)
ProcessData = InputData

ProcessData.drop('email', axis=1, inplace=True)
print("===============Process data value===============")
print(InputData)

ProcessData.rename(columns={'name': 'emp_name'}, inplace=True)
ProcessData.rename(columns={'phone': 'emp_Phone'}, inplace=True)
print(ProcessData)
OutputData = ProcessData
OutputData.to_csv('P4.csv')
print('Done') 
