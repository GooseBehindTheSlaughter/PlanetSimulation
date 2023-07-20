import pygame
import math
import config

class Planet:
    def __init__(self, screen, startingPos:tuple, radius:float, colour:tuple):
        self.position = startingPos
        self.screen = screen
        self.radius = radius
        self.colour = colour
        self.drawOrbit = False
        self.orbitColour = (0,0,0)

        # Vars used for orbits
        self.angle = 0
        self.rotate = False
        pass

    def setPosition(self,position:tuple):
        self.position = position

    def setColour(self,colour:tuple):
        self.colour = colour

    def setRadius(self,radius:float):
        self.radius = radius

    def update(self):
        # if were drawing the orbit and were rotating
        if self.drawOrbit and self.rotate:
            pygame.draw.circle(self.screen,self.orbitColour,config.CENTER,self.rotateDistance, width=1)
            pass


        if self.rotate:
            # rotate the planet around the a set point (self.rotatePos which is set when we call self.rotateAround)
            rotated_angle = math.radians(self.angle)
            rotated_x = int(self.rotatePos[0] + self.rotateDistance * math.cos(rotated_angle))
            rotated_y = int(self.rotatePos[1] - self.rotateDistance * math.sin(rotated_angle))

            self.angle += self.rotateIncrement

            self.position = (rotated_x,rotated_y)

            pygame.draw.circle(self.screen, self.colour, (rotated_x, rotated_y), self.radius)

        else:
            # if were not rotating around the point use this
            # Draw the planet
            pygame.draw.circle(self.screen, self.colour, self.position, self.radius)



    def rotateAround(self ,pos:float ,distance:float ,increment:float = 5, drawOrbit:bool = False, orbitColour = None):
        self.rotate = True
        self.angle = 0 + self.angle
        self.rotateIncrement = increment
        self.rotatePos = pos
        self.rotateDistance = distance
        self.drawOrbit = drawOrbit
        self.orbitColour = orbitColour

        # max the angle
        if self.angle > 360: self.angle = 0
        pass

    def stopRotate(self):
        self.rotate = False


def findIncrement(time: int):
    fps = config.MAXFPS
    angle_increment = 360 / time / fps  # Angle increment per second
    return angle_increment