#!/usr/bin/python3
from urllib import request
import json
from asterisk.agi import *

agi = AGI()
agi.answer()

cep = agi.get_data('digitecep',10000,8)

url = 'https://viacep.com.br/ws/'+str(cep)+'/json/'
html = request.urlopen(url)
info = json.loads(html.read())
nomerua = info['logradouro']

agi.stream_file('rua')
agi.appexec('Agi',f'googletts.agi,{nomerua},"pt-BR"')
agi.hangup()
