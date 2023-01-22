import pandas as pd
from app import app
from flask import render_template, request, session,Flask, redirect, url_for, flash, make_response
from utils import get_db_connection
from models.index_model import get_ProcedureList
import datetime

@app.route('/', methods=['get'])

def index():
     conn = get_db_connection()

     df_Service=get_ProcedureList(conn)
     html = render_template(
     'index.html',
     service= df_Service,
     len = len,
     )

     return html
