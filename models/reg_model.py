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


#информация по записи при нажатии кнопки времени OrderList
def get_OrderListInfo_for_RegPage(con, id_order_list, procedure_name):
    df = pd.read_sql(f'''SELECT IDOrder, OrderData, OrderTime, M.MasterName, P.ProcedureName
    FROM OrderList
    join Schedule S on OrderList.Schedule_IDSchedule = S.IDSchedule
    join Master M on M.IDMaster = S.Master_IDMaster
    join Procedure P on OrderList.Procedure_IDProcedure = P.IDProcedure
    where P.ProcedureName='{procedure_name}'
    ''',con)
    if id_order_list:
        m_list=[]
        for elem in id_order_list:
            m_list.append(int(elem))
        df = df[df.IDOrder.isin(list(m_list))]
        indx = pd.Index(range(0, len(df), 1))
        df = df.set_index(indx)
    return df

# Сумма чека заказа
def get_check_sum(conn, service_list):
    df = pd.read_sql("""
    SELECT ProcedureListName,ProcedurePrice
    from ProcedureList """, conn)
    df=df.loc[df['ProcedureListName'].isin(service_list), 'ProcedurePrice'].sum()
    return df

# Добавить нового клиента
def AddNewClient(con, name, phone):
    Add_Client=f"""
    INSERT INTO Client ("IDClient","ClientName","ClientPhone") 
    VALUES (null, '{name}','{phone}')
    """
    execute_query(con, Add_Client)

# Проверить, есть ли клиент в базе, если нет - добавить. Вернуть его айди.
def get_ClientId_for_chek(conn, name, phone):
    df = pd.read_sql(f"""    
    select * from Client 
    where ClientPhone='{phone}' and ClientName='{name}'
    """,conn)
    isempty = df.empty
    if isempty:
        AddNewClient(conn, name,phone)
        print('Клиент добавлен')
    else: print('Клиент уже есть в базе')
    df1 = pd.read_sql(f"""    
    select IDClient from Client 
    where ClientPhone='{phone}' and ClientName='{name}'
    """,conn)
    return df1['IDClient']. values [0]

# Записать клиента
def RecordClient (con, CLientID, OrderID):
    Reg_for_proc=f'''
    UPDATE OrderList SET Client_IDClient = '{CLientID}' WHERE IDOrder = '{OrderID}'
    '''
    execute_query(con, Reg_for_proc)

# Добавить запись в основной чек
def AddCheck(conn,price, idClient):
    Add_Client=f"""
    INSERT INTO Chek ("Price", "ChekDate", "Client_IDClient") 
    VALUES ('{price}',date('now'), '{idClient}')
    """

    execute_query(conn, Add_Client)
    df = pd.read_sql(f"""    
        select IDChek from Chek
        where Price='{price}' and Client_IDClient='{idClient}' and ChekDate = date('now')
       """, conn)
    print(df)
    return df['IDChek']. values [0]


# Добавить запись в множество окон записи чека
def AddCheck_Order(conn, idcheck, idorder):
    Add_check_order = f"""
        INSERT INTO Chek_has_OrderList ("Chek_IDChek", "OrderList_IDOrder") 
        VALUES ('{idcheck}', '{idorder}')
        """
    execute_query(conn, Add_check_order)



# Добавить запись в множество услуг чека
def AddCheck_Procedure(conn, idcheck, elem_service_list):

    df = pd.read_sql(f'''
    select IDProcedureList from ProcedureList
    where ProcedureListName = '{elem_service_list}'
    ''',conn)
    idprocedure = df['IDProcedureList'].values[0]

    Add_check_procedure = f"""
        INSERT INTO Chek_has_ProcedureList ("Chek_IDChek", "ProcedureList_IDProcedureList") 
        VALUES ('{idcheck}', '{idprocedure}')
        """
    execute_query(conn, Add_check_procedure)


#Удалить клиентов после тестирования
def DeleteTestClient(con):
    D_Client=f"""
    DELETE FROM Client where IDClient>10;
    UPDATE SQLITE_SEQUENCE SET seq = 1 WHERE name = 'Client';
    """
    execute_query(con, D_Client)

# Из рассписания мастеров создать окошки для записи в OrderList
def TimingToOrderLit(con):
    sql_code='''
    DROP VIEW IF EXISTS "Timing";
    CREATE VIEW Timing as
    Select P.IDProcedure as idP, IDSchedule as idS, M.MasterName, Date as date, StartTime+H.Num as Hour
    from Schedule
    cross join Hours H
    Join Master M on Schedule.Master_IDMaster=M.IDMaster
    Join Procedure P on M.Procedure_IDProcedure = P.IDProcedure;
    '''
    sql_code_insert='''
    INSERT INTO OrderList (OrderData,OrderTime,Schedule_IDSchedule,Procedure_IDProcedure)
    select date, Hour ,idS,idP from Timing
    '''
    execute_query(con, sql_code)
    execute_query(con, sql_code_insert)


# def Task6(con):
#     print("3.2 Вывести доступные варианты записи на процедуру 1 после 18:00 и мастеров")
#     return pd.read_sql('''
#     with night as (select * from OrderList where Procedure_IDProcedure=1 and OrderTime>=18 and Client_IDClient is NULL)
#     select IDOrder, P.ProcedureName, OrderData, OrderTime,M.MasterName, M.MasterPhone
#     from night
#     join Schedule S on night.Schedule_IDSchedule=S.IDSchedule
#     join Master M on S.Master_IDMaster=M.IDMaster
#     join Procedure P on M.Procedure_IDProcedure=P.IDProcedure
#     ''',con)




