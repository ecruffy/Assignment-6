# Create a program that ask for 4 numbers
# Print the number from highest to lowest using only if-else statement

print("This is a program that sorts 4 numbers from highest to lowest")

def userInput():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    number4 = float(input("Enter the last number: "))
    return number1, number2, number3, number4,

num1, num2, num3, num4,= userInput()

# find the highest number
def highestNumber():
    if num1 > num2 and num1 > num3 and num1 > num4:
        return num1
    elif num2 > num3 and num2 > num4:
          return num2
    elif num3 > num4:
        return num3
    else:
        return num4

highest = highestNumber()

# find the second highest number
def secondHighestNumber():
    if num1 == highest:
        if num2 > num3 and num2 > num4:
            return num2
        elif num3 > num4:
            return num3
        else:
            return num4
    if num2 == highest:
        if num1 > num3 and num1 > num4:
            return num1
        elif num3 > num4:
            return num3
        else:
            return num4
    if num3 == highest:
        if num1 > num2 and num1 > num4:
            return num1
        elif num2 > num4:
            return num2
        else:
            return num4
    if num4 == highest:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num3:
            return num2
        else:
            return num3

second = secondHighestNumber()
    
# find the lowest number
def lowestNumber():
    if num1 < num2 and num1 < num3 and num1 < num4:
        return num1
    elif num2 < num3 and num2 < num4:
          return num2
    elif num3 < num4:
        return num3
    else:
        return num4

lowest = lowestNumber()

# find the second lowest number
def secondLowestNumber():
    if num1 == lowest:
        if num2 < num3 and num2 < num4:
            return num2
        elif num3 < num4:
            return num3
        else:
            return num4
    if num2 == lowest:
        if num1 < num3 and num1 < num4:
            return num1
        elif num3 < num4:
            return num3
        else:
            return num4
    if num3 == lowest:
        if num1 < num2 and num1 < num4:
            return num1
        elif num2 < num4:
            return num2
        else:
            return num4
    if num4 == lowest:
        if num1 < num2 and num1 < num3:
            return num1
        elif num2 < num3:
            return num2
        else:
            return num3

third = secondLowestNumber()

# print results
print(f"descending order: {highest},{second},{third},{lowest}")