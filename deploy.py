import requests
import json
import csv
import io
from flask import Flask
from flask_cors import CORS, cross_origin
from datetime import date,datetime, timedelta
import ftfy

app = Flask(__name__)

CORS(app, resources=r'/api/*', allow_headers='Content-Type')

#print('JSON:',json_data)

@app.route('/api/reports/cantones')
def index():
    x = datetime.now() - timedelta(days=1)
    mes = x.strftime("%m")
    dia = x.strftime("%d")
    url = f"http://geovision.uned.ac.cr/oges/archivos_covid/{mes}_{dia}/{mes}_{dia}_CSV.csv"
    try:
        csvResponse = requests.get(url)
    except Exception as err:
        return("<h1>Error ocurred while retrieving data</h1>", err)    
    reader = csv.DictReader(io.StringIO(csvResponse.text))    
    json_data = json.dumps(list(reader))    
    return json_data
    

@app.route('/')
def home():
    return '<h2>Welcome to Districts API</h1>'

if __name__ == '__main__':
    app.run(debug=True)