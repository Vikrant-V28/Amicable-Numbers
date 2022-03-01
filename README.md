<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/153715486-5da59ace-7f32-4f79-a365-318102feed51.png">
</div>

# Amicable Numbers

Amicable numbers are two different numbers related in such a way that the sum of the proper divisors of each is equal to the other number. The smallest pair of amicable numbers is (220, 284).

### Python Script
```python
import math
def divSum(n):
    result = 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (i == int(n/i)):
                result = result + i
            else:
                result = result + (i + int(n/i))
    return (result +1)

def amicable (x,y):
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
```

### Output:
`True`
