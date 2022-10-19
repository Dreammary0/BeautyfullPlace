import sqlite3
con = sqlite3.connect("beautyfull.sqlite")
f_damp = open('Beauty.sql','r', encoding ='utf-8-sig')
damp = f_damp.read()
f_damp.close()
# запускаем запросы
con.executescript(damp)
# сохраняем информацию в базе данных
con.commit()
# создаем курсор
cursor = con.cursor()
# выбираем и выводим записи из таблиц author, reader


print("1.1 Вывести услуги для процедуры Парикмахер")
cursor.execute("""SELECT ProcedureListName , ProcedurePrice, P.ProcedureName  
FROM ProcedureList
JOIN "Procedure" P on P.IDProcedure = ProcedureList.Procedure_IDProcedure 
WHERE Procedure_IDProcedure=1 
order by ProcedurePrice ASC 
""")
print(cursor.fetchall())

print("1.2 Вывести мастеров процедуры")
cursor.execute("""
SELECT MasterName , P.ProcedureName
FROM Master
JOIN "Procedure" P on P.IDProcedure = Master.Procedure_IDProcedure
Where Procedure_IDProcedure=2
ORDER BY MasterName ASC 
""")
print(cursor.fetchall())


print("2.1 Сколько процедур у каждой услуги")
cursor.execute("""
Select P.ProcedureName, count(IDProcedureList) 
from ProcedureList 
JOIN "Procedure" P on P.IDProcedure = ProcedureList.Procedure_IDProcedure 
GROUP BY P.ProcedureName
""")
print(cursor.fetchall())

print("2.1 Какие даты есть у мастера")
cursor.execute('''
select Date, StartTime, EndTime, M.MasterName, P.ProcedureName
from Schedule
JOIN Procedure P on P.IDProcedure = M.Procedure_IDProcedure
JOIN Master M on M.IDMaster = Schedule.Master_IDMaster
Where Master_IDMaster=1
GROUP BY Date
''')
print(cursor.fetchall())


print("3.1 Самая дорогая процедура")
cursor.execute('''
with test as (select IDProcedureList, max(ProcedurePrice) as price from ProcedureList)
select P2.ProcedureName, P.ProcedureListName, t.price
from ProcedureList P, test t 
join "Procedure" P2 on P2.IDProcedure = P.Procedure_IDProcedure
where P.IDProcedureList = t.IDProcedureList

''')
print(cursor.fetchall())


print("3.2 Вывести доступные варианты записи на процедуру 1 после 18:00 и мастеров")
cursor.execute('''
with night as (select * from OrderList where Procedure_IDProcedure=1 and OrderTime>=18 and Client_IDClient is NULL)
select IDOrder, P.ProcedureName, OrderData, OrderTime,M.MasterName, M.MasterPhone 
from night
join Schedule S on night.Schedule_IDSchedule=S.IDSchedule
join Master M on S.Master_IDMaster=M.IDMaster
join Procedure P on M.Procedure_IDProcedure=P.IDProcedure
''')
print(cursor.fetchall())

#
cursor.execute('''
select * from OrderList
''')
print(cursor.fetchall())




# закрываем соединение с базой
con.close()
