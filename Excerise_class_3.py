class Product:
    product_code = 0

    def __init__(self,name,price,stock_at_locations):
        self.name = name
        self.price = price
        self.stock_at_locations=stock_at_locations

class Location:
    def __init__(self,name, code):
        self.name=name
        self.code=code

    def display_info(self):
        print("location name:", self.name, "code", self.code)


class Movement:

    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        try:
            if product.stock_at_locations[from_location] >= quantity:
                remain_quntity = product.stock_at_locations[from_location] - quantity
                increment_qunatity = product.stock_at_locations[to_location] + quantity
                product.stock_at_locations.update({from_location: remain_quntity, to_location: increment_qunatity})
                
        except Exception:
            print("no location for that product\n")

    @staticmethod
    def movements_by_product(product_info):
        movements_by_product_list = []
        for movement_info in movement_list:
            if movement_info.product.name.lower() == product_info.name.lower():
                movements_by_product_list.append(movement_info)
        return movements_by_product_list



if __name__ == "__main__":

    # Location Info
    rajkot = Location("RAJKOT", 10001)
    morbi = Location("Morbi", 10002)
    bhavnagar = Location("Bhavnagar", 10002)
    vadodara = Location("Vadodara", 10004)
    location_list = [rajkot, morbi, bhavnagar, vadodara]

    for location_info in location_list:
        location_info.display_info()

    # Product Info
    eye_liner = Product('Eye liner',1450000,{rajkot:30, morbi:40, vadodara:10})
    nail_paint = Product('Nail paint',75000,{rajkot:10,morbi:10,bhavnagar:10})
    sunscreen = Product('sunscreem',88500,{morbi:40,bhavnagar:40,vadodara:10})
    body_location = Product('body location',120000,{rajkot:30,bhavnagar:90,vadodara:10})
    powder = Product('powder',7000,{rajkot:2,morbi:100,bhavnagar:10,vadodara:100})

    # amul = Product('Amul',1450000,{rajkot:30, morbi:40, vadodara:10})
    # ufresh = Product('U-fresh',75000,{rajkot:10,morbi:10,bhavnagar:10})
    # gopal = Product('Gopal',88500,{morbi:40,bhavnagar:40,vadodara:10})
    # mahi = Product('Mahi',120000,{rajkot:30,bhavnagar:90,vadodara:10})
    # bicycle = Product('',7000,{rajkot:2,morbi:100,bhavnagar:10,vadodara:100})

    products_list = [eye_liner, nail_paint,sunscreen, body_location, powder]
    print("\n")
    for product_info in products_list:
        print("Product Name -> ",product_info.name)  # print name of product
        print("\n")
        for key in product_info.stock_at_locations:  # print dictionary of location name,quantity value
            print(f'{key.name} - {product_info.stock_at_locations[key]}')

    print("\n")
    movement1 = Movement(rajkot, vadodara, eye_liner, 20)
    movement2 = Movement(morbi,bhavnagar, nail_paint, 10)
    movement3 = Movement(rajkot, vadodara, sunscreen, 20)
    movement4=Movement(vadodara,bhavnagar,body_location, 30)
    movement5 = Movement(morbi, bhavnagar, powder, 50)  

    movement_list = [movement1, movement2, movement3, movement4, movement5]

    for product_info in products_list:
        print("Product Name -> ",product_info.name)   # product name
        print("\n")
        product_movements_list = Movement.movements_by_product(product_info)  # movement of product
        for product_movement_info in product_movements_list:
            print(f"""From Location: {product_movement_info.from_location.name}, 
                To Location: {product_movement_info.to_location.name}, 
                Product: {product_movement_info.product.name}, 
                Quantity: {product_movement_info.quantity}""")
        print("###############################")

    print("\n")
    print("---------------------------------------------------------------------")
    print("######## new stock at location ########")
    for product_info in products_list:
        print(f'Product Name: {product_info.name}')
        for key in product_info.stock_at_locations:
            print(f'{key.name} - {product_info.stock_at_locations[key]}', end='  ')
        print('\n')
        print("###############################")

    # print("product list by location")
    # for i in location_list:
    #     print(i.name)
    #     for p in listofprodcut:
    #         if i in p.stock_at_locations:
    #             print(f'{p.name} - {p.stock_at_locations[i]}')
    #     print()






