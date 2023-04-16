import pandas as pd
import sqlite3 as sq
sInputFileName = 'student.csv'
InputData = pd.read_csv(sInputFileName)
print(InputData)
ProcessData = InputData
OutputData = ProcessData
SOutputFileName = 'utility.db'
sOutputTable = 'Employee'
conn = sq.connect(SOutputFileName)
OutputData.to_sql(sOutputTable, conn, if_exists="replace")
print('Done')
