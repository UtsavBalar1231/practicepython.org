import random as rd


def cows_and_bulls(x):
    y = int(input("Enter a 4 digit number: "))
    a = []
    [a.append(i) for i in str(y)]
    b = []
    [b.append(i) for i in str(x)]

    cows = 0
    bulls = 0
    for i, j in zip(a, b):
        if (i == j):
            cows += 1
        else:
            bulls += 1
    print(f'{cows} cows, {bulls} bulls')
    return cows, bulls


x = rd.randint(1000, 9999)

cows, bulls = cows_and_bulls(x)
while bulls != 0:
    cows, bulls = cows_and_bulls(x)
