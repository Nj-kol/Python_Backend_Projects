
# Flask REStful API demo

## Set up python Environment

```bash
pipenv install
pipenv shell
```

## DB Set up

```
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

## Running the application

```
cd flask_product_api
export FLASK_APP=product_api
export FLASK_ENV=development
flask run
```

## URLs

```
POST http://127.0.0.1:5000/product
GET http://127.0.0.1:5000/product
PUT http://127.0.0.1:5000/product/<product_id>
DELETE http://127.0.0.1:5000/product/<product_id>
```

**Swagger UI**

http://127.0.0.1:5000/apidocs/index.html 

# Docker 

```
// Build docker image
docker build -t flask_product_api .

// Launch a container
docker run -p 5000:5000 -d \
--name my_container_flask \
flask_product_api

// Housekeeping
docker logs my_container_flask -f
docker exec -it my_container_flask bash

// Teardown
docker container stop my_container_flask
docker container rm my_container_flask
docker image rm flask_product_api
```

# Deploy to Kubernetes

```
kubectl apply -f deploy/

// Use
http://127.0.0.1:30274/apidocs/index.html 

// Housekeeping
kubectl get po -o wide
kubectl logs flask-product-api-59857c865c-lqxzr -f
kubectl exec -it flask-product-api-59857c865c-9g2j2 bash
kubectl get deploy
kubectl get svc

// Teardown
kubectl delete -f deploy/
````

References
==========

**Swagger**

https://github.com/flasgger/flasgger/blob/master/examples/apispec_example.py ( Imp )

https://swagger.io/docs/specification/2-0/describing-request-body/

https://swagger.io/docs/specification/describing-request-body/ ( v3 )

http://brunorocha.org/python/flask/flasgger-api-playground-with-flask-and-swagger-ui.html

**Docker**

https://dev.to/riverfount/dockerize-a-flask-app-17ag

