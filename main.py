import math
import numpy
import random
import tkinter


box = tkinter.Tk()
box.wm_title("python-n-body")

canvas = tkinter.Canvas(box, width=800, height=600, bg="black")
canvas.grid(row=0, column=0)

G = 0.01
Bodies = []


class Body:
    def __init__(self, mass, x, y, v):
        self.Mass = mass
        self.X = x  # todo: are x and y needed?
        self.Y = y
        self.LocationArray = numpy.array([self.X, self.Y], dtype='float')
        self.V = numpy.array(v, dtype='float')
        # self.dV = 0
        self.Size = 10.0

    def gravforce(self, otherbody):
        distance = math.sqrt((otherbody.X - self.X) ** 2 + (otherbody.Y - self.Y) ** 2)
        force = -G * ((self.Mass * otherbody.Mass) / abs(distance) ** 2) * ((self.LocationArray - otherbody.LocationArray) / distance)
        dv = force / self.Mass

        self.V = self.V + dv

        # border bounce
        if self.LocationArray[0] < 0 + self.Size / 2 or self.LocationArray[0] > canvas.winfo_width() - self.Size / 2:
            self.V[0] = self.V[0] * -0.5
        if self.LocationArray[1] < 0 + self.Size / 2 or self.LocationArray[1] > canvas.winfo_height() - self.Size / 2:
            self.V[1] = self.V[1] * -0.5


BodyCount = 10
for i in range(0, BodyCount):
    Bodies.append(Body(random.randrange(10, 500), random.randrange(50, 650), random.randrange(50, 650),
                       [random.randrange(-10, 10) / 20, random.randrange(-10, 10) / 20]))


T = 0
while T < 10000:
    T += 1
    canvas.delete("all")
    for firstBody in Bodies:
        for secondBody in Bodies:
            if firstBody != secondBody:
                firstBody.gravforce(secondBody)
                firstBody.LocationArray += firstBody.V

                canvas.create_oval(firstBody.LocationArray[0] - firstBody.Size,
                                   firstBody.LocationArray[1] - firstBody.Size,
                                   firstBody.LocationArray[0] + firstBody.Size,
                                   firstBody.LocationArray[1] + firstBody.Size,
                                   outline="white",
                                   fill="blue",
                                   width=2)
        canvas.update()

box.mainloop()
