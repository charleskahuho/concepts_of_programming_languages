class Point: # creating a class called point
    def __init__(self, x, y): # line initiates the class defination fot the point class self represents the instance for the class itself. x &y used to intialize the attributes of the object
        #cunstructor(__init method__) 
        self.x = x
        self.y = y
# this method is used to overload + operator for the class
#self represents the first point 'point1' and other represents the other point 'point2'
#this method creates anew point by adding x&y cordinates of the two points
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(p3.x)  # 4
print(p3.y)  # 6