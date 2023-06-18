# [Demo] FastAPI with async MySQL

To demonstrate `async` is useful, we use Istio's fault injection so that network access to MySQL has delay.

Therefore, we use Kubernetes for demo.

## Kubernetes

1. Copy and create `k8s/.env`
```sh
cp k8s/.env.example k8s/.env
vi k8s/.env  # set secure passwords
```

2. Deploy our app along with Istio
```sh
kubectl apply -k k8s/
```


## Docker-Compose

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
