import math
class Person:

    def __init__(self, x, y):
        if ( isinstance(x, float) or isinstance(x,int) ) and ( isinstance(y, float) or isinstance(y, int)):
            self.x = x
            self.y = y
        else:
            raise TypeError('x and y should be numbers')

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

if __name__ == "__main__":
    try:
        p = Person(8,6)
        print(p.distance())
    except TypeError as e:
        print(e)