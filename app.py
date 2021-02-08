def main():
    import sys
    import os
    print('              ' + 'Welcome to the app!')
    products = ['Coke','pepsi', '7up', 'noodles', 'kebab shwarma']
    while True:
        print('press 0 to close app' + '     ' + 'press 1 to show products')
        value = int(input("Press 0 or 1 to continue"))
        if value == 0:
            sys.exit(0)  
        elif value == 1:
            import os
            os.system('cls')
            print(*products,sep='\n')
            value2 = int(
                input('<Enter 0 for main manu>   <Enter 1 for product>'   
                '\n<Enter 2 to create new product>   <Enter 3 to update products>'
                '<Enter 4 to delete a product>')
            )
            if value2 == 0:
                os.system('cls')
                main
                print('press 0 to close app' + '     ' + 'press 1 to show products')
            elif value2 == 1:
                os.system('cls')
                print(products)
                print('press 0 to close app' + '     ' + 'press 1 to show products')
            elif value2 == 2:
                os.system('cls')
                print(f"Enter the product you would like!")
                new_product = input()
                products.append(new_product)
                print(products)
            elif value2 == 3:
                os.system('cls')
                print("Please select a product to update."
                "\n Select between 0-5. 0 for coke, 1 for pepsi and so on"
                )
                value3 = int(input())
                if value3 == 0:
                    os.system('cls')
                    products[0] = input('Enter new product name')
                    print(products)
                elif value3 == 1:
                    os.system('cls')
                    products[1] = input('Enter new product name')
                    print(products)
                elif value3 == 2:
                    os.system('cls')
                    products[2] = input('Enter new product name')
                    print(products)
                elif value3 == 3:
                    os.system('cls')
                    products[3] = input('Enter new product name')
                    print(products)
                elif value3 == 4:
                    os.system('cls')
                    products[4] = input('Enter new product name')
                    print(products)
                elif value3 == 5:
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
                value4 = int(input())
                if value4 == 0:
                    os.system('cls')
                    products.pop(0)
                    print(products)
                elif value4 == 1:
                    os.system('cls')
                    products.pop(1)
                    print(products)
                elif value4 == 2:
                    os.system('cls')
                    products.pop(2)
                    print(products)
                elif value4 == 3:
                    os.system('cls')
                    products.pop(3)
                    print(products)
                elif value4 == 4:
                    os.system('cls')
                    products.pop(4)
                    print(products)
                elif value4 == 5:
                    os.system('cls')
                    products.pop(5)
                    print(products)
                else: 
                    print('please enter value between 0-5')
            else:
                print('please enter values between 0 and 2')
        else:
            print('please enter values between 0 and 1')
    os.system('cls')
main()


                    
                
            
                    
