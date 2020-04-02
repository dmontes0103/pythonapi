import requests
import json
import csv
import io
from flask import Flask

app = Flask(__name__)

#print('JSON:',json_data)

@app.route('/api/reports/districts')
def index():
    csvResponse = requests.get("http://geovision.uned.ac.cr/oges/archivos_covid/03_30/03_30_CSV.csv")
    print(csvResponse.text)    
    reader = csv.DictReader(io.StringIO(csvResponse.text))
    json_data = json.dumps(list(reader))
    return json_data
