import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from datetime import datetime
import StringIO
import csv
import requests
from app import db
import config
from app.models import Day


url = "https://docs.google.com/spreadsheet/ccc?key=%s&output=csv" % config.GSHEET_KEY
response = requests.get(url)

f = StringIO.StringIO(response.content)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print row

