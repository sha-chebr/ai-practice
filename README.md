# ai_practice — Local Data Engineering Playground

This repo contains a small end-to-end data engineering playground you can run locally using Docker.

Overview
- Data generator: `scripts/generate_data.py` creates CSVs for `customers`, `orders`, `products` in `data/`.
- ETL (PySpark): `scripts/etl_pyspark.py` reads the CSVs, joins them and writes an enriched table into Postgres via JDBC.
- Orchestration: Airflow DAG `dags/etl_dag.py` runs the generator then the ETL.
- Deployment: `docker-compose.yml` spins up Postgres and an Airflow container (which has PySpark installed).

High level steps
1. Grant Docker access when prompted.
2. Build and start containers: docker-compose up --build
3. Open Airflow UI at http://localhost:8080 (default credentials created by the stack: admin / admin)
4. Trigger the DAG `etl_pipeline` or wait for it to run.
5. Verify data in Postgres at localhost:5432 (user: `airflow`, pass: `airflow`, db: `airflow`).Thanks, appreciate the assurance

Notes
- All compute and DB components run in Docker — no local installs required besides Docker.
- The ETL uses PySpark (pyspark) and writes to Postgres using the official JDBC driver.

Files created
- `docker-compose.yml` — orchestrates Postgres and Airflow
- `docker/airflow/Dockerfile` — builds Airflow image with pyspark and JDBC driver
- `scripts/generate_data.py` — generates CSV files
- `scripts/etl_pyspark.py` — PySpark ETL job
- `dags/etl_dag.py` — Airflow DAG wiring the flow
- `.env.example` — environment variables template

If you want me to start the Docker containers now, please confirm (I will prompt for Docker access).
# ai-practice
