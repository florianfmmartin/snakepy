# imports
import blessed
import random
from point import Point

# app
app = blessed.Terminal()

# constants
MAX_WIDTH = app.width
MAX_HEIGHT = app.height

# class Food
class Food:
    # init
    def __init__(self):
        x = random.choice(range(0, MAX_WIDTH))
        y = random.choice(range(0, MAX_HEIGHT))
        self.pos = Point(x, y, None)

    def change(self):
        x = random.choice(range(0, MAX_WIDTH))
        y = random.choice(range(0, MAX_HEIGHT))
        self.pos.x = x
        self.pos.y = y
