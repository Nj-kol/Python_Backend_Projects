FROM python:3.7.1

LABEL Author="Nilanjan Sarkar"
LABEL E-mail="Nilanjan.Sarkar@gmail.com"
LABEL version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "product_api"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /flask_product_api
WORKDIR /flask_product_api

COPY . /flask_product_api/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /flask_product_api

EXPOSE 5000

CMD flask run --host=0.0.0.0