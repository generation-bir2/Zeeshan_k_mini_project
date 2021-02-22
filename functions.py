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
    select = input('write Courier name to delete:  ')
    mycursor.execute("DELETE FROM couriers where name=(%s)", (select))


# Orders

def show_orders():
    mycursor.execute("SELECT * FROM Orders")
    myresult = mycursor.fetchall()
    print('Orders Table')
    for row in myresult:
        print("-----------------------")
        print(f"Order ID: {row[0]}")
        print(f"Customer name: {row[1]}")
        print(f"Customer Address: {row[2]}")
        print(f"Customer phone: {row[3]}")
        print(f"Courier: {row[4]}")
        print(f"Status: {row[5]}")
        print(f"Items: {row[6]}")

def new_order():
    new_name = input('Enter new customer name: ')
    new_address = input('Enter new customer address: ')
    new_phone = input('Enter new customer phone no: ')
    show_couriers()
    select_courier = input('Enter courier name: ')
    order_status = input('Enter order status: ')
    os.system('clear')
    show_products()
    items = input('Enter items on order: ')
    mycursor.execute("INSERT INTO Orders (Customer_Name, Customer_Address, Customer_phone, Courier, Status, Item) VALUES (%s, %s, %s, %s, %s, %s)", 
    (new_name, new_address, new_phone,select_courier, order_status, items))

def update_orders():
    show_orders()
    select = input('Enter the customer name to update:  ')
    os.system('clear')
    new_name = input('Enter new customer name: ')
    new_address = input('Enter new customer address: ')
    new_phone = input('Enter new customer phone no: ')
    show_couriers()
    select_courier = input('Enter a couriers name: ') 
    order_status = input('Enter order status: ')
    os.system('clear')
    show_products()
    items = input('Enter items on order: ')
    mycursor.execute("UPDATE Orders SET Customer_Name=(%s), Customer_Address=(%s), Customer_phone=(%s), Courier=(%s), status=(%s), Item=(%s) where Customer_Name=(%s)", 
    (new_name, new_address, new_phone, select_courier, order_status, items, select))

def delete_orders():
    show_orders()
    select = input('write customers name on order to delete:  ')
    mycursor.execute("DELETE FROM Orders where Customer_Name=(%s)", (select))