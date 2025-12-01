import requests
import time

while True:
    try:
        resposta = requests.get('http://servico-lista:5000/lista')
        dados = resposta.json()
        print(f"Dados recebidos: {dados}", flush=True)
    except:
        print("Tentando conectar", flush=True)
    time.sleep(5)