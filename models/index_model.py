import sqlite3
import pandas as pd

#функция изменения базы данных
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#Вывести услуги для процедур
def get_ProcedureList(con):
    return pd.read_sql("""SELECT IDProcedureList, ProcedureListName , ProcedurePrice, P.ProcedureName  
    FROM ProcedureList
    JOIN "Procedure" P on P.IDProcedure = ProcedureList.Procedure_IDProcedure 
    order by ProcedurePrice ASC 
    """,con)

