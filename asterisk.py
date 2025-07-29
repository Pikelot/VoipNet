#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asterisk import AGI
from func import *

agi = AGI()
    
try:
    # Reproduz mensagem de boas-vindas
    agi.stream_file("bemvindo")
    
    # Captura os dígitos do CEP (8 dígitos)
    agi.stream_file("custom/digite-cep")
    cep_digits = agi.get_data("beep", timeout=10000, max_digits=8)
    
    # Formata o CEP e pega o bairro pelo mesmo rodando a função

    cep_formatado = f"{cep_digits[:5]}-{cep_digits[5:]}"
    
    bairro = pegar_bairro_cep(cep_formatado)
    
    # Log no console do Asterisk
    agi.verbose(f"CEP: {cep_formatado} | Região: {bairro}")

    # Aqui é para que ele retorne o plano após verificar o bairro, necessário verificar como -
    # vamos colocar o texto para voz
    
    plano = indicar_bairro_oferecer_plano(bairro)
        
    # Continua o fluxo de atendimento...
    
except Exception as e:
    agi.verbose(f"Erro: {str(e)}")
    agi.hangup()