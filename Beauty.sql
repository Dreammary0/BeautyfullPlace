BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Chek_has_ProcedureList";
CREATE TABLE IF NOT EXISTS "Chek_has_ProcedureList" (
	"Chek_IDChek"	INT NOT NULL,
	"ProcedureList_IDProcedureList"	INT NOT NULL,
	CONSTRAINT "fk_Chek_has_ProcedureList_ProcedureList1" FOREIGN KEY("ProcedureList_IDProcedureList") REFERENCES "ProcedureList"("IDProcedureList") ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT "fk_Chek_has_ProcedureList_Chek1" FOREIGN KEY("Chek_IDChek") REFERENCES "Chek"("IDChek") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("Chek_IDChek","ProcedureList_IDProcedureList")
);
DROP TABLE IF EXISTS "Client";
CREATE TABLE IF NOT EXISTS "Client" (
	"IDClient"	INTEGER NOT NULL,
	"ClientName"	VARCHAR(45) NOT NULL,
	"ClientPhone"	VARCHAR(12),
	PRIMARY KEY("IDClient" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Master";
CREATE TABLE IF NOT EXISTS "Master" (
	"IDMaster"	INTEGER NOT NULL,
	"MasterName"	VARCHAR(45) NOT NULL,
	"MasterPhone"	VARCHAR(12) NOT NULL,
	"Procedure_IDProcedure"	INT NOT NULL,
	CONSTRAINT "fk_Master_Procedure1" FOREIGN KEY("Procedure_IDProcedure") REFERENCES "Procedure"("IDProcedure") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("IDMaster" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Chek";
CREATE TABLE IF NOT EXISTS "Chek" (
	"IDChek"	INTEGER NOT NULL,
	"OrderList_IDOrder"	INT NOT NULL,
	"Price"	REAL,
	"ChekDate"	DATE,
	"ChekClient"	VARCHAR(45),
	CONSTRAINT "fk_Chek_OrderList1" FOREIGN KEY("OrderList_IDOrder") REFERENCES "OrderList"("IDOrder") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("IDChek" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Procedure";
CREATE TABLE IF NOT EXISTS "Procedure" (
	"IDProcedure"	INTEGER NOT NULL,
	"ProcedureName"	VARCHAR(45) NOT NULL,
	PRIMARY KEY("IDProcedure" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Schedule";
CREATE TABLE IF NOT EXISTS "Schedule" (
	"IDSchedule"	INTEGER NOT NULL,
	"Date"	DATE,
	"StartTime"	TIME,
	"EndTime"	TIME,
	"Master_IDMaster"	INT NOT NULL,
	CONSTRAINT "fk_Schedule_Master1" FOREIGN KEY("Master_IDMaster") REFERENCES "Master"("IDMaster") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("IDSchedule" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "ProcedureList";
CREATE TABLE IF NOT EXISTS "ProcedureList" (
	"IDProcedureList"	INTEGER NOT NULL UNIQUE,
	"ProcedureListName"	VARCHAR(20) NOT NULL,
	"ProcedurePrice"	REAL NOT NULL,
	"Procedure_IDProcedure"	INT NOT NULL,
	CONSTRAINT "fk_ProcedureList_Procedure1" FOREIGN KEY("Procedure_IDProcedure") REFERENCES "Procedure"("IDProcedure") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("IDProcedureList")
);
DROP TABLE IF EXISTS "Hours";
CREATE TABLE IF NOT EXISTS "Hours" (
	"NUM"	INTEGER
);
DROP TABLE IF EXISTS "OrderList";
CREATE TABLE IF NOT EXISTS "OrderList" (
	"IDOrder"	INTEGER NOT NULL,
	"OrderData"	DATE,
	"OrderTime"	TIME,
	"Client_IDClient"	INT,
	"Schedule_IDSchedule"	INT NOT NULL,
	"Procedure_IDProcedure"	INT NOT NULL,
	CONSTRAINT "fk_OrderList_Client1" FOREIGN KEY("Client_IDClient") REFERENCES "Client"("IDClient") ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT "fk_OrderList_Schedule1" FOREIGN KEY("Schedule_IDSchedule") REFERENCES "Schedule"("IDSchedule") ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT "fk_OrderList_Procedure1" FOREIGN KEY("Procedure_IDProcedure") REFERENCES "Procedure"("IDProcedure") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("IDOrder" AUTOINCREMENT)
);




INSERT INTO "Chek_has_ProcedureList" ("Chek_IDChek","ProcedureList_IDProcedureList") VALUES (1,9),
 (1,10),
 (1,12);
INSERT INTO "Client" ("IDClient","ClientName","ClientPhone") VALUES (1,'Мария','721200'),
 (2,'Соня','421278'),
 (3,'Денис','678264'),
 (4,'Аня','690253'),
 (5,'Павел','773829'),
 (6,'Вероника','709453'),
 (7,'Варвара','276355'),
 (8,'Евгений','882293'),
 (9,'Даша','221638'),
 (10,'Лариса','901267');
INSERT INTO "Master" ("IDMaster","MasterName","MasterPhone","Procedure_IDProcedure") VALUES (1,'Лиза','236725',1),
 (2,'Мрина','876362',2),
 (3,'Эдуард','564378',3),
 (4,'Андрей','983627',4),
 (5,'Жанна','256394',5),
 (6,'Томара','982514',1),
 (7,'Валентина','123364',2),
 (8,'Катя','428764',3),
 (9,'Эльмир','907532',4),
 (10,'Авдотья','127855',5);
INSERT INTO "Chek" ("IDChek","OrderList_IDOrder","Price","ChekDate","ChekClient") VALUES (1,1,1000.0,'2022.12.07','Мария');
INSERT INTO "Procedure" ("IDProcedure","ProcedureName") VALUES (1,'Парикмахер'),
 (2,'Маникюр'),
 (3,'Визажист'),
 (4,'Шугаринг'),
 (5,'Косметолог');
INSERT INTO "Schedule" ("IDSchedule","Date","StartTime","EndTime","Master_IDMaster") VALUES (1,'2022.12.01','12:00','17:00',1),
 (2,'2022.12.03','15:00','20:00',1),
 (3,'2022.12.05','12:00','17:00',1),
 (4,'2022.12.01','12:00','17:00',4),
 (5,'2022.12.03','16:00','21:00',5),
 (6,'2022.12.05','12:00','17:00',3),
 (7,'2022.12.01','10:00','15:00',2),
 (8,'2022.12.07','12:00','17:00',2);
INSERT INTO "ProcedureList" ("IDProcedureList","ProcedureListName","ProcedurePrice","Procedure_IDProcedure") VALUES (1,'Мужская стрижка',300.0,1),
 (2,'Женская стрижка',500.0,1),
 (3,'Детская стрижка',1000.0,1),
 (4,'Укладка',500.0,1),
 (5,'Мытье головы',300.0,1),
 (6,'Ламинирование волос ',2000.0,1),
 (7,'Кератиновое выпрямление',5000.0,1),
 (8,'Плетение кос',3000.0,1),
 (9,'Снятие чужого покрытия',200.0,2),
 (10,'Аппаратный маникюр',1000.0,2),
 (11,'Аппаратный педикюр',1200.0,2),
 (12,'Покрытие гель лаком',600.0,2),
 (13,'Дизайн ногтей',300.0,2),
 (14,'Наращивание ногтей',2000.0,2),
 (15,'Ванночка для рук',150.0,2),
 (16,'Вечерний макияж',1500.0,3),
 (17,'Нюдовый макияж',1000.0,3),
 (18,'Макияж ненвсты',2000.0,3),
 (19,'Мужской макияж',1000.0,3),
 (20,'Обучение для подростка',3000.0,3),
 (21,'Подготовка к фотосессии',3000.0,3),
 (22,'Макияж на выпускной',3000.0,3),
 (23,'Комплекс на все тело',2500.0,4),
 (24,'Комплекс подмышки+бикини',1800.0,4),
 (25,'Глубокое бикини',1200.0,3),
 (26,'Ноги полностью',900.0,4),
 (27,'Механическая чистка',1500.0,5),
 (28,'Кислотный пилинг',2000.0,5),
 (29,'Лимфодренажный массаж',5000.0,5),
 (30,'Мезотерапия
',6000.0,5),
 (31,'Счастье для лица',10000.0,5);
INSERT INTO "Hours" ("NUM") VALUES (0),
 (1),
 (2),
 (3),
 (4),
 (5);
INSERT INTO "OrderList" ("IDOrder","OrderData","OrderTime","Client_IDClient","Schedule_IDSchedule","Procedure_IDProcedure") VALUES (1,'2022.12.01',12,NULL,1,1),
 (2,'2022.12.01',13,NULL,1,1),
 (3,'2022.12.01',14,NULL,1,1),
 (4,'2022.12.01',15,NULL,1,1),
 (5,'2022.12.01',16,NULL,1,1),
 (6,'2022.12.01',17,NULL,1,1),
 (7,'2022.12.03',15,NULL,2,1),
 (8,'2022.12.03',16,NULL,2,1),
 (9,'2022.12.03',17,NULL,2,1),
 (10,'2022.12.03',18,NULL,2,1),
 (11,'2022.12.03',19,NULL,2,1),
 (12,'2022.12.03',20,NULL,2,1),
 (13,'2022.12.05',12,NULL,3,1),
 (14,'2022.12.05',13,NULL,3,1),
 (15,'2022.12.05',14,NULL,3,1),
 (16,'2022.12.05',15,NULL,3,1),
 (17,'2022.12.05',16,NULL,3,1),
 (18,'2022.12.05',17,NULL,3,1),
 (19,'2022.12.01',12,NULL,4,4),
 (20,'2022.12.01',13,NULL,4,4),
 (21,'2022.12.01',14,NULL,4,4),
 (22,'2022.12.01',15,NULL,4,4),
 (23,'2022.12.01',16,NULL,4,4),
 (24,'2022.12.01',17,NULL,4,4),
 (25,'2022.12.03',16,NULL,5,5),
 (26,'2022.12.03',17,NULL,5,5),
 (27,'2022.12.03',18,NULL,5,5),
 (28,'2022.12.03',19,NULL,5,5),
 (29,'2022.12.03',20,NULL,5,5),
 (30,'2022.12.03',21,NULL,5,5),
 (31,'2022.12.05',12,NULL,6,3),
 (32,'2022.12.05',13,NULL,6,3),
 (33,'2022.12.05',14,NULL,6,3),
 (34,'2022.12.05',15,NULL,6,3),
 (35,'2022.12.05',16,NULL,6,3),
 (36,'2022.12.05',17,NULL,6,3),
 (37,'2022.12.01',10,NULL,7,2),
 (38,'2022.12.01',11,NULL,7,2),
 (39,'2022.12.01',12,NULL,7,2),
 (40,'2022.12.01',13,NULL,7,2),
 (41,'2022.12.01',14,NULL,7,2),
 (42,'2022.12.01',15,NULL,7,2),
 (43,'2022.12.07',12,NULL,8,2),
 (44,'2022.12.07',13,NULL,8,2),
 (45,'2022.12.07',14,NULL,8,2),
 (46,'2022.12.07',15,NULL,8,2),
 (47,'2022.12.07',16,NULL,8,2),
 (48,'2022.12.07',17,NULL,8,2);



DROP VIEW IF EXISTS "Timing";
CREATE VIEW Timing as 
Select P.IDProcedure as idP, IDSchedule as idS, M.MasterName, Date as date, StartTime+H.Num as Hour
from Schedule
cross join Hours H
Join Master M on Schedule.Master_IDMaster=M.IDMaster
Join Procedure P on M.Procedure_IDProcedure = P.IDProcedure;
COMMIT;
