import sys
import os
# import Loading_data

#Empty list for couriers and products

def main_menu():
    return 0


couriers = []
products = []

def load_data(couriers, products):
    with open('load_couriers.txt', 'r') as courier_txt:
        for courier in courier_txt.readlines():
            couriers.append(courier.rstrip())
    with open('load_products.txt', 'r') as product_txt:
        for product in product_txt.readlines():
            products.append(product.rstrip())


def save_data(couriers, products):
    with open('load_couriers.txt', 'w') as courier_txt:
        for row in couriers:
            courier_txt.write(str(row) + '\n')
    with open('load_products.txt', 'w') as product_txt:
        for row in products:
            product_txt.write(str(row)+ '\n')

# product = products

def couriers_menu(): #Function to get back to couriers menu.
    main_menu_optionc = int(
    input('<Enter 0 for main menu>   <Enter 1 to print couriers on screen>'   
    '\n<Enter 2 to create new couriers>   <Enter 3 to update Couriers>'
    '<Enter 4 to delete a couriers>'))

##### Function to get back to couriers menu
def products_menu(): #Function to get back to couriers menu
    os.system('cls')
    print('Product Menu')
    print('')
    print(*products,sep='\n')
    print('')
    product_menu_option = int(
    input('<Enter 0 for main menu>   <Enter 1 for product>'   
    '\n<Enter 2 to create new product>   <Enter 3 to update products>'
    '\n<Enter 4 to delete a product>'))
    return product_menu_option


load_data(couriers, products)
save_data(couriers, products)
while True:
    os.system('cls')
    print('Welcome to the app!')
    print('')
    main_menu_option = int(input("Press 0 to close app \nPress 1 to show products Menu \nPress 2 for Couriers Menu"))
    if main_menu_option == 0:
        print('')
        print('....closing app ....')
        save_data(couriers, products)
        sys.exit(0)
    elif main_menu_option == 1: # Enter product menu
        os.system('cls')
        print('Product Menu')
        print('')
        print(*products,sep='\n')
        print('')
        product_menu_option = int(
        input('<Enter 0 for main menu>   <Enter 1 for product>'   
        '\n<Enter 2 to create new product>   <Enter 3 to update products>'
        '\n<Enter 4 to delete a product>'))
        if product_menu_option == 0:
            os.system('cls')
            main_menu()


        elif product_menu_option == 1:
            os.system('cls')
            print('Products')
            print('')
            print(*products,sep='\n')
            print('')
            Exitmenu_mainmenu_productmenu_options = int(
            input('<Enter 0 for main menu>\n<Enter 1 for products menu>\n<Enter 2 to exit app'))
            if Exitmenu_mainmenu_productmenu_options == 0:
                os.system('cls')
                main_menu()
            elif Exitmenu_mainmenu_productmenu_options == 1:
                os.system('cls')
                products_menu()
            elif Exitmenu_mainmenu_productmenu_options == 2:
                sys.exit(3)
            else:
                os.system('cls')
                print('<oops!!! Please enter 0 or 1>') 


### create new products
        elif product_menu_option == 2:
            #main_menu_option2 = products_menu()
            os.system('cls')
            print(f"Enter the product you would like!")
            new_product = input()
            products.append(new_product)
            print('')
            print('Updated products')
            print(*products,sep='\n')
            print('')


            back_to_main_and_product_menu = int(
            input('<Enter 0 for main menu>   <Enter 1 for products menu>'))
            if back_to_main_and_product_menu == 0:
                os.system('cls')
                main_menu()
            elif back_to_main_and_product_menu == 1:
                os.system('cls')
                products_menu()
            else:
                os.system('cls')
                print('<Please enter 0 or 1>') 

######## Updating a product

        elif product_menu_option == 3:
            os.system('cls')
            print(*products,sep='\n')
            product_length = len(products) - 1
            print(f"Please select a product to update."
            f"\n Select between 0-{product_length}. 0 for coke, 1 for pepsi and so on"
            )
            products_update = int(input())
            if products_update == 0:
                os.system('cls')
                products[0] = input('Enter new product name')
                print(*products, sep='\n')
                back_to_main_and_product_menu = int(
                input('<Enter 0 for main menu>   <Enter 1 for products menu>'))


                if back_to_main_and_product_menu == 0:
                    os.system('cls')
                    main_menu()
                elif back_to_main_and_product_menu == 1:
                    os.system('cls')
                    products_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 


            elif products_update == 1:
                os.system('cls')
                products[1] = input('Enter new product name')
                print(*products, sep='\n')


                back_to_main_and_product_menu = int(
                input('<Enter 0 for main menu>   <Enter 1 for products menu>'))
                if back_to_main_and_product_menu == 0:
                    os.system('cls')
                    main_menu()
                elif back_to_main_and_product_menu == 1:
                    os.system('cls')
                    products_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 


            elif products_update == 2:
                os.system('cls')
                products[2] = input('Enter new product name')
                print(*products, sep='\n')


                back_to_main_and_product_menu = int(
                input('<Enter 0 for main menu>   <Enter 1 for products menu>'))
                if back_to_main_and_product_menu == 0:
                    os.system('cls')
                    main_menu()
                elif back_to_main_and_product_menu == 1:
                    os.system('cls')
                    products_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 


            elif products_update == 3:
                os.system('cls')
                products[3] = input('Enter new product name')
                print(*products, sep='\n')


                back_to_main_and_product_menu = int(
                input('<Enter 0 for main menu>   <Enter 1 for products menu>'))
                if back_to_main_and_product_menu == 0:
                    os.system('cls')
                    main_menu()
                elif back_to_main_and_product_menu == 1:
                    os.system('cls')
                    products_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')


            elif products_update == 4:
                os.system('cls')
                products[4] = input('Enter new product name')
                print(*products, sep='\n')


                back_to_main_and_product_menu = int(
                input('<Enter 0 for main menu>   <Enter 1 for products menu>'))
                if back_to_main_and_product_menu == 0:
                    os.system('cls')
                    main_menu()
                elif back_to_main_and_product_menu == 1:
                    os.system('cls')
                    products_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')


            elif products_update == 5:
                os.system('cls')
                products[5] = input('Enter new product name')
                print(*products, sep='\n')
            else: 
                print('please enter main_menu_option between 0-5')


####### Deleting a product
        elif product_menu_option == 4:
            os.system('cls')
            print( "Please select a product to update."
            "\n Select between 0-5. 0 for coke, 1 for pepsi and so on"
            )
            main_menu_option2b = int(input())
            if main_menu_option2b == 0:
                os.system('cls')
                products.pop(0)
                print(*products, sep='\n')
            elif main_menu_option2b == 1:
                os.system('cls')
                products.pop(1)
                print(*products, sep='\n')
            elif main_menu_option2b == 2:
                os.system('cls')
                products.pop(2)
                print(*products, sep='\n')
            elif main_menu_option2b == 3:
                os.system('cls')
                products.pop(3)
                print(*products, sep='\n')
            elif main_menu_option2b == 4:
                os.system('cls')
                products.pop(4)
                print(*products, sep='\n')
            elif main_menu_option2b == 5:
                os.system('cls')
                products.pop(5)
                print(*products, sep='\n')
            else: 
                print('please enter value between 0-5')


        else:
            print('please enter value between 0 and 2')


    elif main_menu_option == 2: #Enter into Couriers menu
        os.system('cls')
        main_menu() 
        print(*couriers,sep='\n') 
        main_menu_optionc = int(
        input('<Enter 0 for main menu>   <Enter 1 to print couriers on screen>'   
        '\n<Enter 2 to create new couriers>   <Enter 3 to update Couriers>'
        '<Enter 4 to delete a couriers>'))
        if main_menu_optionc == 0:
            os.system('cls')
            main_menu()


        elif main_menu_optionc == 1:
            os.system('cls')
            print(couriers)
            main_menu_optionc1 = int(
            input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
            if main_menu_optionc1 == 0:
                os.system('cls')
                main_menu()
            elif main_menu_optionc1 == 1:
                os.system('cls')
                couriers_menu()
            else:
                os.system('cls')
                print('<Please enter 0 or 1>')   


        elif main_menu_optionc == 2: #Adding new couriers
            os.system('cls')
            print(f"Enter the couriers you would like!")
            new_couriers = input()
            couriers.append(new_couriers)
            print(couriers)
            main_menu_optionc2 = int(
            input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
            if main_menu_optionc2 == 0:
                os.system('cls')
                main_menu()
            elif main_menu_optionc2 == 1:
                os.system('cls')
                couriers_menu()
            else:
                os.system('cls')
                print('<Please enter 0 or 1>')  


        elif main_menu_optionc == 3: #updating a courier
            os.system('cls')
            print(couriers)
            print("Please select a couriers from above to update."
            "\n Select between 0-5. 0 for matt, 1 for ali and so on"
            )
            main_menu_optionc3 = int(input())
            if main_menu_optionc3 == 0:
                os.system('cls')
                couriers[0] = input('Enter new couriers name')
                print(f'Updated couriers\n{couriers}')
                main_menu_optionf = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionf == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionf == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')   
            elif main_menu_optionc3 == 1:
                os.system('cls')
                couriers[1] = input('Enter new couriers name')
                print(f'Updated couriers\n{couriers}')
                main_menu_optionf1 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionf1 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionf1 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')


            elif main_menu_optionc3 == 2:
                os.system('cls')
                couriers[2] = input('Enter new couriers name')
                print(couriers)
                main_menu_optionf2 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionf2 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionf2 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')


            elif main_menu_optionc3 == 3:
                os.system('cls')
                couriers[3] = input('Enter new couriers name')
                print(couriers)
                main_menu_optionf3 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionf3 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionf3 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')
            elif main_menu_optionc3 == 4:
                os.system('cls')
                couriers[4] = input('Enter new couriers name')
                print(couriers)
                main_menu_optionf4 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionf4 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionf4 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')
            elif main_menu_optionc3 == 5:
                os.system('cls')
                couriers[5] = input('Enter new couriers name')
                print(couriers)
            else: 
                print('please enter main_menu_option between 0-5')
        elif main_menu_optionc == 4:
            os.system('cls')
            print( "Please select a couriers to delete."
            "\n Select between 0-5. 0 for coke, 1 for pepsi and so on"
            )
            main_menu_optionc4 = int(input())
            if main_menu_optionc4 == 0:
                os.system('cls')
                couriers.pop(0)
                print(f'Updated couriers\n{couriers}')
                main_menu_optionc4f == int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionc4f == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionc4f == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')   
            elif main_menu_optionc4 == 1:
                os.system('cls')
                couriers.pop(1)
                print(f'Updated couriers\n{couriers}')
                main_menu_optionc4f1 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionc4f1 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionc4f1 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>')   
            elif main_menu_optionc4 == 2:
                os.system('cls')
                couriers.pop(2)
                print(f'Updated couriers\n{couriers}')
                main_menu_optionc4f2 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionc4f2 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionc4f2 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            elif main_menu_optionc4 == 3:
                os.system('cls')
                couriers.pop(3)
                print(f'Updated couriers\n{couriers}')
                main_menu_optionc4f3 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionc4f3 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionc4f3 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            elif main_menu_optionc4 == 4:
                os.system('cls')
                couriers.pop(4)
                print(f'Updated couriers\n{couriers}')
                main_menu_optionc4f4 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionc4f4 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionc4f4 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            elif main_menu_optionc4 == 5:
                os.system('cls')
                couriers.pop(5)
                print(f'Updated couriers\n{couriers}')
                main_menu_optionc4f5 = int(
                input('<Enter 0 for main menu>   <Enter 1 for couriers menu>'))
                if main_menu_optionc4f5 == 0:
                    os.system('cls')
                    main_menu()
                elif main_menu_optionc4f5 == 1:
                    os.system('cls')
                    couriers_menu()
                else:
                    os.system('cls')
                    print('<Please enter 0 or 1>') 
            else: 
                print('please enter main_menu_option between 0-5')
    else:
        print('please enter main_menu_options between 0 and 1')
main_menu()
os.system('cls')