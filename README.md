# ai_practice — Local Data Engineering Playground

This repo contains a small end-to-end data engineering playground you can run locally using Docker.

## Service Ports (Non-Default)

| Service | Port | Default Port | Description |
|---------|------|--------------|-------------|
| Airflow Webserver | 9090 | 8080 | Airflow UI interface |
| PostgreSQL | 5433 | 5432 | Database service |

## Overview
- Data generator: `scripts/generate_data.py` creates CSVs for `customers`, `orders`, `products` in `data/`.
- ETL (PySpark): `scripts/etl_pyspark.py` reads the CSVs, joins them and writes an enriched table into Postgres via JDBC.
- Orchestration: Airflow DAG `dags/etl_dag.py` runs the generator then the ETL.
- Deployment: `docker-compose.yml` spins up Postgres and Airflow services (which has PySpark installed).

## High Level Steps
1. Grant Docker access when prompted.
2. Build and start containers:
```bash
docker compose up --build
```
3. Open Airflow UI at http://localhost:9090 (credentials: admin / admin)
4. Trigger the DAG `etl_pipeline` or wait for it to run.
5. Verify data in Postgres at localhost:5433 (user: `airflow`, pass: `airflow`, db: `airflow`)

## Notes
- All compute and DB components run in Docker — no local installs required besides Docker.
- The ETL uses PySpark (pyspark) and writes to Postgres using the official JDBC driver.
- Non-default ports are used to avoid conflicts with existing services.

## Project Structure
- `docker-compose.yml` — orchestrates Postgres and Airflow
- `docker/airflow/Dockerfile` — builds Airflow image with pyspark and JDBC driver
- `scripts/generate_data.py` — generates CSV files
- `scripts/etl_pyspark.py` — PySpark ETL job
- `dags/etl_dag.py` — Airflow DAG wiring the flow
- `.env.example` — environment variables template

## Database Connection
To connect to PostgreSQL directly:
```bash
# Using psql
psql -h localhost -p 5433 -U airflow -d airflow

# Using connection string
postgresql://airflow:airflow@localhost:5433/airflow
```
