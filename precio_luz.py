#!/usr/bin/env python3

"""
https://es.wikipedia.org/wiki/Precio_voluntario_para_el_peque%C3%B1o_consumidor
https://api.esios.ree.es/
"""

import json
import requests
import os

from datetime import datetime

# You need to request a token from api.esios.ree.es
TOKEN = os.getenv("ESIOS_TOKEN")

# peninsula
geoid = 8741 
# electricity price
code=1001

url = f"https://api.esios.ree.es/indicators/{code}"
headers = {'Accept':'application/json; application/vnd.esios-api-v2+json',
           'Content-Type':'application/json',
           'Host':'api.esios.ree.es',
           'Authorization':'Token token=' + TOKEN}

response = requests.get(url, headers=headers)

if response.status_code == 200:

  json_data = json.loads(response.text)
  valores = json_data['indicator']['values']
  precios = [x for x in valores if x['geo_id'] == geoid ]

  for precio in precios:
      date_time = datetime.strptime(precio['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
      human_date = date_time.strftime("%m/%d/%Y, %H:%M:%S")
      print(f"{human_date}: {precio['value']}")
else:
    print(f"ERROR leyendo datos: {response.status_code}")

