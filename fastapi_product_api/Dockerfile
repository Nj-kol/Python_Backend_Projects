FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

LABEL Author="Nilanjan Sarkar"
LABEL E-mail="Nilanjan.Sarkar@gmail.com"
LABEL version="0.0.1"

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

RUN mkdir /fastapi_product_api
WORKDIR /fastapi_product_api

COPY . /fastapi_product_api/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /flask_product_api

EXPOSE 8000

CMD uvicorn app.main:app --host=0.0.0.0
