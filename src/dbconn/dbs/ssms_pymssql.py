
import pymssql
from pandas import DataFrame

from dbconn.dbs.dbs_base import BaseDb



class SSMSConnPymssql(BaseDb):
    
    def __init__(self):
        super().__init__("pymssql")
        self.connection = None #TODO
        
    def connect(self,server:str, user:str, password:str, database:str):
        conn = pymssql.connect(server, user, password, database)
        return conn 


    def disconnect(self, connection):
        connection.close()


    def run_query(self, connection, sqlQuery:str)-> None:
        rows=[]
        try:
            cursor=connection.cursor(as_dict=True)
            cursor.execute(sqlQuery) 

            rows = cursor.fetchall()

        except Exception as e:
            print("Couldnt query the table, ", e)

        return rows
    

    def run_query_to_df(self,connection, sqlQuery:str):
        rows = self.run_query(connection, sqlQuery)
        if len(rows)==0:
            print(f'ERROR! Query returned empty table! Code: {sqlQuery}')
            return []
        else:
            df = DataFrame(rows)
            #df = pd.DataFrame(rows, columns=cols)
            return df





