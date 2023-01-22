import pandas as pd
from app import app
from flask import render_template, request, session, Flask, redirect, url_for, flash, make_response
from utils import get_db_connection
from models.master_model import get_Find_time_date, get_Masters_for_procedure

def convert(date):
    return max(i for i in date.replace('-', '.').split())

@app.route('/datepage', methods=['get'])
def datepage():
    conn = get_db_connection()
    add_procedure_list = []
    if request.values.get('barber'):
        barber_list = request.values.getlist('barber')
        add_procedure_list.append('Парикмахер')
    else:
        barber_list = []

    if request.values.get('nail'):
        nail_list = request.values.getlist('nail')
        add_procedure_list.append('Маникюр')
    else:
        nail_list = []

    if request.values.get('makeup'):
        makeup_list = request.values.getlist('makeup')
        add_procedure_list.append('Визажист')
    else:
        makeup_list = []

    if request.values.get('shugaring'):
        shugaring_list = request.values.getlist('shugaring')
        add_procedure_list.append('Шугаринг')
    else:
        shugaring_list = []

    if request.values.get('cosmetolog'):
        cosmetolog_list = request.values.getlist('cosmetolog')
        add_procedure_list.append('Косметолог')
    else:
        cosmetolog_list = []

    if add_procedure_list:
        session['procedures'] = add_procedure_list
        df_Masters_for_procedure = get_Masters_for_procedure(conn, session['procedures'])
    elif session['procedures']:
        df_Masters_for_procedure = get_Masters_for_procedure(conn, session['procedures'])
    else:
        df_Masters_for_procedure = pd.DataFrame

    date_list_list=[]
    uniq_date_list = []
    master_list = list(df_Masters_for_procedure['MasterName'])
    date_list_df = pd.DataFrame
    indecator = 0
    if request.values.get('submitGetDate'):
        startDate = request.values.get('dateStart')
        endDate = request.values.get('dateEnd')
        startDate = convert(startDate)
        endDate = convert(endDate)
        for elem in master_list:
            date_list_df = get_Find_time_date(conn, startDate, endDate, elem)
            print(date_list_df)
            isempty = date_list_df.empty
            print(isempty)
            if (isempty): print('пусто')
            else:
                date_list_list.append(date_list_df)
        indecator=1

    if date_list_list:
        for elem in date_list_list:
            df_Date_record_uniq_date = elem.Дата.unique()
            uniq_date_list.append(df_Date_record_uniq_date)


    html = render_template(
        'date_page.html',
        date_list_list=date_list_list,
        int=int,
        uniq_date_list=uniq_date_list,
        len=len,
        indecator=indecator,
    )
    return html
