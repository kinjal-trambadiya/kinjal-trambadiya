
class Category(object):

    def __init__(self, category_name, code,parent=None):
        self.category_name=category_name
        self.code=code
        self.parent=parent
        self.display_name=" "
        self.products=[]       
        self.no_of_products = 0

    def dis_name(self):
         if self.parent == None:
            self.display_name = self.category_name
            
         else:
            self.display_name= self.parent + " > " + self.category_name
         
    def show(self): 
        
        print(self.category_name,self.code,self.parent,self.no_of_products,self.display_name,self.products)

        
class Product(Category):
    
    def __init__(self, name, code, category, price):
        self.name=name
        self.code=code    
        self.category = category
        category.no_of_products = category.no_of_products + 1
        self.price=price
        
    def disp(self):
        print(self.name,self.code,self.category.category_name, self.price)

c4 = Category("Vehicle",101,None)
c1 = Category("Car",103, c4.category_name)
c2 = Category("Bike", 104, c4.category_name)
c3 = Category("Bicycle",106, c4.category_name)
# c4.dis_name()
# c3.dis_name()
# c2.dis_name()
# c1.dis_name()
print("--------------------------------------")

print("--------------------------------------")
p1 =Product("Verna", "AE10234" , c1 , 1500000 )
p2 =Product("Hond city" , "AS9874" , c1 , 1600000)
p3 =Product("i20" , "ADC2365" , c1 , 900000)
p4 =Product("Hond" , "AWD5697" , c2 , 45000)
p5 =Product("Activa" , "AZX2589" , c2 , 80000)
p6 =Product("Jupiter", "AVF7452" , c2 , 75000)
p7 =Product("Road bicycle" , "ASD9321" , c3 ,8000 )
p8 =Product("Mountain bicycle", "AHU6987", c3, 9000)
p9 =Product("Cargo bicycle" , "AWE5989" , c3 , 10000)

print("--------------------------------------------------")

cat_list = [c1,c2,c3,c4]
my_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]


# ---------------------------Arrange by Price         [Product Class]        ----------------------------

 # temp = 0
# print("Elements of original list: ");    
# for i in my_list:    
#     print(i.name,i.code,i.category.category_name,i.price, end=" ")  
#     print() 

# for i in range(0, len(my_list)):    
#     for j in range(i+1, len(my_list)):    
#         if(my_list[i].price > my_list[j].price):
#             temp = my_list[i]  
#             my_list[i] = my_list[j]
#             my_list[j] = temp  

# #------------------------Ascending Order      [Product Class]      -----------------------------

# print("---------------------------------------------------")
# print("Elements of array sorted in ascending order: ")    
# for i in my_list:  
#     print(i.name,i.code,i.category.category_name,i.price, end=" ")
#     print()

# ---------------------Desceding Order -----------------------------------------

# print("Element of list in descending order")
# for i in range(len(my_list)-1,0,-1):
#     print(my_list[i].name,my_list[i].code,my_list[i].price)

# # ---------------Enetr code for Product Category and display its details-   [Product Class]    -------------------------------------

# enter_code=input("choose code in above : ")
# flag = False
# for c in my_list:
#     if (enter_code == c.code):
#         print(c.name,c.code,c.category.category_name,c.price)
#         flag = True

# if not flag:
#     print("code is not available")
   
# # --------------------Display category with its code   [Category Class]     -------------------------------

# for c in cat_list:
#     if c.code:
#         print("\n ",c.code,c.category_name,c.display_name)
#         for i in my_list:  
#             if c.category_name == i.category.category_name:  
#                  print(i.name,i.code,i.price, end=" ")  

# -------===Display category with code  ---[Category class]---   &   Displaay Category Class member Products(List of All Product Object)----------
# ------------------------------In Display Category ---------def show()--------------------------------------------

for c in cat_list:
    p_list = []
    if c.code:
        #print("\n ",c.code,c.category_name,c.display_name)
        for i in my_list:  
            if c.category_name == i.category.category_name:  
                 print(i.name,i.code,i.price, end=" ")  
                 p_list.append(i.name)
            
        
    print()
    c.products = p_list


# # ------------------Ordered by category Name       [Category Class]         ------------------------------

# for i in range(0, len(my_list)):    
#     for j in range(i+1, len(my_list)):    
#         if(my_list[i].category.category_name > my_list[j].category.category_name):
#             temp = my_list[i]  
#             my_list[i] = my_list[j]
#             my_list[j] = temp  

# for i in my_list:
#     print(i.category.category_name,i.name,i.code,i.price)
#     print()

c1.show()
c2.show()
c3.show()
c4.show()
