class Rectangle :
    def __init__(self,lengh,width):
        self.lengh=lengh
        self.width=width

class Square(Rectangle):
    def __int__(self,lengh,width):
        super().__init__(lengh,width)
    def area(self):
        return self.lengh*self.width

class Cube(Rectangle):
    def __init__(self,hight,lengh, width):
        super().__init__(lengh, width)
        self.hight=hight
    def volume(self):    
        return self.lengh*self.width*self.hight

cube=Cube(2,3,4)
square=Square(4,5)

print(cube.volume())
print(square.area())
