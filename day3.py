f = open('day3.txt')
count = 0
sum = [0]*12
for line in f:
    count += 1
    digits = [int(a) for a in line.strip()]
    sum = [a + b for a,b in zip(sum,digits)]
sum = [round(a/count) for a in sum]
gamma = int(''.join([str(a) for a in sum]),2)
epsilon = int(''.join([str(1-a) for a in sum]),2)
print(gamma, epsilon, gamma*epsilon)