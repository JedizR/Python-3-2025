import time
import os

class Circle:
    def __init__(self, radius, x, y, start_direction, space_x, space_y):
        self.radius = radius
        self.x = x
        self.y = y
        self.direction = start_direction   
        self.space_x = space_x
        self.space_y = space_y
           
    def draw(self):
        print(f"{self.x} {self.y}")
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_by_direction(self):
        #Direction: 1 - E, 2 - NE, 3 - N, 4 - NW, 5 - W, 6 - SW, 7 - S, 8 - SE
        #Border: line((0,0),(0,10)) line((0,0),(10,0)) line((0,10),(10,10)) line((10,0),(10,10))
        if self.y == 0 and self.x == 0 and self.direction == 4:
            self.direction = 8
        elif self.y == 0 and self.x == self.space_x - 1 and self.direction == 6:
            self.direction = 2
        elif self.y == self.space_y - 1 and self.x == 0 and self.direction == 2:
            self.direction = 6
        elif self.y == self.space_y - 1 and self.x == self.space_x - 1 and self.direction == 8:
            self.direction = 4
        elif self.x == 0 and self.y != 0 and self.y != 9:
            if self.direction == 2:
                self.direction = 8
            elif self.direction == 3:
                self.direction = 7
            elif self.direction == 4:
                self.direction = 6
        elif self.y == 0 and self.x != 0 and self.x != 9:
            if self.direction == 4:
                self.direction = 2
            elif self.direction == 5:
                self.direction = 1
            elif self.direction == 6:
                self.direction = 8
        elif self.x == self.space_x - 1 and self.y != 0 and self.y != 9:
            if self.direction == 6:
                self.direction = 4
            elif self.direction == 7:
                self.direction = 3
            elif self.direction == 8:
                self.direction = 2
        elif self.y == self.space_y - 1 and self.x != 0 and self.x != 9:
            if self.direction == 8:
                self.direction = 6
            elif self.direction == 1:
                self.direction = 5
            elif self.direction == 2:
                self.direction = 4
        
        
        if self.direction == 1:
            self.move(0,1)
        if self.direction == 2:
            self.move(-1,1)
        if self.direction == 3:
            self.move(-1,0)
        if self.direction == 4:
            self.move(-1,-1)
        if self.direction == 5:
            self.move(0,-1)
        if self.direction == 6:
            self.move(1,-1)
        if self.direction == 7:
            self.move(1,0)
        if self.direction == 8:
            self.move(1,1)
            
    def plot(self):
        for i in range(self.space_x):
            for j in range(self.space_y):
                if i == self.x and j == self.y:
                    print("*", end="")
                else:
                    print(".", end="")
            print("")
                            
class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
                
if __name__ == "__main__":    
    os.system('clear')  
    circle1 = Circle(1, 8, 4, 8, 10, 20) # Circle(radius, start_x, start_y, display_height, display_width)
    while(True):
        os.system('clear')
        circle1.plot()
        circle1.move_by_direction()
        time.sleep(0.2)
    
    
    