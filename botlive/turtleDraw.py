import turtle
# from random import randrange
# from time import sleep


class Bixinho:
    def __init__(self):
        self.screen = turtle.Screen()
        self.bug = turtle.RawTurtle(self.screen)
        self.bug.pensize(5)
        self.bug.shape('turtle')

    def walk(self, direction, distance):
        if 0 < direction < 360 and 0 < distance <= 50:
            self.bug.right(direction)
            self.bug.forward(distance)

    def color(self, color):
        self.bug.color(color)

    def stop(self):
        self.screen.bye()
