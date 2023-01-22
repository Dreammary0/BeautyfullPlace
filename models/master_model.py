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


#Вывести мастеров для выбранных процедур
def get_Masters_for_procedure(conn, procedures_list):
    df = pd.read_sql("""
    SELECT IDMaster, MasterName , P.ProcedureName
    FROM Master
    JOIN "Procedure" P on P.IDProcedure = Master.Procedure_IDProcedure
    ORDER BY P.ProcedureName """, conn)
    if procedures_list:
        df = df[df.ProcedureName.isin(procedures_list)]
    return df


# Какие окошки есть у мастера
def get_Master_records(con, master):
    df = pd.read_sql(f'''
    select IDOrder, OrderData as Дата, OrderTime as Время, Client_IDClient as Запись, M.MasterName, P.ProcedureName
    from OrderList
    JOIN Schedule S on Schedule_IDSchedule=S.IDSchedule
    JOIN Master M on S.Master_IDMaster=M.IDMaster 
    join Procedure P on M.Procedure_IDProcedure = P.IDProcedure
    where Master_IDMaster={master}
    ''',con)
    # if master_list:
    #     m_list=[]
    #     for elem in master_list:
    #         m_list.append(int(elem))
    #     print(m_list)
    #     df = df[df.Master_IDMaster.isin(list(m_list))]
    df['Запись'] = df['Запись'].fillna(0)
    return df

#Окошки в выбранные даты (с указанным мастером для перебора в цикле контроллера)
def get_Find_time_date(con, dateStart, dateEnd, name):
        df=pd.read_sql(f'''
        select IDOrder, OrderData as Дата, OrderTime as Время, Client_IDClient as Запись, M.MasterName, P.ProcedureName, M.IDMaster
        from OrderList
        JOIN Schedule S on Schedule_IDSchedule=S.IDSchedule
        JOIN Master M on S.Master_IDMaster=M.IDMaster 
        join Procedure P on M.Procedure_IDProcedure = P.IDProcedure
        WHERE OrderData>='{dateStart}' and OrderData<='{dateEnd}' and MasterName='{name}'
    ''',con)
        df['Запись'] = df['Запись'].fillna(0)
        return df

