# Desafio 5 - API Gateway

## Arquitetura
Implementação do padrão API Gateway. Um servidor Nginx atua como porta de entrada única, recebendo todas as requisições externas e roteando para os microsserviços internos (Usuários ou Pedidos) dependendo da URL acessada.

## Tecnologias Utilizadas
* Docker Compose
* Nginx (Proxy Reverso)
* Python (Flask)

## Como Executar
Execute o orquestrador na pasta do desafio:

```bash
docker-compose up
```
### O que faz
1. Sobe dois microsserviços simples (Usuários e Pedidos) que não são acessíveis diretamente pelo mundo externo.
2. Sobe o container do Nginx configurado com as regras de roteamento.
3. Ao acessar localhost:8080/users, o Nginx busca os dados no container de usuários.
4. Ao acessar localhost:8080/orders, o Nginx busca os dados no container de pedidos.