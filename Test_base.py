# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:40:50 2020

@author: TroshinMV
"""

import PostgreSQL_module.py as psql

db.InsertValues('customers', {'first_Name': 'Kevin', 'last_Name': 'Smith'})    
        
show_tables_in = db.prepare('SELECT * FROM pg_catalog.pg_tables WHERE schemaname = $1')
table_names = show_tables_in('public')
table_names1 = db.query("SELECT tablename FROM (SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public') AS public_tables ")
table_names1


        
db = DbTable('postgres')
db.ShowTables()
db.CreateNewTable('customers', ['id SERIAL PRIMARY KEY', 'First_Name CHAR(64)', 'Last_Name CHAR(64)'])
db.CreateNewTable_1('Orders', {'customer_id':'SMALLINT', 'goods':'CHAR(64)', 'price':'SMALLINT'})
FirstNames = ['John', 'Jack', 'Sam', 'Ludvig', 'Harry', 'Kevin', 'Henry', 'Steve', 'Peter', 'Avraam']
LastNames = ['Black', 'Smith', 'Pork', 'Beetle', 'Potter', 'Klint', 'Good', 'Petek', 'Hitler' ,'Shervood']
try: 
    for FN in FirstNames:
        for LN in LastNames:
            db.InsertValues('customers', {'First_Name': FN, 'Last_Name': LN})
except Exception:
    db.close()
    print('That doesn''t work!')
            
print(" 'public' ")


db = postgresql.open('pq://postgres:postgres@localhost/postgres')
db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, login CHAR(64), password CHAR(64))")

#работает
delete = db.prepare('DELETE FROM users WHERE users.id BETWEEN $1 AND $2')
ins = db.prepare('INSERT INTO users (login, password) VALUES ($1, $2)')
updatepass = db.prepare("UPDATE users SET password = $2 WHERE login = $1")

ins('Mihulich', '1234567')
ins('Popka', '74638')

db.query('SELECT id, trim(login), trim(password) FROM users')
user2 = db.query('SELECT * FROM users WHERE id = 2')
user2[0]
user2[0]['password']
user2[0]['login'].strip()

with db.xact() as xact:
    xact.rollback()


updatepass('Mihulich', 'Nika')
delete(3, 10)

db.close()

with db.xact() as xact:
    db.query('SELECT id FROM users')
    
with db.xact() as xact:
    db.query("SELECT id FROM users")
    xact.rollback()
    
ver = db.proc('version()')
ver()

alphabet = 'abcdefghigklmnopqrstuvwxyz'
for i in range(10):
    name = ''
    for k in range(3):
        name += alphabet[random.randint(0, len(alphabet)-1)]
    ins(name, str(random.randint(1000, 9999)))

    