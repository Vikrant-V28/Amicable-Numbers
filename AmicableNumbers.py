import math


def divSum(n):
    result = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (i == int(n/i)):
                result = result + i
            else:
                result = result + (i + int(n/i))
    return (result + 1)


def amicable(x, y):
    if (divSum(x) != y):
        return False
    return(divSum(y) == x)


# Driven code
x = 220
y = 284
if (amicable(x, y)):
    print("True")
else:
    print("False")
