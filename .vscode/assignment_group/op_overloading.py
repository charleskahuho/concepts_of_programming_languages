class Point: # creating a class called point
    def __init__(self, x, y): # line initiates the class defination fot the point class
        #cunstructor(__init method__)
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(p3.x)  # 4
print(p3.y)  # 6