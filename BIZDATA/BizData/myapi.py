import json
import requests
import MySQLdb
from collections import ChainMap

r = requests.get('http://127.0.0.1:8000/show/?format=json')
json_data = json.loads(r.text)

mydict = {}
for i in json_data:
    mydict.update(i)


# mydict = ChainMap(*json_data)



db = MySQLdb.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='bizdata',
                     port=3307
                     )

placeholders = ', '.join(['%s'] * len(mydict))
columns = ', '.join(mydict.keys())
sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('mytable', columns, placeholders)
cursor = db.cursor()
cursor.execute(sql, list(mydict.values()))
db.commit()
