
import class_excerise_2
from class_excerise_2 import Category,Product

class location:
    def __init__(self,name,code):
        self.name=name
        self.code=code

    def disp(self):
        print("Name : ",self.name,"Code : ",self.code)

# ----------------------------Movement Class-----------------------------------------
class movement:
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        self.display=''
        try:
            if self.product.stock_at_location[self.from_location] >= self.quantity:
#-------------------------------------Decrese Quantity in from location-------------------------------------
                quant= self.product.stock_at_location[self.from_location] - self.quantity
                self.product.stock_at_location.update({self.from_location: quant})
                if self.to_location in self.product.stock_at_location:  
                    qun1 = self.product.stock_at_location[self.to_location] + self.quantity  
                    self.product.stock_at_location.update({self.to_location.name: qun1}) 
                else:
#----------------------- If not available location then upd Location and Quantity------------------------
                    self.product.stock_at_location.update({self.to_location: self.quantity})
                print(self.product.name,"Movement Done")
                self.display = f'Product Quantity :{self.quantity} from {self.from_location} to {self.to_location}'

            else:
                print(f"Quantity: {self.quantity} of {self.product.name} Not available {self.from_location.name}")
        except Exception as error:
            print("no location for that product\n",error)

#-----------------------------Static method in Movement class-------------------------------
    @staticmethod
    def movement_by_product(product):
        n = 0
        for m in movement_list:
            if m.product.name == product.name:
                n = 1
                print(m.display)

        if n == 0:
            print("No movements..........")

#---------------------------------------- Create Location Class Object------------------------------------------
if __name__ == "__main__":
    location_rajkot=location("Rajkot",360004)
    location_baroda=location("Baroda",390023)
    location_ahemdabad=location("Ahemdabad",380003)
    location_junagadh=location("Junagadh",362001)

    # ----------------------------------------- Location list-------------------------------------------
    location_list = [location_rajkot,location_baroda,location_ahemdabad,location_junagadh]
    for l in location_list:

        l.disp()

    # ----------- Create Category class object------------------------------------------------------------
    category_obj1 = Category("Amul",101)

    # ---------------Create Product class object & Location as a key : Quantity as a value---------
    product_obj1=Product("Chochlet",100,category_obj1,200,{location_rajkot:10,location_ahemdabad:5})
    product_obj2=Product("Butter Milk",50,category_obj1,100,{location_baroda:10,location_junagadh:20})
    product_obj3=Product("Milk",20,category_obj1,300,{location_rajkot:10,location_ahemdabad:1})
    product_obj4=Product("Cheese",150,category_obj1,200,{location_ahemdabad:9,location_rajkot:20})
    product_obj5=Product("Butter",30,category_obj1,200,{location_rajkot:5,location_ahemdabad:5})

    #--------------Create product list---------------------------------
    product_list = [product_obj1,product_obj2,product_obj3,product_obj4,product_obj5]

    for p in product_list:
        print()
        print(p.name)
        
        for key in p.stock_at_location:
            print(f'{key.name} :- {p.stock_at_location[key]}')
        print()
    print("\n")

    # -------------Movement class object---------------------
    movement1 = movement(location_ahemdabad,location_baroda,product_obj1,50)
    movement2 = movement(location_junagadh,location_baroda,product_obj2,30)
    movement3 = movement(location_ahemdabad,location_baroda,product_obj5,80)
    movement4 = movement(location_rajkot,location_baroda,product_obj2,20)
    movement5 = movement(location_baroda,location_rajkot,product_obj4,150)

    # ---------------List of movement class---------------------------
    movement_list = [movement1,movement2,movement3,movement4,movement5]

    for i in product_list:
        print(i.name)  
        movement.movement_by_product(i)  # Movement of product
        print()
    print("\n")
    print("---------------------------------------------")
    print("New stock at location")
    for i in product_list:
        # print("Helllloooooooooooooooo")
        i.disp()
        for location_key in i.stock_at_location:


            print(f'{location_key.name} - {i.stock_at_location[location_key]}', end=' ')
        print('\n')
   
    print("product list by location")
    print("--------------------------------------------")
    
    for i in location_list:
        print(i.name)
        for p in product_list:
            if i in p.stock_at_location:
                print(f'{p.name} - {p.stock_at_location[i]}')
        print()
