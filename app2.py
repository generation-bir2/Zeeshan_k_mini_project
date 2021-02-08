import sys
import os
couriers = []
products = []
def main_menu():
    with open('load_couriers.txt', 'r') as courier_txt:
        for courier in courier_txt.readlines():
            couriers.append(courier.rstrip())
    with open('load_products.txt', 'r') as product_txt:
        for product in product_txt.readlines():
            products.append(product.rstrip())
def couriers_menu(): #Function to get back to couriers menu.
    valuec = int(
    input('<Enter 0 for main menu>   <Enter 1 to print couriers on screen>'   
    '\n<Enter 2 to create new couriers>   <Enter 3 to update Couriers>'
    '<Enter 4 to delete a couriers>'))
def products_menu(): #Function to get back to couriers menu
    os.system('cls')
    print('Product Menu')
    print('')
    print(*products,sep='\n')
    print('')
    value2 = int(
    input('<Enter 0 for main menu>   <Enter 1 for product>'   
    '\n<Enter 2 to create new product>   <Enter 3 to update products>'
    '\n<Enter 4 to delete a product>'))

while True:
    os.system('cls')
    print('Welcome to the app!')
    print('')
    value = int(input("Press 0 to close app\n"
    "Press 1 to show products Menu\nPress 2 for Couriers Menu"))
    if value == 0:
        print('')
        print('....closing app ....')
        sys.exit(0)
    elif value == 1:
        main_menu()
        os.system('cls')
        print('Product Menu')
        print('')
        print(*products,sep='\n')
        print('')
        value2 = int(
        input('<Enter 0 for main menu>   <Enter 1 for product>'   
        '\n<Enter 2 to create new product>   <Enter 3 to update products>'
        '\n<Enter 4 to delete a product>'))
        if value2 == 0:
            os.system('cls')
            main_menu()
            #print('press 0 to close app\npress 1 to show products')
        elif value2 == 1:
            os.system('cls')
            print('Products')
            print('')
            print(*products,sep='\n')
            print('')
            value2f1 = int(
            input('<Enter 0 for main menu>\n<Enter 1 for products menu>\n<Enter 2 to exit app'))
            if value2f1 == 0:
                os.system('cls')
                main_menu()
            elif value2f1 == 1:
                os.system('cls')
                products_menu()
            elif value2f1 == 2:
                sys.exit(3)
            else:
                os.system('cls')
                print('<oops!!! Please enter 0 or 1>') 
        elif value2 == 2:
            #product_menu()
            #os.system('cls')
            print(f"Enter the product you would like!")
            new_product = input()
            products.append(new_product)
            print(f'UPDATED PRODUCT\n{products}')
        elif value2 == 3:
            os.system('cls')
            print("Please select a product to update."
            "\n Select between 0-5. 0 for coke, 1 for pepsi and so on"
            )
            value2a = int(input())
            if value2a == 0:
                os.system('cls')
                products[0] = input('Enter new product name')
                print(products)
            elif value2a == 1:
                os.system('cls')
                products[1] = input('Enter new product name')
                print(products)
            elif value2a == 2:
                os.system('cls')
                products[2] = input('Enter new product name')
                print(products)
            elif value2a == 3:
                os.system('cls')
                products[3] = input('Enter new product name')
                print(products)
            elif value2a == 4:
                os.system('cls')
                products[4] = input('Enter new product name')
                print(products)
            elif value2a == 5:
                os.system('cls')
                products[5] = input('Enter new product name')
                print(products)
            else: 
                print('please enter value between 0-5')
        elif value2 == 4:
            os.system('cls')
            print( "Please select a product to update."
            "\n Select between 0-5. 0 for coke, 1 for pepsi and so on"
            )
            value2b = int(input())
            if value2b == 0:
                os.system('cls')
                products.pop(0)
                print(products)
            elif value2b == 1:
                os.system('cls')
                products.pop(1)
                print(products)
            elif value2b == 2:
                os.system('cls')
                products.pop(2)
                print(products)
            elif value2b == 3:
                os.system('cls')
                products.pop(3)
                print(products)
            elif value2b == 4:
                os.system('cls')
                products.pop(4)
                print(products)
            elif value2b == 5:
                os.system('cls')
                products.pop(5)
                print(products)
            else: 
                print('please enter value between 0-5')
        else:
            print('please enter values between 0 and 2')
    elif value == 2:   #Enter into Couriers menu
        couriers_menu()
        if valuec == 0:
            os.system('cls')
            main_menu()
        elif valuec == 1:
            os.system('cls')
            print(couriers)
            valuec1 = int(
            input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
            if valuec1 == 0:
                os.system('cls')
                main_menu()
            elif valuec1 == 1:
                os.system('cls')
                couriers_menu()
            else:
                os.system('cls')
                print('<Please enter 0 or 1>')   
        elif valuec == 2: #Adding new couriers
            os.system('cls')
            print(f"Enter the couriers you would like!")
            new_couriers = input()
            couriers.append(new_couriers)
            print(couriers)
            valuec2 = int(
            input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
            if valuec2 == 0:
                os.system('cls')
                main_menu()
            elif valuec2 == 1:
                os.system('cls')
                couriers_menu()
            else:
                os.system('cls')
                print('<Please enter 0 or 1>')   
        elif valuec == 3: #updating a courier
            os.system('cls')
            print(couriers)
            print("Please select a couriers from above to update."
            "\n Select between 0-5. 0 for matt, 1 for ali and so on"
            )
            valuec3 = int(input())
            if valuec3 == 0:
                os.system('cls')
                couriers[0] = input('Enter new couriers name')
                print(f'Updated couriers\n{couriers}')
                valuef = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuef == 0:
                    os.system('cls')
                    main_menu()
                elif valuef == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')   
            elif valuec3 == 1:
                os.system('cls')
                couriers[1] = input('Enter new couriers name')
                print(f'Updated couriers\n{couriers}')
                valuef1 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuef1 == 0:
                    os.system('cls')
                    main_menu()
                elif valuef1 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')
            elif valuec3 == 2:
                os.system('cls')
                couriers[2] = input('Enter new couriers name')
                print(couriers)
                valuef2 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuef2 == 0:
                    os.system('cls')
                    main_menu()
                elif valuef2 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')
            elif valuec3 == 3:
                os.system('cls')
                couriers[3] = input('Enter new couriers name')
                print(couriers)
                valuef3 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuef3 == 0:
                    os.system('cls')
                    main_menu()
                elif valuef3 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')
            elif valuec3 == 4:
                os.system('cls')
                couriers[4] = input('Enter new couriers name')
                print(couriers)
                valuef4 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuef4 == 0:
                    os.system('cls')
                    main_menu()
                elif valuef4 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')
            elif valuec3 == 5:
                os.system('cls')
                couriers[5] = input('Enter new couriers name')
                print(couriers)
            else: 
                print('please enter value between 0-5')
        elif valuec == 4:
            os.system('cls')
            print( "Please select a couriers to delete."
            "\n Select between 0-5. 0 for coke, 1 for pepsi and so on"
            )
            valuec4 = int(input())
            if valuec4 == 0:
                os.system('cls')
                couriers.pop(0)
                print(f'Updated couriers\n{couriers}')
                valuec4f == int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuec4f == 0:
                    os.system('cls')
                    main_menu()
                elif valuec4f == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')   
            elif valuec4 == 1:
                os.system('cls')
                couriers.pop(1)
                print(f'Updated couriers\n{couriers}')
                valuec4f1 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuec4f1 == 0:
                    os.system('cls')
                    main_menu()
                elif valuec4f1 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')   
            elif valuec4 == 2:
                os.system('cls')
                couriers.pop(2)
                print(f'Updated couriers\n{couriers}')
                valuec4f2 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuec4f2 == 0:
                    os.system('cls')
                    main_menu()
                elif valuec4f2 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            elif valuec4 == 3:
                os.system('cls')
                couriers.pop(3)
                print(f'Updated couriers\n{couriers}')
                valuec4f3 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuec4f3 == 0:
                    os.system('cls')
                    main_menu()
                elif valuec4f3 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            elif valuec4 == 4:
                os.system('cls')
                couriers.pop(4)
                print(f'Updated couriers\n{couriers}')
                valuec4f4 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuec4f4 == 0:
                    os.system('cls')
                    main_menu()
                elif valuec4f4 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            elif valuec4 == 5:
                os.system('cls')
                couriers.pop(5)
                print(f'Updated couriers\n{couriers}')
                valuec4f5 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if valuec4f5 == 0:
                    os.system('cls')
                    main_menu()
                elif valuec4f5 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            else: 
                print('please enter value between 0-5')
    else:
        print('please enter values between 0 and 1')
main_menu()
os.system('cls')