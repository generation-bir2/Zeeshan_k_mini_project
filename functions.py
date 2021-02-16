import pymysql
from dotenv import load_dotenv
import os

host='localhost'
user='root'
password='password'
database='db'

def save_data():
    # with open('load_couriers.txt', 'w') as courier_txt:
    #     for row in couriers:
    #         courier_txt.write(str(row) + '\n')
    # with open('load_products.txt', 'w') as product_txt:
    #     for row in products:
    #         product_txt.write(str(row)+ '\n')
    connection.commit()
# def load_data(couriers, products):
    # with open('load_couriers.txt', 'r') as courier_txt:
    #     for courier in courier_txt.readlines():
    #         couriers.append(courier.rstrip())
    # with open('load_products.txt', 'r') as product_txt:
    #     for product in product_txt.readlines():
    #         products.append(product.rstrip())

connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database,
)

mycursor = connection.cursor()

# products
def show_products():
    mycursor.execute("SELECT * FROM products")
    myresult = mycursor.fetchall()
    print('Products Table')
    for row in myresult:
        print("-----------------------")
        print(f"Product ID: {row[0]}")
        print(f"Product name: {row[1]}")
        print(f"Product price: {row[2]}")
        print("-----------------------")

def new_product():
    new = input('Name of new product:  ')
    new_price = input('Price of new product:  ')
    mycursor.execute("INSERT INTO products (product, price) VALUEs (%s,%s)", (new,new_price))
    # return products.append(new)

def update_product():
    show_products()
    select = input('Enter the product name to update:  ')
    update_product = input('Enter new name:  ')
    update_price = input('Price of new product:  ')
    mycursor.execute("UPDATE products SET product=(%s), price=(%s) where product=(%s)", (update_product,update_price,select))
    #products[select] = update

def delete_product():
    show_products()111
    select = input('Enter the product name to Delete:  ')
    mycursor.execute("DELETE FROM products where product=(%s)", (select))
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