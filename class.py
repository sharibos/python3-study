# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius = 3, color = 'blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
RedCircle = Circle(10, 'red')
dir(RedCircle)