#!/usr/bin/python3

from urllib import request
import json
from asterisk.agi import *
import os
from func import *
#from func import *

agi = AGI()
agi.answer()

# SE DER ERRO ELE VAI FEECHAR SEM TE FALAR O QUE FOI, PQ ELE NOS ODEIA
# agi.appexec('Agi',f'googletts.agi,,"pt-BR"')

# Reproduz mensagem de boas-vindas
# NÃO PODE UTILIZAR , NO DO MEIOOOOO
agi.appexec('Agi',f'googletts.agi,Seja bem vindo a Voip Net em que posso ajuda-lo?,"pt-BR"')
agi.appexec('Agi',f'googletts.agi,Para contratar um novo plano digite um,"pt-BR"')
agi.appexec('Agi',f'googletts.agi,Para cancelar seu contrato digite dois,"pt-BR"')
agi.appexec('Agi',f'googletts.agi,Para reclamar com a nossa atendente a troco de nada digite 3,"pt-BR"')

# Aqui pegamos o que o usuário escolher

digito = agi.get_data('beep', timeout=10000, max_digits=1)
#implementar algum tipo de controle de erro, ou não, não sou seu pai

if digito == "1" :

    #while True :
    agi.appexec('Agi',f'googletts.agi,Digite seu CEP,"pt-BR"')
    cep = agi.get_data("beep", timeout=10000, max_digits=8)
    bairro = pegar_bairro_cep(cep)

elif digito == "2" :

    #se for possível, implementar para que passe para um atendente, se não, deixa assim mesmo
    agi.appexec('Agi',f'googletts.agi,Estaremos cancelando,"pt-BR"')
    agi.hangup()

elif digito == "3" :
    # para ser sincero essa opção só está aqui para encher linguiça

    agi.appexec('Agi',f'googletts.agi,Isso foi rude estarei desligando,"pt-BR"')
    agi.hangup()

agi.verbose(f"CEP: {cep} | Região: {bairro}")

plano = indicar_bairro_oferecer_plano(bairro)

if plano == "Não temos nenhum plano estaremo desligando tenha uma boa noite" :
    agi.hangup()

agi.appexec('Agi',f'googletts.agi,{plano},"pt-BR"')
agi.appexec('Agi',f'googletts.agi,gostaria de contratar?,"pt-BR"')
agi.appexec('Agi',f'googletts.agi,Se sim digite um,"pt-BR"')
agi.appexec('Agi',f'googletts.agi,Se não digite dois,"pt-BR"')

#parte final
digito = agi.get_data('beep', timeout=10000, max_digits=1)

if digito == "1" :
    agi.appexec('Agi',f'googletts.agi,Estaremos enviando uma equipe para {bairro},"pt-BR"')
    agi.hangup()
elif digito == "2" :
    agi.appexec('Agi',f'googletts.agi,tudo bem estaremos desligando tenha uma boa noite,"pt-BR"')
    agi.hangup()

agi.hangup()