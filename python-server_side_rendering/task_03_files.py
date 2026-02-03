#!/usr/bin/env python3
import json
import csv
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
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

