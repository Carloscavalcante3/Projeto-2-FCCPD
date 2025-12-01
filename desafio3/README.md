# Desafio 3 - Orquestração com Docker Compose

## Arquitetura
Uma aplicação web composta por três serviços que dependem uns dos outros:
1. **Pagina**: Aplicação Python/Flask que exibe um contador.
2. **Cache**: Banco Redis para armazenar o número de visitas.
3. **Administrador**: Interface gráfica (Adminer) para gestão de dados.
Todos rodam em uma rede interna criada automaticamente pelo Compose.

## Tecnologias Utilizadas
* Docker Compose
* Python (Flask)
* Redis
* Adminer

## Como Executar
Certifique-se de estar dentro da pasta do desafio e execute:

```bash
docker-compose up
```

### O que faz
1. Lê o arquivo docker-compose.yml.
2. Baixa as imagens do Redis e do Adminer e constrói a imagem da aplicação Python local.
3. Inicia os serviços na ordem correta (o Python espera o Redis estar pronto).
4. Libera a porta 5000 para acesso no navegador (localhost:5000), onde é possível ver o contador de visitas aumentando.