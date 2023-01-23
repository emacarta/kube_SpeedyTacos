FROM postgres:latest

ENV POSTGRES_DB ORDINI_database
ENV POSTGRES_USER SQLuser
ENV POSTGRES_PASSWORD 1234

COPY db_script.sql /docker-entrypoint-initdb.d/
