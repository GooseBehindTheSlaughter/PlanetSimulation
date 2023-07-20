# PlanetSimulation

# Description 
This is a simple planet simulation using pygame that i made to learn how it worked, im pretty sure the math is correct but idk

# Usage 
You can easily add the rest of the planets and orbit times you'll just have to look at the planet class and see how i set them up
ill leave some simple instructions but nothing more, as i said this is my first time doing something like this so i proberly did 
everything the long way 🤷‍♂️

#Adding planet
```
from planet import Planet

# screen is obiously the pygame display
planet = Planet(screen, spawnOrigin, radius, colour)

# If you want the planet to rotate around a static point then just call it before you run the main loop

# Otherwise if you want it to rotate around a planet (moon for example) then it has to be called in the main loop

# Increment is how much you want it to rotate every frame, this should work with the frame rate but im not sure
planet.rotateAround(rotatePoint, distanceFromPoint, increment, drawOrbit)

# You call this in the main loop to draw the planet and update its rotatation if it has any
planet.update()
```

<br> If you want to update this then go ahead 
