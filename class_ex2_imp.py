

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
        self.stock_at_location= []
        
        
    
    def disp(self):
        print(self.name,self.code,self.category.category_name, self.price,self.stock_at_location)


# --------------Create Category Class Object---------------------
c4 = Category("Vehicle",101)
c1 = Category("Car",103)
c2 = Category("Bike", 104)
c3 = Category("Bicycle",106)


# ---------------Create Product Class Object------------------------
p1 =Product("Verna", "AE10234" , c1 , 1500000 )
p2 =Product("Hond city" , "AS9874" , c1 , 1600000)
p3 =Product("i20" , "ADC2365" , c1 , 900000)
p4 =Product("Hond" , "AWD5697" , c2 , 45000)
p5 =Product("Activa" , "AZX2589" , c2 , 80000)

c1.show()
c2.show()
c3.show()
c4.show()

p1.disp()
p2.disp()
p3.disp()
p4.disp()
p5.disp()


my_list = [p1,p2,p3,p4,p5]
cat_list = [c1,c2,c3,c4]   



for i in l_list:
    print(i)
    sal = []
    if i.name:
        print(i.name,i.code)
        for m in move_list:
            if i.name == m.to_location:
                print(m.to_location,m.product)
                sal.append(m.to_location ," + " ,m.product)
    print()
    i.stock_at_location=sal 

