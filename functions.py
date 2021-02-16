import pymysql
from dotenv import load_dotenv
import os

host='localhost'
user='root'
password='password'
database='db'


def save_data():
    connection.commit()


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


def update_product():
    show_products()
    select = input('Enter the product name to update:  ')
    update_product = input('Enter new name:  ')
    update_price = input('Price of new product:  ')
    mycursor.execute("UPDATE products SET product=(%s), price=(%s) where product=(%s)", (update_product,update_price,select))


def delete_product():
    show_products()
    select = input('Enter the product name to Delete:  ')
    mycursor.execute("DELETE FROM products where product=(%s)", (select))
# couriers
def show_couriers():
    mycursor.execute("SELECT * FROM couriers")
    myresult = mycursor.fetchall()
    print('Couriers Table')
    for row in myresult:
        print("-----------------------")
        print(f"Couriers ID: {row[0]}")
        print(f"Couriers name: {row[1]}")
        print(f"Couriers phone: {row[2]}")
        print("-----------------------")


def new_courier():
    new = input('Name of new courier:  ')
    new_price = input('phone number of new courier:  ')
    mycursor.execute("INSERT INTO couriers (name, phone) VALUEs (%s,%s)", (new,new_price))
    # new = input('Name of new courier:  ')
    # return couriers.append(new)

def update_courier():
    show_couriers()
    select = input('Enter the courier name to update:  ')
    update_name = input('Enter new name:  ')
    update_phone = input('phone of new courier:  ')
    mycursor.execute("UPDATE couriers SET name=(%s), phone=(%s) where name=(%s)", (update_name,update_phone,select))

def delete_courier():
    show_couriers()
    select = input('Select Courier to delete:  ')
    mycursor.execute("DELETE FROM couriers where name=(%s)", (select))


