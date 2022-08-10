

class Category(object):

    def __init__(self, category_name, code):
        self.category_name=category_name
        self.code=code        
        self.no_of_products = 0        

            
    def show(self): 
        print(self.category_name,self.code,self.no_of_products)

        
class Product(Category):
    
    def __init__(self,  name, code, category, price):
        self.name=name
        
        self.code=code
        self.category = category
        
        category.no_of_products = category.no_of_products + 1
        self.price=price
        
    
    def disp(self):
        print(self.name,self.code,self.category.category_name, self.price)


c1 = Category("Car",103)
c2 = Category("Bike", 104)
c3 = Category("Bicycle",106)

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

c1.show()
c2.show()
c3.show()

print("--------------------------------------------------")


my_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
c = Category(my_list)
print(c.code)


c1.show()
for i in range(0, len(my_list)): 
    if my_list[i].category.category_name == "Car":
        print()
        print(my_list[i].name,my_list[i].code,my_list[i].category.category_name,my_list[i].price, end=" ")  
        print()
print("------------------------------------------------------")
c2.show()
for i in range(0, len(my_list)): 
    if my_list[i].category.category_name == "Bike":
        print()
        print(my_list[i].name,my_list[i].code,my_list[i].category.category_name,my_list[i].price, end=" ")  
        print()
print("------------------------------------------------------")
c3.show()
for i in range(0, len(my_list)): 
    if my_list[i].category.category_name == "Bicycle":
        print()
        print(my_list[i].name,my_list[i].code,my_list[i].category.category_name,my_list[i].price, end=" ")  
        print()





temp = 0
print("Elements of original array: ");    
for i in range(0, len(my_list)):    
    print(my_list[i].name,my_list[i].code,my_list[i].category.category_name,my_list[i].price, end=" ")  
    print() 

for i in range(0, len(my_list)):    
    for j in range(i+1, len(my_list)):    
        if(my_list[i].price > my_list[j].price):
            temp = my_list[i]  
            my_list[i] = my_list[j]
            my_list[j] = temp  
             
print("---------------------------------------------------")
print("Elements of array sorted in ascending order: ")    
for i in range(0, len(my_list)):    
    print(my_list[i].name,my_list[i].code,my_list[i].category.category_name,my_list[i].price, end=" ")
    print()

print("Element of list in descending")
for i in range(len(my_list)-1,0,-1):
    print(my_list[i].name,my_list[i].code,my_list[i].price)


enter_code=input("choose code in above : ")
flag = False
for c in my_list:
    if (enter_code == c.code):
        print(c.name,c.code,c.category.category_name,c.price)
        flag = True

if not flag:
    print("code is not available")
   


