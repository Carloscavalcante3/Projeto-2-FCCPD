docker volume create volume-meu-banco

docker run -d --name banco-teste -e POSTGRES_PASSWORD=senha123 -v volume-meu-banco:/var/lib/postgresql/data postgres

docker exec -it banco-teste psql -U postgres -c "CREATE TABLE informacoes (id serial, texto text);"
docker exec -it banco-teste psql -U postgres -c "INSERT INTO informacoes (texto) VALUES ('Dado importante salvo');"

docker rm -f banco-teste

docker run -d --name banco-recuperado -e POSTGRES_PASSWORD=senha123 -v volume-meu-banco:/var/lib/postgresql/data postgres

docker exec -it banco-recuperado psql -U postgres -c "SELECT * FROM informacoes;"