import turtle
# from random import randrange
# from time import sleep


class Chegada:
    def __init__(self):
        self.screen = turtle.Screen()
        self.bug = turtle.RawTurtle(self.screen)
        self.bug.shape('turtle')
        self.bug.pensize(0)
        self.bug.penup()
        self.bug.goto(-350, 400)
        self.bug.pendown()
        self.bug.right(90)
        self.bug.forward(800)
        self.bug.penup()
        self.bug.goto(200, 0)




    def walk(self, direction, distance):
        self.bug.right(direction)
        self.bug.forward(distance)
        # if direction > 360 or distance > 20:
        #     return
        coordx = round(self.bug.xcor(), 1)
        # coordy = round(self.bug.ycor(), 1)
        print(coordx)
        if coordx < -350:
            self.bug.goto(200, 0)
            for x in range(5):
                self.bug.goto(0,0)
                self.bug.circle(50)
                self.bug.circle(60)



    def color(self, color):
        self.bug.color(color)

    def stop(self):
        self.screen.bye()
