import sys
import os
from dotenv import load_dotenv
from functions import *

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host,
    user,
    password,
    database
)

couriers = []
products = []
orders = []

load_data(couriers, products)

print('''
___________________________
|                         |
|                         |
|  Welcome To The App!!   |
|                         |
|_________________________|

''')

while True:
    print('0 - Close App\n1 - Products\n2 - Couriers\n3 - Orders')
    main_menu = int(input('\nselect menu option: '))
    os.system('clear')
    
    if main_menu == 0:
        save_data(couriers, products)
        sys.exit(0)
    
    # products
    elif main_menu == 1:
        print('0 - Return\n1 - Show Products\n2 - New Product\n3 - Update Product\n4 - Delete Product')
        products_menu = int(input('select menu option: '))
        os.system('clear')

        if products_menu == 0:
            os.system('clear')
        
        elif products_menu == 1:
            show_products(products)
            input('Press Any Button To Continue')
            os.system('clear')

        elif products_menu == 2:
            new_product(products)
            input('Press Any Button To Continue')
            os.system('clear')

        elif products_menu == 3:
            update_product(products)
            input('Press Any Button To Continue')
            os.system('clear')

        elif products_menu == 4:
            delete_product(products)
            input('Press Any Button To Continue')
            os.system('clear')
    
    elif main_menu == 2:
        print('0 - Return\n1 - Show Couriers\n2 - New Courier\n3 - Update Courier\n4 - Delete Courier')
        couriers_menu = int(input('select menu option: '))
        os.system('clear')

        if couriers_menu == 0:
            os.system('clear')

        elif couriers_menu == 1:
            show_couriers(couriers)
            input('Press Any Button To Continue')
            os.system('clear')

        elif couriers_menu == 2:
            new_courier(couriers)
            input('Press Any Button To Continue')
            os.system('clear')

        elif couriers_menu == 3:
            update_courier(couriers)
            input('Press Any Button To Continue')
            os.system('clear')

        elif couriers_menu == 4:
            delete_courier(couriers)
            input('Press Any Button To Continue')
            os.system('clear')


    # elif main_menu == 3:
    #     orders_menu == int(input('select menu option: '))

    #     if orders_menu == 0:
    #         os.system('cls')
        
    #     elif orders_menu == 1:
        
    #     elif orders_menu == 2:
        
    #     elif orders_menu == 3: