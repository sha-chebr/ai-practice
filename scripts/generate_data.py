#!/usr/bin/env python3
"""Generate sample CSV data for customers, products and orders."""
import csv
import os
import random
import uuid
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def ensure_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def gen_customers(n=100):
    rows = []
    for i in range(1, n + 1):
        rows.append({'customer_id': i, 'name': f'Customer {i}', 'email': f'customer{i}@example.com'})
    return rows


def gen_products(n=30):
    rows = []
    for i in range(1, n + 1):
        rows.append({'product_id': i, 'name': f'Product {i}', 'price': round(random.uniform(5, 500), 2)})
    return rows


def gen_orders(n=200, customer_count=100, product_count=30):
    rows = []
    start = datetime.now() - timedelta(days=365)
    for i in range(1, n + 1):
        cust = random.randint(1, customer_count)
        prod = random.randint(1, product_count)
        qty = random.randint(1, 5)
        order_date = start + timedelta(days=random.randint(0, 365))
        rows.append({'order_id': i, 'customer_id': cust, 'product_id': prod, 'quantity': qty, 'order_date': order_date.strftime('%Y-%m-%d')})
    return rows


def write_csv(path, rows, fieldnames):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    ensure_dir()
    customers = gen_customers(100)
    products = gen_products(30)
    orders = gen_orders(200, customer_count=100, product_count=30)

    write_csv(os.path.join(DATA_DIR, 'customers.csv'), customers, ['customer_id', 'name', 'email'])
    write_csv(os.path.join(DATA_DIR, 'products.csv'), products, ['product_id', 'name', 'price'])
    write_csv(os.path.join(DATA_DIR, 'orders.csv'), orders, ['order_id', 'customer_id', 'product_id', 'quantity', 'order_date'])


if __name__ == '__main__':
    main()
