FROM apache/airflow:2.8.3-python3.10

# Install pyspark and psycopg2-binary
USER root
RUN pip install --no-cache-dir pyspark psycopg2-binary sqlalchemy

# Download Postgres JDBC driver for Spark JDBC writes
RUN mkdir -p /opt/java_jars && \
    curl -L --silent -o /opt/java_jars/postgresql.jar \
      https://jdbc.postgresql.org/download/postgresql-42.6.0.jar

USER airflow

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
