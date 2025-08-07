#!/usr/bin/python3
import psycopg2
from asterisk.agi import *

con = psycopg2.connect(host='localhost', database='clientes', user='clientesuser', password='q1w2e3r4')
cur = con.cursor()

agi = AGI()
agi.answer()
idcliente = agi.get_data('clientes-principal',10000,5)

query="select situacao from lista where codigo='"+idcliente+"'"
cur.execute(query)

recset = cur.fetchone()
for rec in recset:
    if rec == 'pagador':
        agi.stream_file('clientes-emdia')
    elif rec == 'devedor':
        agi.stream_file('clientes-devendo')

agi.hangup()
con.close()
