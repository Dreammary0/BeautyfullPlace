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



def Task1(con):
    print("1.1 Вывести услуги для процедуры Парикмахер")
    return pd.read_sql("""SELECT ProcedureListName , ProcedurePrice, P.ProcedureName  
    FROM ProcedureList
    JOIN "Procedure" P on P.IDProcedure = ProcedureList.Procedure_IDProcedure 
    WHERE Procedure_IDProcedure=1 
    order by ProcedurePrice ASC 
    """,con)

def Task2(con):
    print("1.2 Вывести мастеров процедуры")
    return pd.read_sql("""
    SELECT MasterName , P.ProcedureName
    FROM Master
    JOIN "Procedure" P on P.IDProcedure = Master.Procedure_IDProcedure
    Where Procedure_IDProcedure=2
    ORDER BY MasterName ASC 
    """,con)

def Task3(con):
    print("2.1 Сколько процедур у каждой услуги")
    return pd.read_sql("""
    Select P.ProcedureName, count(IDProcedureList) 
    from ProcedureList 
    JOIN "Procedure" P on P.IDProcedure = ProcedureList.Procedure_IDProcedure 
    GROUP BY P.ProcedureName
    """,con)

def Task4(con):
    print("2.1 Какие даты есть у мастера")
    return pd.read_sql('''
    select Date, StartTime, EndTime, M.MasterName, P.ProcedureName
    from Schedule
    JOIN Procedure P on P.IDProcedure = M.Procedure_IDProcedure
    JOIN Master M on M.IDMaster = Schedule.Master_IDMaster
    Where Master_IDMaster=1
    GROUP BY Date
    ''',con)

def Task5(con):
    print("3.1 Самая дорогая процедура")
    return pd.read_sql('''
    with test as (select IDProcedureList, max(ProcedurePrice) as price from ProcedureList)
    select P2.ProcedureName, P.ProcedureListName, t.price
    from ProcedureList P, test t 
    join "Procedure" P2 on P2.IDProcedure = P.Procedure_IDProcedure
    where P.IDProcedureList = t.IDProcedureList

    ''',con)

def Task6(con):
    print("3.2 Вывести доступные варианты записи на процедуру 1 после 18:00 и мастеров")
    return pd.read_sql('''
    with night as (select * from OrderList where Procedure_IDProcedure=1 and OrderTime>=18 and Client_IDClient is NULL)
    select IDOrder, P.ProcedureName, OrderData, OrderTime,M.MasterName, M.MasterPhone 
    from night
    join Schedule S on night.Schedule_IDSchedule=S.IDSchedule
    join Master M on S.Master_IDMaster=M.IDMaster
    join Procedure P on M.Procedure_IDProcedure=P.IDProcedure
    ''',con)


def Task7(con):
    print("4.1 Добавить клиента")
    Add_Client='''
    INSERT INTO Client ("IDClient","ClientName","ClientPhone") 
    VALUES (null, 'Марина','574374')
/*    DELETE FROM Client where IDClient>10;
    UPDATE SQLITE_SEQUENCE SET seq = 1 WHERE name = 'Client';*/
    '''
    execute_query(con, Add_Client)


def Task8(con):
    print("4.2 Записать клиента на процедуру")
    Reg_for_proc='''
    UPDATE OrderList SET Client_IDClient = 1 WHERE IDOrder=1
    '''
    execute_query(con, Reg_for_proc)

