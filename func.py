import requests
import sys

def pegar_bairro_cep(cep):

    if not cep or not cep.isdigit() or len(cep) != 8:
        return None

    try:
        
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=5) # Timeout de 5 segundos

        if response.status_code == 200:
            data = response.json()

            if 'erro' in data:
                return None
            return data.get('bairro') # Pega o valor da chave 'bairro'
        else:
            return None
    except requests.RequestException:

        return None

def indicar_bairro_oferecer_plano(bairro):
        
    if bairro == "Nossa Senhora da Apresentação":
        return ("Temos o plano de 100 gigas")

    elif bairro == "Planalto":
        return ("Temos o plano de 50 gigas")

    elif bairro == "Alecrim":
        return ("Temos o plano 25 gigas")
    
    elif bairro == "Lagoa Azul":
        return ("Temos o plano 300 gigas")
    
    else :
        return ("Não temos nenhum plano estaremo desligando tenha uma boa noite")