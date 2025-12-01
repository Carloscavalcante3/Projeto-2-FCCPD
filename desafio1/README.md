# Desafio 1 - Containers em Rede

## Arquitetura
A arquitetura consiste em dois containers isolados conectados por uma *bridge network* (rede ponte) customizada. O primeiro container atua como servidor web e o segundo como cliente, provando que é possível comunicação direta entre containers usando seus nomes como endereço.

## Tecnologias Utilizadas
* Docker (Redes e Containers)
* Python (Biblioteca http.server)
* Linux (Imagem base Alpine/Slim)
* Curl (Para testes de requisição)

## Como Executar
Abra o terminal na pasta do desafio e rode os comandos abaixo sequencialmente:

```bash
docker network create rede-desafio1

docker build -t imagem-servidor .

docker run -d --name container-servidor --network rede-desafio1 imagem-servidor

docker run --rm --name container-cliente --network rede-desafio1 curlimages/curl:latest sh -c "while true; do curl http://container-servidor:8080; sleep 5; done"
```
### O que faz
1. Cria uma rede privada do Docker chamada rede-desafio1.
2. Constrói a imagem do servidor Python.
3. Sobe o container do servidor conectado nessa rede.
4. Sobe um segundo container (cliente) que entra num loop infinito enviando requisições para o servidor a cada 5 segundos, exibindo a resposta no terminal.