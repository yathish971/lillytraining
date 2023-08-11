inner_planets = ('Mercury', 'Venus', 'Earth', 'Mars') 
outer_planets=('Jupiter', 'Saturn', 'Uranus','Neptune')

# Concatenate inner and outer planets
planets=inner_planets+outer_planets
print(planets)

# Access individual planets by indexing, display giant planets
print(outer_planets[0])

# Iterate over the planets and display information
for x in planets:
    print(x)

# Try to modify the tuple(This should throw an error)


# Convert the tuple to a list for modification
List_planets = list(planets)

# Modify a planet's name
List_planets[2]="Kripton"

# Convert the list back to a tuple
planets=tuple(List_planets)

# Display the updated tuple of planetary data
print(planets)