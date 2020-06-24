FROM python:latest

ADD ./app /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

EXPOSE 8080

ENTRYPOINT ["python","/app/server.py"]