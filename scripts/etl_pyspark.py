"""PySpark ETL job: read CSVs, join and write to Postgres via JDBC."""
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr


DATA_DIR = '/opt/airflow/data'


def get_spark(jars_path='/opt/java_jars/postgresql.jar'):
    spark = SparkSession.builder \
        .appName('etl_job') \
        .config('spark.jars', jars_path) \
        .getOrCreate()
    return spark


def run():
    spark = get_spark()

    customers = spark.read.option('header', True).csv(os.path.join(DATA_DIR, 'customers.csv'))
    products = spark.read.option('header', True).csv(os.path.join(DATA_DIR, 'products.csv'))
    orders = spark.read.option('header', True).csv(os.path.join(DATA_DIR, 'orders.csv'))

    # Cast numeric columns
    products = products.withColumn('price', col('price').cast('double'))
    orders = orders.withColumn('quantity', col('quantity').cast('int'))
    orders = orders.withColumn('order_id', col('order_id').cast('int'))
    orders = orders.withColumn('product_id', col('product_id').cast('int'))
    orders = orders.withColumn('customer_id', col('customer_id').cast('int'))

    # Simple join and compute total
    joined = orders.join(customers, 'customer_id', 'left') \
        .join(products, 'product_id', 'left') \
        .withColumn('total', col('quantity') * col('price'))

    # Write to Postgres using JDBC
    pg_url = os.environ.get('POSTGRES_URL', 'jdbc:postgresql://postgres:5432/airflow')
    pg_props = {
        'user': os.environ.get('POSTGRES_USER', 'airflow'),
        'password': os.environ.get('POSTGRES_PASSWORD', 'airflow'),
        'driver': 'org.postgresql.Driver'
    }

    joined.select('order_id', 'order_date', 'customer_id', 'name', 'product_id', 'quantity', 'price', 'total') \
        .write.jdbc(url=pg_url, table='public.orders_enriched', mode='overwrite', properties=pg_props)

    spark.stop()


if __name__ == '__main__':
    run()
