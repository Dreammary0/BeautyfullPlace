import pandas as pd
from app import app
from flask import render_template, request, session,Flask, redirect, url_for, flash, make_response
from utils import get_db_connection
from models.master_model import get_Master_records
@app.route('/masterdatepage', methods=['get'])
def masterdatepage():

     conn = get_db_connection()

     if request.values.get('masters'):
          masters_list_list=[]
          masters_list = request.values.getlist('masters')
          for elem in masters_list:
               df_Master_record=get_Master_records(conn, elem)
               masters_list_list.append(df_Master_record)
     else:
          masters_list=[]
          masters_list_list=[]
          df_Master_record=pd.DataFrame


     if masters_list:
          uniq_date_list=[]
          for elem in masters_list_list:
               df_Master_record_uniq_date=elem.Дата.unique()
               uniq_date_list.append(df_Master_record_uniq_date)
          html = render_template(
               'master_date_page.html',
               master_records_list=masters_list_list,
               len=len,
               int=int,
               uniq_date_list=uniq_date_list
               )
     return html

