"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-20, 19) * 10
        ##Cambie los valores para permitir que se mueva por todo el tablero
        food.y = randrange(-20, 19) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        numcol = randrange(1,5)
        if numcol == 1:
            square(body.x, body.y, 9, 'black')
            square(food.x, food.y, 9, 'green')
        if numcol == 2:

            square(body.x, body.y, 9, 'green')
            square(food.x, food.y, 9, 'blue')
        if numcol == 3:

            square(body.x, body.y, 9, 'yellow')
            square(food.x, food.y, 9, 'purple')
        if numcol == 4:

            square(body.x, body.y, 9, 'blue')
            square(food.x, food.y, 9, 'yellow')
        if numcol == 5:

            square(body.x, body.y, 9, 'purple')
            square(food.x, food.y, 9, 'black')

    update()   #se modifica la velocidad, a más puntos menos velocidad
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
