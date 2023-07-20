import math

semi_major_axis_mars = 1.524  # Semi-major axis of Mars' orbit in AU

orbital_period_mars = math.sqrt(semi_major_axis_mars**3)

print("Orbital period of Mars:", orbital_period_mars, "years")
