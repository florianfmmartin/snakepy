# imports
from terminal import Term
from snake import Snake
from food import Food

# app
terminal = Term()
app = terminal.term

# constants
MAX_WIDTH = app.width
MAX_HEIGHT = app.height

# create snake
snake = Snake()

# snake speed
speed = 0.1

# grow counter
counter = 1

# txt
txt_erase = app.home + app.blue_on_black + app.clear

# food
food = Food()

# with
with app.cbreak(), app.hidden_cursor():
    # clear screen
    print(txt_erase)

    # input key
    val = ""

    # app loop
    while val != "q":
        val = app.inkey(timeout = speed)

        # change direction
        snake.change(val.code)

        # move or not
        snake.move()

        # clear point
        print(app.move(snake.head.y, snake.head.x) + " ")

        # print erase
        print(txt_erase,  end="", flush=True)

        # print snake
        for part in snake.body:
            print(app.move(part.y, part.x) + "█",  end="", flush=True)

        # print food
        print(app.move(food.pos.y, food.pos.x) + app.red_on_black + "@", end="", flush=True)

        # food eaten?
        if snake.head.x == food.pos.x and snake.head.y == food.pos.y:
            food.change()
            for i in range(0, int(counter)):
                snake.grow()
            speed += -0.0005
            counter = counter * 1.15

        # collision ?
        body_len = len(snake.body)

        for i in range(0, body_len):
            if i != 0:
                if snake.head.x == snake.body[i].x and snake.head.y == snake.body[i].y:
                    val = "q"
