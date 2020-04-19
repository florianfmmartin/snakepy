# imports
import blessed

# app
app = blessed.Terminal()

# constants
MAX_WIDTH = app.width
MAX_HEIGHT = app.height

# class Point
class Point:
    # init
    def __init__(self, x, y, d):
        self.x = int(x % MAX_WIDTH)
        self.y = int(y % MAX_HEIGHT)
        self.direction = "r"

    # move lrud
    def move(self, direction=None):
        if direction == None:
            direction = self.direction
        else:
            pass
        
        if direction == "l":
            self.x += -1
        elif direction == "r":
            self.x += 1
        elif direction == "d":
            self.y += 1
        elif direction == "u":
            self.y += -1
        else:
            pass
        self.x = int(self.x % MAX_WIDTH)
        self.y = int(self.y % MAX_HEIGHT)
