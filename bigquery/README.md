# apache airflow template

# build docker image
docker build --tag pahennessey/airflow .

# use docker-compose to start orchestration first time
docker-compose up -d airflow_db && \
docker-compose run --rm airflow_webserver airflow initdb && \
docker-compose up -d

# use docker to start orchestration each additional time
docker-compose up -d

# connect to airflow webserver
localhost:1080

# connect to airflow postgres database
user: airflow
database: airflow
port: 5431