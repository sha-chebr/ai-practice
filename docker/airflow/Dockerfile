FROM apache/airflow:2.8.4-python3.11

# Use root for system-level package installs; keep layers small and reproducible
USER root

# Non-interactive apt and install minimal utilities, then install pinned Python packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    default-jdk \
    procps && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64

# Download Postgres JDBC driver for Spark JDBC writes (pin version via ARG)
ARG POSTGRES_JDBC_VERSION=42.6.0
RUN mkdir -p /opt/java_jars && \
  curl -fsSL "https://jdbc.postgresql.org/download/postgresql-${POSTGRES_JDBC_VERSION}.jar" -o /opt/java_jars/postgresql.jar

# Switch to airflow user and install Python packages into the user's local site-packages
USER airflow
ENV PATH=/home/airflow/.local/bin:${PATH}
RUN python -m pip install --user --upgrade pip setuptools wheel && \
  python -m pip install --user --no-warn-script-location \
    pyspark==3.4.1 \
    psycopg2-binary==2.9.6

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
