#!/usr/bin/python3
from asterisk.agi import *

agi = AGI()

agi.answer()
result = agi.get_data('principal',5000,1)
if result == '1':
    musica = agi.get_data('lista-musicas',5000,1)
    if musica == '1':    
        agi.stream_file('instrumental')
    elif musica == '2':
        agi.stream_file('sultans')
    else:
        agi.stream_file('opcao-invalida')
elif result == '3':
    agi.appexec('Dial','SIP/10009191')
else:
    agi.stream_file('opcao-invalida')
agi.hangup()
