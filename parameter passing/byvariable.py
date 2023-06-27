#variables themselves are not directly passed but the values of the variables are passed
#similar to pass by value
def change_variable(variable):
    variable.append(3)
    variable.append(4)

my_list = [1, 2]
change_variable(my_list)
print(my_list)  
