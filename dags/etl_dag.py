from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
}

with DAG('etl_pipeline', schedule_interval='@once', default_args=default_args, catchup=False) as dag:
    gen = BashOperator(
        task_id='generate_data',
        bash_command='python /opt/airflow/scripts/generate_data.py'
    )

    etl = BashOperator(
        task_id='run_etl',
        bash_command='python /opt/airflow/scripts/etl_pyspark.py'
    )

    gen >> etl
