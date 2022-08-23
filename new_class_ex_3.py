import pprint
# -------------------Category Class-----------------------------------
class Category(object):

    def __init__(self, category_name, code):
        self.category_name=category_name
        self.code=code        
        self.no_of_products = 0        

    
    def show(self): 
        print(self.category_name,self.code,self.no_of_products)

# ------------------------Product Class---------------------------------------        
class Product(Category):
    
    def __init__(self,  name, code, category, price):
        self.name=name
        self.code=code
        self.category = category
        category.no_of_products = category.no_of_products + 1
        self.price=price
        self.stock_at_location= {}
    
    def disp(self):
        print()
        print(self.name,self.code,self.category.category_name, self.price,self.stock_at_location)
        print("------------------------------------------------------------------")

        #-----------Exception Handling--------------Don't allow Negative value------------------------------------------
        for product_quantity in self.stock_at_location.values():
            try:
                assert product_quantity > 0
                    
            except AssertionError:
                print("Don't allow Negative value")
                print()

# ----------------------Location Class-------------------------------------------------
class location(Product):
    def __init__(self,name,code):
        self.name=name
        self.code=code

    def display(self):
        print("Name : ",self.name,"Code : ",self.code)

# ----------------------------Movement Class-----------------------------------------
class movement(location):
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        

    @staticmethod
    def movements_by_product(product):
       for movement_product in move_list:
            if movement_product.product.name == product:
                print("From location :- ",movement_product.from_location,"\nTo location :-",movement_product.to_location,"\nQuantity :-",movement_product.quantity)
                print()

        
    def show(self):
        print("From Location : ",self.from_location,"To_Location : ",self.to_location,"Product  :",self.product,"Quantity :",self.quantity)    


# --------------Create Category Class Object---------------------
c1 = Category("Amul",101)
c2 = Category("U-fresh",103)
c3 = Category("Gopal", 104)
c4 = Category("Mahi",106)


# ---------------Create Product Class Object------------------------
p1 =Product("Milk", "AE10234" , c1 , 30 )
p2 =Product("Butter" , "AS9874" , c1 , 75)
p3 =Product("Cheese" , "ADC2365" , c1 , 110)
p4 =Product("Butter Milk" , "AWD5697" , c2 , 15)
p5 =Product("Frimes" , "AZX2589" , c3 , 10)

#---------------Create Location Class Object-----------------------
l1 = location("Junagadh",362001)
l2 = location("Rajkot",360004)
l3 = location("Ahemdabad",380003)
l4 = location("Baroda",390023)


#--------------Create Movement Object--------------------------
m1=movement("Rajkot","Baroda",p1,-10)
m2=movement("Rajkot","Junagadh",p2,9)
m3=movement("Rajkot","Ahemdabad",p4,5)
m4=movement("Rajkot","Baroda",p1,-15)
m5=movement("Rajkot","Baroda",p3,25)
m6=movement("Rajkot","Baroda",p5,6)
m7=movement("Rajkot","Junagadh",p2,1)



p_list = [p1,p2,p3,p4,p5]
cat_list = [c1,c2,c3,c4]   
l_list = [l1,l2,l3,l4]
move_list = [m1,m2,m3,m4,m5,m6,m7]  

# --------------Static method call Movement by product-----------Direct access class
movement.movements_by_product("Milk")

#----------------Display product list by location   (Group by location)-----------------------------------

for location_name in l_list:
    if location_name.name:
        print("---------------------------------------------")
        print(location_name.name)
        print("---------------------------------------------")
        for movement_location in move_list:
            for product_item in p_list:
                if location_name.name == movement_location.to_location:
                    if movement_location.product.name == product_item.name:
                        print(product_item.name,product_item.code,product_item.category.category_name,product_item.price)  
                        print()      


#--------------------Movement Class-----------------Check location and Product-------------------------------------
stock_movement_list = []

for movement_info in move_list:
    
    update = False
    
    for stock_movement_info in stock_movement_list:
        #print(stock_movement_info['to_location'],stock_movement_info['quantity'])
        if movement_info.product.name == stock_movement_info['product'] and movement_info.from_location == stock_movement_info['from_location'] and movement_info.to_location == stock_movement_info['to_location']:
            stock_movement_info['quantity'] += movement_info.quantity
            #print(stock_movement_info['to_location'],stock_movement_info['quantity'])

# #--------------Append data in Product class--------Location as a key : Quantity as a value ------Stock at location in Product Category------------------------------
            
            movement_info.product.stock_at_location = ({stock_movement_info['to_location']:stock_movement_info['quantity']})
            update = True

          
    if not update:
        stock_movement_list.append({'product': movement_info.product.name,'from_location' : movement_info.from_location,'to_location': movement_info.to_location, 'quantity': movement_info.quantity})
        movement_info.product.stock_at_location = ({movement_info.to_location:movement_info.quantity})
    #pprint.pprint(stock_movement_list)

print("\n")
print("************************************************************************************")
pprint.pprint(stock_movement_list)
print("************************************************************************************")
print("\n")


p1.disp()
p2.disp()
p3.disp()
p4.disp()
p5.disp()