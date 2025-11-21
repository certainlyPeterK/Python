mass = [14, -6, 3, 11, 6, 8,5, 99, -20, -6, 10, 40, 0.25, -4, 5]
newMass = []
for num in mass:
    if num > 0:
        newMass.append(num)
mass = newMass
mass.sort(reverse=True)
