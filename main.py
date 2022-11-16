from jinja2 import Template, Environment, FileSystemLoader
import sqlite3
from sqlite3 import Error
from Beauty_Model import *

#создание соединения
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

con = create_connection("beautyfull.sqlite")



#print(Task1(con))
#print(Task2(con))
#print(Task3(con))
#print(Task4(con))
#print(Task5(con))
#print(Task6(con))
Task7(con)
#Task8(con)



def Create_Home():
    # Шаблон для главной страницы
    f_template = open('templates/Home_templ.html', 'r', encoding='utf-8-sig')
    html = f_template.read()
    f_template.close()
    # создаем объект-шаблон
    template = Template(html)
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/Home_templ.html')
    template.globals['len'] = len
    template.globals['print'] = print

    # генерируем результат на основе шаблона
    result_html = template.render(
        len=len
    )

    # создаем файл для HTML-страницы
    f = open('pages/Home.html', 'w', encoding='utf-8-sig')
    # выводим сгенерированную страницу в файл
    f.write(result_html)
    f.close()
