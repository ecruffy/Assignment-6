# Create a program that ask for 4 numbers
# Print the number from highest to lowest using only if-else statement

print("This is a program that sorts 4 numbers from highest to lowest")

def userInput():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the last number: "))
    return num1, num2, num3, num4,

a, b, c, d,= userInput()

# find the highest number
def highestNumber():
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
          return b
    elif c > d:
        return c
    else:
        return d

highest = highestNumber()

# find the second highest number
def secondHighestNumber():
    if a == highest:
        if b > c and b > d:
            return b
        elif c > d:
            return c
        else:
            return d
    if b == highest:
        if a > c and a > d:
            return a
        elif c > d:
            return c
        else:
            return d
    if c == highest:
        if a > b and a > d:
            return a
        elif b > d:
            return b
        else:
            return d
    if d == highest:
        if a > b and a > c:
            return a
        elif b > c:
            return b
        else:
            return c

second = secondHighestNumber()
    
# find the lowest number
def lowestNumber():
    if a < b and a < c and a < d:
        return a
    elif b < c and b < d:
          return b
    elif c < d:
        return c
    else:
        return d

lowest = lowestNumber()

# find the second lowest number
def secondLowestNumber():
    if a == lowest:
        if b < c and b < d:
            return b
        elif c < d:
            return c
        else:
            return d
    if b == lowest:
        if a < c and a < d:
            return a
        elif c < d:
            return c
        else:
            return d
    if c == lowest:
        if a < b and a < d:
            return a
        elif b < d:
            return b
        else:
            return d
    if d == lowest:
        if a < b and a < c:
            return a
        elif b < c:
            return b
        else:
            return c

third = secondLowestNumber()

# print results
print(f"descending order: {highest},{second},{third},{lowest}")