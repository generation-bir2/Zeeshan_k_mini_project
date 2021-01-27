def main():
    import sys
    load_couriers = open('load_couriers.txt', 'r')
    load_products = open('load_products.txt', 'r')
    couriers = []
    products = []
    for courier in load_couriers.readlines():
        couriers.append(courier.rstrip())
    print(couriers)
    for porduct in load_products.readlines():
        products.append(product.rstip())
    print (products)
main()