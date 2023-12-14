import pyodbc
from pandas import DataFrame
from numpy import array

from dbconn.dbs.dbs_base import BaseDb



class SSMSConnPyodbc(BaseDb):
    
    def __init__(self):
        super().__init__("pyodbc")
        self.connection = None #TODO


    def connect(self,server:str, database:str) -> None:
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                  'Server='+server+';'
                  'Database='+database+';'
                  'Trusted_Connection=yes;')

        return conn
        

    def disconnect(connection):
        connection.close()

    def run_query(self,connection, sqlQuery:str)-> None:
        cols = []

        try:
            cursor = connection.cursor() 

            result = cursor.execute(sqlQuery) 
            rows = result.fetchall() 

        #while row: 
        #    print(row)
        #    row = cursor.fetchone()
        except Exception as e:
            print("Couldnt query the table, ", e)
            return [], []
        #columns = [column[0] for column in cursor.description]

        if len(rows)>0:
            cols = list(rows[0].keys())
        
        #WORKS for pyodbc but not for pymsql
        for i,_ in enumerate(result.description): #WORKS for pyodbc but not for pymsql
            cols.append(result.description[i][0]) #WORKS for pyodbc but not for pymsql
        for row in cursor:
            cols.append(row)
        

        return rows, cols
    

    def run_query_to_df(self,connection, sqlQuery:str):
        rows, cols = self.run_query(connection, sqlQuery)
        if len(rows)==0:
            print(f'ERROR! Query returned empty table! Code: {sqlQuery}')
            return []
        else:
            df = DataFrame(array(rows), columns=cols)
            #df = pd.DataFrame(rows, columns=cols)
            return df



