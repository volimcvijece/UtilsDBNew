from src.dbconn.dbs import ssms_odbc, ssms_pymssql


def choose_connection(dbs_type):
    if dbs_type == "ssms_odbc":
        return ssms_odbc.SSMSConnPyodbc()
    elif dbs_type == "ssms_pymssql":
        return ssms_pymssql.SSMSConnPymssql()
    else:
        #raise Exception("You have to specify dbms connection [ssms_odbc, ssms_pymssql]")
        print("You have to specify dbms connection [ssms_odbc, ssms_pymssql]")