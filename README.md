# Projeto - Docker e Arquitetura de Microsserviços

## Visão Geral
Este repositório contém a solução completa para os 5 desafios práticos de Docker e Microsserviços. O objetivo foi demonstrar domínio sobre criação de containers, redes, persistência de dados, orquestração com Docker Compose e padrões de arquitetura como API Gateway.

Cada desafio foi isolado em sua própria pasta contendo seus respectivos `Dockerfiles`, scripts e instruções específicas.

## Estrutura do Projeto

| Pasta | Tema | Descrição Resumida |
| :--- | :--- | :--- |
| **/desafio1** | **Containers em Rede** | Comunicação entre um servidor Python e um cliente via *bridge network* customizada. |
| **/desafio2** | **Persistência de Dados** | Banco de dados PostgreSQL com volumes para garantir que dados sobrevivam à remoção do container. |
| **/desafio3** | **Orquestração (Compose)** | Aplicação Web + Redis + Adminer rodando integrados via Docker Compose. |
| **/desafio4** | **Microsserviços** | Dois serviços independentes (Produtor/Consumidor) conversando via HTTP/JSON. |
| **/desafio5** | **API Gateway** | Implementação de um Gateway Nginx centralizando o acesso a dois microsserviços distintos. |

## Resultados Esperados
Abaixo descrevo o que deve ser observado ao executar cada desafio para validar o funcionamento:

### Desafio 1: Rede Customizada
* **Resultado:** Ao rodar os scripts, o terminal do cliente deve exibir repetidamente a mensagem de resposta do servidor (ex: "Ola sou o servidor..."), provando que a resolução de nomes via DNS do Docker funcionou na rede isolada.

### Desafio 2: Volumes e Persistência
* **Resultado:** O script insere um dado, deleta o container e sobe um novo. O teste final deve mostrar o registro `"Dado importante salvo"` sendo recuperado com sucesso, provando que o volume funcionou.

### Desafio 3: Docker Compose
* **Resultado:** Ao acessar `localhost:5000`, a página deve mostrar um contador de visitas. Ao recarregar a página, o número deve aumentar (1, 2, 3...), indicando que o Python está conseguindo escrever e ler no Redis corretamente.

### Desafio 4: Comunicação HTTP
* **Resultado:** O container "consumidor" deve imprimir no log os dados JSON recebidos do container "lista" (ex: `Recebi os dados: {'nomes': ['Carlos', ...]}`), confirmando a integração via API REST.

### Desafio 5: API Gateway
* **Resultado:**
    * Acessar `localhost:8080/users` -> Retorna dados do serviço de Usuários.
    * Acessar `localhost:8080/orders` -> Retorna dados do serviço de Pedidos.
    * Isso confirma que o Nginx está roteando as chamadas corretamente para os containers internos.

## Tecnologias e Decisões
Optei por utilizar **Python** na maioria das soluções pela simplicidade de criar servidores HTTP sem necessidade de *frameworks* pesados, facilitando a visualização da lógica de arquitetura.
Para o banco de dados, utilizei **PostgreSQL** e para o Gateway o **Nginx**, seguindo padrões de mercado.

## Como Executar
Navegue até a pasta do desafio desejado e siga as instruções do arquivo `README.md` local.