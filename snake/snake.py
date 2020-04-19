# imports
from point import MAX_HEIGHT, MAX_WIDTH, Point

# class Snake
class Snake:
    # init
    def __init__(self):
        self.head = Point(MAX_WIDTH / 2, MAX_HEIGHT / 2, "r")
        self.body = [self.head]

    # move snake
    def move(self):
        body_len = len(self.body)

        for i in range(body_len, 0, -1):
            i = i - 1
            if i == 0:
                self.body[i].move()
            else:
                self.body[i].x = self.body[i-1].x
                self.body[i].y = self.body[i-1].y

    # change direction
    def change(self, key):
        if key == 258:
            self.head.direction = "d"
        elif key == 259:
            self.head.direction = "u"
        elif key == 260:
            self.head.direction = "l"
        elif key == 261:
            self.head.direction = "r"
        else:
            pass

    def grow(self):
        next_point = {"x" : None, "y" : None, "d" : self.body[-1].direction}

        if self.head.direction == "d":
            next_point["x"] = self.body[-1].x
            next_point["y"] = self.body[-1].y - 1
        elif self.head.direction == "u":
            next_point["x"] = self.body[-1].x
            next_point["y"] = self.body[-1].y + 1
        elif self.head.direction == "r":
            next_point["x"] = self.body[-1].x - 1
            next_point["y"] = self.body[-1].y
        elif self.head.direction == "l":
            next_point["x"] = self.body[-1].x + 1
            next_point["y"] = self.body[-1].y
        else:
            pass

        self.body.append(Point(next_point["x"], next_point["y"], next_point["d"]))
