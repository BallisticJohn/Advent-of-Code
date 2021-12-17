f = open('day1.txt')
count = 0
last = 2**30
for line in f:
    depth = int(line)
    if depth > last:
        count += 1
    last = depth
print(count)

f = open('day1.txt')
count = 0
win = [2**30]*3
last = sum(win)
pos = 0
for line in f:
    win[pos] = int(line)
    current = sum(win)
    if current > last:
        count += 1
    last = current
    pos = (pos + 1) % 3
print(count)