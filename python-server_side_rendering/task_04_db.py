#!/usr/bin/env python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv_file():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

def read_sqlite_db():
    products = []
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })

    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    try:
        if source == 'json':
            data = read_json_file()
        elif source == 'csv':
            data = read_csv_file()
        elif source == 'sql':
            data = read_sqlite_db()
        else:
            error = "Wrong source"
            return render_template('product_display.html', error=error)

        if product_id:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
            if not data:
                error = "Product not found"

    except Exception:
        error = "Database error"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

