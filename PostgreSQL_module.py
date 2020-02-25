# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:56:29 2019

@author: TroshinMV
"""

import postgresql
import random
import time

class DataBase:
    '''класс для работы с таблицами созданной ранее базой данных PostgreSQL:
        встроенные функции:
        - создание таблицы
        - запись данных в таблицу
        - удаление данных из таблицы
        - выгрузка данных по условию в виде таблицы
    '''
    
    def __init__(self, database_name):  
        self.db_tables = [] # множество вложенных таблиц
        try:
            self.db = postgresql.open(('pq://postgres:postgres@localhost/%s' %(str(database_name))))
        except Exception:
            self.db.close()
            self.db = None
            print('Database name in invalid')
            
        while True:
            time.sleep(2) # ждем 2 сек для открытия базы данных
            if self.db:
                table_names = self.db.query("SELECT tablename FROM (SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public') AS public_tables ") 
                if table_names:  # если переменная записалась, т.е. запрос нормально отработал
                    for names in table_names:    # в списке имен лежат кортежи из 1 значения
                        self.db_tables.append(str(names[0]))
                else:
                    raise NameError('Show tables query is invalid! Check the corresponding class function!')
                   
            else:
                raise NameError("DataBase didn't open properly")
                
    def Tables(self):
        return self.db_tables
            
    def CreateNewTable(self, table_name, Column_DataType_List):
        # пример передачи аргументов: ['id SERIAL PRIMARY KEY', 'login CHAR(64)', 'password CHAR(64)']
        columns = ','.join(Column_DataType_List)
        # список созданных таблиц
        self.db_tables.append(str(table_name))
        create_query = 'CREATE TABLE ' + str(table_name) + ' ({})'.format(columns)     
        try:
            self.db.execute(create_query)
        except Exception:
            self.db.close()
            print('You are stupid bitch!')
       
        
    def CheckTableName(self, table_name):
        # Проверка на существование требуемой таблицы в базе данных
        return True if table_name in self.db_tables else False
            
    
    def InsertValues(self, table_name, values_dict):
        # пример передачи аргументов: {'login': 'pipka', 'password': '12345'}
        # db.prepare('INSERT INTO users (login, password) VALUES ($1, $2)')
        # INSERT INTO customers (last_name) VALUES ('Fuck');
        if db.CheckTableName(table_name):
            for key in values_dict.keys():
                insert_query = 'INSERT INTO ' + str(table_name) + ' %s VALUES %s' %(str(key), str(values_dict[key]))
                try:
                    print(insert_query)
                    #self.db.execute(insert_query)
                except Exception:
                    self.db.close()
                    print('Insertion failed!')
        else:
            print('Table name argument in invalid!')
      
          
    def DeleteRows(self, table_name, rows):
        '''
        Function deletes selected rows fron selected table
        '''
        # 'DELETE FROM users WHERE users.id BETWEEN $1 AND $2'
            
            
    def CreateNewTable_1(self, table_name, RowPattern):
        # пример передачи аргументов: {'id':'SERIAL PRIMARY KEY', 'login':'CHAR(64)', 'password':'CHAR(64)'}
        self.RowDesc = [] # описание колонок в списке (ключи отсортированы)
        for key in sorted(RowPattern.keys()):   # работаем с отсортированным списком ключей
            column = (str(key) + ' ' + str(RowPattern[key]))
            self.RowDesc.append(column)
        rowdesc = ','.join(self.RowDesc)
        create_query = 'CREATE TABLE ' + str(table_name) + ' ({})'.format(rowdesc)
        try:
            self.db.execute(create_query)
        except Exception:
            self.db.close()
            print('Creating new table procedure failed!')
                     