import turtle
import time

times = 0

while True:
    turtle.forward(130 - times)
    turtle.right(300)
    turtle.backward(200)
    times += 1
    time.sleep(1)
