# Desafio 4 - Microsserviços Independentes

## Arquitetura
Arquitetura de microsserviços simples com dois componentes desacoplados:
* **Produtor (API)**: Serve dados em formato JSON.
* **Consumidor**: Script que acessa a API periodicamente para buscar informações.
Cada serviço possui seu próprio Dockerfile e contexto de execução.

## Tecnologias Utilizadas
* Docker (Build e Run manuais)
* Python (Flask para API, Requests para o consumidor)
* JSON

## Como Executar
É necessário criar a rede e subir cada serviço em terminais separados ou em sequência:

```bash
# 1. Criar rede
docker network create rede-servicos

# 2. Subir a API (Produtor)
cd servico_lista
docker build -t img-lista .
docker run -d --name servico-lista --network rede-servicos img-lista
cd ..

# 3. Subir o Consumidor
cd servico_consumidor
docker build -t img-leitor .
docker run --rm --network rede-servicos img-leitor
```

### O que faz
1. Prepara uma rede para comunicação interna.
2. O serviço de lista (API) sobe e fica aguardando conexões na porta 5000 interna.
3. O serviço consumidor inicia, conecta-se via HTTP no endereço http://servico-lista:5000/lista e imprime os dados recebidos no console.