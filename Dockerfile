FROM python:3.12.9-bullseye
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt
COPY . .
