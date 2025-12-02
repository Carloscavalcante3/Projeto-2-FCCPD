# Desafio 2 - Persistência de Dados

## Arquitetura
O sistema utiliza um container de banco de dados PostgreSQL. Para garantir que os dados não sejam perdidos quando o container for desligado ou removido, foi configurado um Volume Docker externo mapeado para a pasta de dados do banco.

## Tecnologias Utilizadas
* Docker Volumes
* PostgreSQL 15
* Scripts Shell (Bash)

## Como Executar
Você pode rodar o script de teste incluído (`bancoDados_desafio.sh`) ou digitar os comandos abaixo manualmente:

```bash
docker volume create volume-meu-banco

docker run -d --name banco-teste -e POSTGRES_PASSWORD=senha123 -v volume-meu-banco:/var/lib/postgresql/data postgres:15

docker exec -it banco-teste psql -U postgres -c "CREATE TABLE informacoes (id serial, texto text);"
docker exec -it banco-teste psql -U postgres -c "INSERT INTO informacoes (texto) VALUES ('Dado importante salvo');"

docker rm -f banco-teste

docker run -d --name banco-recuperado -e POSTGRES_PASSWORD=senha123 -v volume-meu-banco:/var/lib/postgresql/data postgres:15

docker exec -it banco-recuperado psql -U postgres -c "SELECT * FROM informacoes;"
```
### O que faz
1. Cria um volume persistente.
2. Inicia um banco de dados ligado a esse volume.
3. Cria uma tabela e salva um dado nela.
4. Deleta o container do banco de dados (simulando uma falha ou atualização).
5. Cria um novo container ligado ao mesmo volume.
6.  Consulta o banco para provar que o dado inserido no passo 3 continua lá.