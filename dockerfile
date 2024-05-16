FROM python:latest

WORKDIR /projectclass

COPY . /projectclass

RUN pip install -r requirements.txt

CMD ["python", "server.py"]