import time
import redis
from flask import Flask

aplicacao = Flask(__name__)
bancoMemoria = redis.Redis(host='cache', port=6379)

def contarAcessos():
    tentativas = 5
    while True:
        try:
            return bancoMemoria.incr('acessos')
        except redis.exceptions.ConnectionError as erro:
            if tentativas == 0:
                raise erro
            tentativas -= 1
            time.sleep(0.5)

@aplicacao.route('/')
def inicio():
    numero = contarAcessos()
    return 'Essa pagina foi vista {} vezes.\n'.format(numero)