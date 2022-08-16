import sys

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
        print(self.name,self.code,self.category.category_name, self.price,self.stock_at_location)
        #print(self.stock_at_location)
        stock_at_locat = self.stock_at_location.values()
        #print(stock_at_locat)
        
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
        return product

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


# c1.show()
# c2.show()
# c3.show()
# c4.show()



p_list = [p1,p2,p3,p4,p5]
cat_list = [c1,c2,c3,c4]   
l_list = (l1,l2,l3,l4)
move_list = [m1,m2,m3,m4,m5,m6,m7]           

#--------------Append data in Product class--------Location as a key ------Stock at location in Product Category------------------------------

# for p in p_list:
#     add_quant = 0
#     my_dict = {}
    
#     if p.name:
#         #print(p.name)
#         for m in move_list:
            
#             if p.name == m.product.name:
#                 add_quant += m.quantity
#                 my_dict.update({m.to_location:add_quant})
#                 #print(my_dict)
#                 p.stock_at_location = my_dict
#                 #print(p.stock_at_location)

# #--------------------Exception Handle negative value--------------------------

#                 stock_at_locat = p.stock_at_location.values()
#                 #print(stock_at_locat)
                
#                 for stock in stock_at_locat:
                    
#                     try:
#                         if stock > 0:
#                             raise ValueError
#                     except:
#                         print("Don't allow Negative Value")

#----------------Display product list by location   (gfroup by location)-----------------------------------

for l in l_list:
    for m in move_list:
        if l.name:
            print(l.name)
            break
        
            
        
# for p in p_list:
#     new_dict = {}
    
#     if p.name:
#         #print(p.name)
#         for m in move_list:
#             print()
#             if p.name == m.product.name:
#                 new_dict.update({"Location name":m.to_location,"Product name":m.product.name})
#                 print(new_dict)

# p1.disp()
# p2.disp()
# p3.disp()
# p4.disp()
# p5.disp()