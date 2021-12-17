f = open('day2.txt')
horiz = 0
depth = 0
for line in f:
    a,b = line.split()
    b = int(b)
    if a == "forward":
        horiz += b
    if a == "down":
        depth += b
    if a == "up":
        depth -= b
print(horiz*depth)

f = open('day2.txt')
horiz = 0
depth = 0
aim = 0
for line in f:
    a,b = line.split()
    b = int(b)
    if a == "forward":
        horiz += b
        depth += (aim*b)
    if a == "down":
        aim += b
    if a == "up":
        aim -= b
print(horiz*depth)