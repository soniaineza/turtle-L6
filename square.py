import turtle
turtle.Screen().bgcolor("orange")
sc = turtle.Screen()
sc.setup(300,400)
turtle.title("welcome to turtle")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1
turtle.done()