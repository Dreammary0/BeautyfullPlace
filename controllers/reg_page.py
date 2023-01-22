import pandas as pd
from app import app
from flask import render_template, request, session,Flask, redirect, url_for, flash, make_response
from utils import get_db_connection
from models.reg_model import get_OrderListInfo_for_RegPage, get_check_sum, get_ClientId_for_chek, AddNewClient, RecordClient, AddCheck, AddCheck_Order, AddCheck_Procedure
@app.route('/regpage', methods=['get'])

def regpage():
     conn = get_db_connection()
     if request.values.get('record_button'):
          record_button_list=request.values.getlist('record_button')
          session['order_add']=record_button_list
          df_order_list_list=[]

          for proc in session['procedures']:
               df_order_list_list.append(get_OrderListInfo_for_RegPage(conn, record_button_list, proc))

          check_list=[]
          for serv in session['services']:
               if serv != '-':
                    for elem in serv:
                         check_list.append(elem)

          df_check_sum = get_check_sum(conn, check_list)
          session['check_sum']=df_check_sum
          session['service_list']=check_list

     else:
          record_button_list=[]


     if request.values.get('submitSuccess'):
         if (request.values.get('username') and request.values.get('userphone')):
              # Полуили айди клинта (если клиент новый - добавили в базу)
              IDClient = get_ClientId_for_chek(conn, request.values.get('username'), request.values.get('userphone'))
              # Записали его в окошко OrderList
              for elem in session['order_add']:
                   RecordClient(conn,IDClient,elem)

              # Создание записи для чека и двух смежных таблиц многие-ко-многим
              idCheck = AddCheck(conn,session['check_sum'],IDClient)
              for elem in session['order_add']:
                   AddCheck_Order(conn, idCheck, elem)
              for elem in session['service_list']:
                   AddCheck_Procedure(conn, idCheck, elem)

         html = render_template('success.html', name= request.values.get('username'), phone=request.values.get('userphone'))
         return html

     elif request.values.get('exit'):
          return redirect('/')

     html = render_template(
          'reg_page.html',
          procedure_list=session['procedures'],
          service_list = session['services'],
          record_button_list=session['order_add'],
          len=len,
          order_list = df_order_list_list,
          check_sum=df_check_sum
          )

     return html
