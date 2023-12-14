
import pymssql
from pandas import DataFrame

import os
from src.dbconn.dbs.dbs_base import BaseDb



class SSMSConnPymssql(BaseDb):
    
    def __init__(self):
        super().__init__("pymssql")
        self._conn_info = {
            'user': os.getenv("snowflake_db_user"),
            'password': os.getenv("snowflake_db_password"),
            'account': os.getenv("snowflake_db_account"),
            'database': os.getenv("snowflake_db_database") ,
            #'warehouse': None ,
            #'role': None
            #'log_level': logging.WARNING    
            }
        self.connection = None
        
    def connect(self,server:str, user:str, password:str, database:str):
        conn = pymssql.connect(server, user, password, database)
        return conn 


    def disconnect(connection):
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





