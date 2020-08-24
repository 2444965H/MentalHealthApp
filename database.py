from tinydb import TinyDB, Query

#Create path
db = TinyDB('/path/to/db.json')

#Create Table
table = db.table('MentalProfile')
table.insert({'value': True})
table.all()
[{'value': True}]