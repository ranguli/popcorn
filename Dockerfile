FROM python:alpine3.7
MAINTAINER Joshua Murphy "hello@joshmurphy.ca"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000 

CMD ["python", "app.py"]
