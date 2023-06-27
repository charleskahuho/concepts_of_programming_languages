#supports primitive data types like variables booleans and floats
# a copy of the variable called to the function
#a change in the function does not affect the original variable
def change_value(x):
    x = 2
    return x

value = 1
change_value(value)
print(value)  
