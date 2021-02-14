    couriers = []
    products = []
def load_data():
    with open('load_couriers.txt', 'r') as courier_txt:
        for courier in courier_txt.readlines():
            couriers.append(courier.rstrip())
    with open('load_products.txt', 'r') as product_txt:
        for product in product_txt.readlines():
            products.append(product.rstrip())