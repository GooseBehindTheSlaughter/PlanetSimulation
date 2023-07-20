import pygame
import config
from planet import Planet, findIncrement

# Finds the correct increment based on how many seconds it takes to rotate the sun


# Converts the current time into the angle
def TimeToAngle(custom_time):
    # Calculate the elapsed time since the start of the day in seconds
    elapsed_time = custom_time.hour * 3600 + custom_time.minute * 60 + custom_time.second

    # Calculate the fraction of the Earth's rotation completed
    rotation_fraction = elapsed_time / (23 * 3600 + 56 * 60 + 4)

    # Calculate the rotation angle in degrees
    rotation_angle = rotation_fraction * 360

    # Adjust the rotation angle to be within the range of 0 to 360 degrees
    rotation_angle = rotation_angle % 360

    return rotation_angle



pygame.init()

# Set up the display window
screen = pygame.display.set_mode(config.WIN_SIZE)
clock = pygame.time.Clock()

# Setting up the planets increments
moonAroundEarth = findIncrement(86400) # Seconds in a day
earthAroundSun = findIncrement(31536000) # Seconds in a year

# Setting up the planets
sun = Planet(screen, config.CENTER, 50, config.YELLOW)
earth = Planet(screen, config.CENTER, 25, config.BLUE)
moon = Planet(screen, config.CENTER, 15,config.GRAY)

# rotate them around the center (sun)
earth.rotateAround(config.CENTER, 250, increment=earthAroundSun, drawOrbit= True, orbitColour=config.GRAY)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill screen
    screen.fill((56,56,56))

    # update the positions of the planets
    earth.update()
    moon.update()
    sun.update()

    # if the object were rotating around is moving we have to move rotate to the loop
    moon.rotateAround(earth.position, 50, moonAroundEarth, True, config.GRAY) 




    # update the display and fix it to the fps
    pygame.display.update()
    clock.tick(config.MAXFPS)

pygame.quit()
