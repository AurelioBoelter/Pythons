import csv

with open('exemple.csv') as file:
    read = csv.reader(file, delimiter =',')
    print(read)
    for row in read:
        print(row)         
        
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

with open('ExcelImporta.csv') as file:
    read = csv.reader(file, delimiter =' ')
    print(read)
    for row in read:
        print(row)
tabem por linha
print(row[0], row[1], row[2]...etc)


-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

import pyodbc

con = pyodbc.connect('Driver={SQL Server};''Server=10.22.232.20;''Database=xxxx;''uid=usuario;pwd=xxxxx;')

c = con.cursor()

c.execute('select * from tabela')

for r in c:
    print('row = %r' %(r,))



-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

import pyodbc

con = pyodbc.connect('Driver={SQL Server};''Server=10.22.232.20;''Database=xxxx;''uid=usuario;pwd=xxxxx;')

c = con.cursor()

cmd_insert='insert into table values(?,?,?,?,?,?)'

var = [(Valores conforme colunas')]

for rec in var:
c.execute(cmd_insert,rec)
con.commit()


*****************************************

import pyodbc

con = pyodbc.connect('Driver={SQL Server};''Server=10.22.232.20;''Database=master;''uid=sa;pwd=!Q2w3e4r;')

cur= con.cursor()

cmd_create = 'create table xxxxx(id integer primary key, Nome varchar(50), Turno varchar(10))'

cur.execute(cmd_create)

con.commit()
