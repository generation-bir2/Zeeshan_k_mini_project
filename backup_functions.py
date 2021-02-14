import pymysql
from dotenv import load_dotenv
import os

host='localhost'
user='root'
password='password'
database='db'

def save_data(couriers, products):
    with open('load_couriers.txt', 'w') as courier_txt:
        for row in couriers:
            courier_txt.write(str(row) + '\n')
    with open('load_products.txt', 'w') as product_txt:
        for row in products:
            product_txt.write(str(row)+ '\n')

def load_data(couriers, products):
    with open('load_couriers.txt', 'r') as courier_txt:
        for courier in courier_txt.readlines():
            couriers.append(courier.rstrip())
    with open('load_products.txt', 'r') as product_txt:
        for product in product_txt.readlines():
            products.append(product.rstrip())


# products
def show_products(products):
    for number, letter in enumerate(products):
        print(number, letter)
        
def new_product(products):
    new = input('Name of new product:  ')
    return products.append(new)

def update_product(products):
    show_products(products)
    select = int(input('Select Product to update:  '))
    update = input('Enter new name:  ')
    products[select] = update

def delete_product(products):
    show_products(products)
    select = int(input('Select Product to delete:  '))
    products.pop(select)

# couriers
def show_couriers(couriers):
    for number, letter in enumerate(couriers):
        print(number, letter)

def new_courier(couriers):
    new = input('Name of new courier:  ')
    return couriers.append(new)

def update_courier(couriers):
    show_couriers(couriers)
    select = int(input('Select Courier to update:  '))
    update = input('Enter new name:  ')
    couriers[select] = update

def delete_courier(couriers):
    show_couriers(couriers)
    select = int(input('Select Courier to delete:  '))
    couriers.pop(select)