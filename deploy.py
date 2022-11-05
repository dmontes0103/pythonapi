from os import path
import requests
import json,csv,io
from test import csv_to_json
from flask import Flask
from flask_cors import CORS, cross_origin
from datetime import date,datetime, timedelta

app = Flask(__name__)

CORS(app, resources=r'/api/*', allow_headers='Content-Type')

#print('JSON:',json_data)

@app.route('/api/reports/cantones')
def index():
    x = datetime.now() - timedelta(days=1)
    mes = x.strftime("%m")
    dia = x.strftime("%d")
    #url = f"http://geovision.uned.ac.cr/oges/archivos_covid/{mes}_{dia}/{mes}_{dia}_CSV.csv"
    try:        
        data = csv_to_json('/data/dummydata.csv')
    except Exception as err:
        return str(err)
    return app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
    

@app.route('/')
def home():
    return '<h2>Welcome to Cantones API</h1>'

if __name__ == '__main__':
    app.run()