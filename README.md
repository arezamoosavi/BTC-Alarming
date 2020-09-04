# Bitcoin-Alarm
This app is a scheduler such that every 10 sec get the bitcoin value in EUR and USD and save it to the database. The app is build with Faust, Kafka, Redis and PostgreSQL.

## Up
for running app:
```bash
docker-compose up --build -d
```
for stopping:
```bash
docker-compose down
```
## Tools
Tasks: Faust, Kafka, Redis


Data: Postgre, Asyncpg, Tortoise, Pydantic


Build: docker, docker-compose

## [Medium](https://medium.com/@sdamoosavi/real-time-bitcoin-notification-with-faust-f8fc32490fa5)
