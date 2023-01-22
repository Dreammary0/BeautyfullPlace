import pandas as pd
from app import app
from flask import render_template, request, session,Flask, redirect, url_for, flash, make_response
from utils import get_db_connection
from models.master_model import get_Masters_for_procedure
@app.route('/masterpage', methods=['get'])
def masterpage():

     session['services']=['-']
     conn = get_db_connection()
     add_procedure_list=[]
     if request.values.get('barber'):
          barber_list = request.values.getlist('barber')
          add_procedure_list.append('Парикмахер')
          session['services'].append(barber_list)
     else:
          barber_list = []


     if request.values.get('nail'):
          nail_list = request.values.getlist('nail')
          add_procedure_list.append('Маникюр')
          session['services'].append(nail_list)
     else:
          nail_list = []

     if request.values.get('makeup'):
          makeup_list = request.values.getlist('makeup')
          add_procedure_list.append('Визажист')
          session['services'].append(makeup_list)
     else:
          makeup_list = []


     if request.values.get('shugaring'):
          shugaring_list = request.values.getlist('shugaring')
          add_procedure_list.append('Шугаринг')
          session['services'].append(shugaring_list)
     else:
          shugaring_list = []

     if request.values.get('cosmetolog'):
          cosmetolog_list = request.values.getlist('cosmetolog')
          add_procedure_list.append('Косметолог')
          session['services'].append(cosmetolog_list)
     else:
          cosmetolog_list = []

     if add_procedure_list:
        df_Masters_for_procedure = get_Masters_for_procedure(conn, add_procedure_list)
        session['procedures']=add_procedure_list
        print(session['procedures'])
        print( session['services'])
     else:
          df_Masters_for_procedure = pd.DataFrame


     html = render_template(
          'master_page.html',
          len=len,
          masters=df_Masters_for_procedure,
          add_procedure_list=list(session['procedures']),
          add_service_list = list(session['services']),
     )


     return html
