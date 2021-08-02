FROM python:alpine
RUN apk add --no-cache py3-pip
RUN pip install -r requirements.txt