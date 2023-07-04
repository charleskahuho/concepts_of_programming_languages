#implicit coercion
num_int = 4  
num_float = 3.2
sum = num_float + num_int # integer is automatically converted to float and summed
print(sum)

#explicit coercion
num_str = "14"
num_int = int(num_str) #  the user defines the datatype the variable is to be converted to
print(num_int)

num_float= float(num_int)
print(num_float)
