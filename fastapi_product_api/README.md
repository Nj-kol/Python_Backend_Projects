# Products CRUD API using Fast API

A simple demonstration of creating APIs using the FastAPI library

# Setup

## Create environment

* Create a virtual environment to run the applicaiton :

```bash
conda create -n web_dev python=3.6
conda activate web_dev
```

* Checkout the project from git, and install the dependencies

```bash
pip install -r requirments.txt
```

* Under the root folder create a file called `.env` and add the following lines :

```bash
PROJECT_NAME=product_api_fastapi
BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost"]

DATABASE_URI = 'mysql+pymysql://<db_user>:<db_pass>@<hostname>:<port>/<db_name>'
```

## DB Set up

* Create a table :

```sql
CREATE TABLE product (
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(100),
	description VARCHAR(200),
	price FLOAT,
	qty INTEGER,
	PRIMARY KEY (id),
	UNIQUE (name)
);
```

* Insert some dummy records for testing

## Run the app

```bash
cd fastapi_product_api
fastapi run
```

# Generated Open API docs

* The Open API docgenerated can be viewed at :

http://127.0.0.1:8000/docs

* Also, an alternate form of API documentation is generated

http://127.0.0.1:8000/redoc

# Endpoints

curl http://127.0.0.1:8000/product | jq

**Sample response**

```json
[
  {
    "description": "Biscuit",
    "qty": 1,
    "price": 10,
    "name": "Good Day ",
    "id": 1
  },
  {
    "description": "Shampoo",
    "qty": 1,
    "price": 76,
    "name": "Clinic Plus ",
    "id": 2
  },
  {
    "description": "Coke",
    "qty": 1,
    "price": 20,
    "name": "Coca Cola Classic",
    "id": 3
  }
]
```
# Testing

## Run tests

* Testing is accomplished using `pytest` and automated using `tox`.
* To run using only `pytest` , use  `pytest -s -v`
* Alternatively, you can run tests with `tox`

## Code coverage reports

* If you run, the tests with `tox`, code coverage is gathered automatically using `coverage`
* To see the reports : `coverage report -m`
* To generate html reports :  `coverage html`
* Alternatively, you can use `coverage run -m pytest -s -v`, to gather coverage data, if you are not using `tox`

# Committing Code

* It's usually a good idea to run the hooks against all of the files when adding new hooks
  (usually `pre-commit` will only run on the changed files during git hooks)

```bash
pre-commit run --all-files
```

# Deployment

## Deploy on Docker

```bash
# Build docker image
docker build -t fastapi_product_api .

# Launch a container
docker run -p 8000:8000 -d \
--name my_container_fastapi \
fastapi_product_api

# Housekeeping
docker logs my_container_fastapi
docker exec -it my_container_fastapi bash

# Teardown
docker container stop my_container_fastapi
docker container rm my_container_fastapi
docker image rm fastapi_product_api
```

## Deploy on Kubernetes

* Deploy all artifacts :

```bash
kubectl apply -f deploy/
```

* Check

http://127.0.0.1:30274/docs

```bash
# Housekeeping
kubectl get po -o wide
kubectl logs fastapi-product-api-59857c865c-lqxzr -f
kubectl exec -it fastapi-product-api-59857c865c-9g2j2 bash
kubectl get deploy
kubectl get svc
```

* Shutdown

```bash
# Teardown
kubectl delete -f deploy/
````
