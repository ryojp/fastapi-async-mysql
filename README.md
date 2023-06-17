# [Demo] FastAPI with async MySQL

1. Start the environment
```sh
docker compose up --build --remove-orphans
```

2. Query
```sh
# insert db entries
curl localhost:8000/post

# fetch inserted entries
curl localhost:8000/list
```

3. Cleanup
```sh
# `-v` to delete the MySQL volume
docker compose down -v
```
