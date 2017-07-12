"""
this file creates a json in a format that can be later fed to the db using $ python manage.py loaddata <modelname>

make sure the output looks like:
[
    {
	"model": "scsite.<modelname>",
	"pk": 1, (and incrementing)
	"fields":{
        "field1": "value1",
        "field2": "value1",
    }},
    {
    ....
    }
]
"""

import csv
import json
from sys import argv

script, model = argv

with open('%s.csv'%model, 'r') as csvfile:
    reader = csv.DictReader(csvfile) #DictReader makes dict keys of the first row.
    rows = list(reader)


with open('%s.json'%model, 'w') as jsonfile:
    feeds = []
    enumerator = 1
    for row in rows:
        feeds.append({"model": "scsite.%s"%model, "pk": enumerator, "fields": row})
        enumerator+=1
    json.dump(feeds, jsonfile,indent=4)