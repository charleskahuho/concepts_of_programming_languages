# a function can modify the original variable directly
#when you pass an object by refrernce a copy of the reference is passed by value 
#modifications will be refrected outside the function but reassigning the parameter will not affect the original reference
 
def change_list(lst):
    lst.append(3)

my_list = [1, 2]
change_list(my_list)
print(my_list)  
