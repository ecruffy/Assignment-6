# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)


import random

# Create the 10 questions using random integers and if-else statements
def questionOne():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionTwo():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionThree():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionFour():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionFive():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionSix():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionSeven():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionEight():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionNine():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

def questionTen():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input(f"{first} + {second} = "))
    if answer == calculation:
        return 1
    else:
        return 0

# Display the scores. I added if else statements to give remarks to the user.
def displayOutput(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    totalScore = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    if totalScore <= 5:
        print(f"Your score is {totalScore}/10. Better luck next time.")
    elif totalScore > 5 and totalScore <= 7:
        print(f"Your score is {totalScore}/10. Try a bit harder!")
    else:
        print(f"Your score is {totalScore}/10. GOOD JOB!")

question1 = questionOne()
question2 = questionTwo()
question3 = questionThree()
question4 = questionFour()
question5 = questionFive()
question6 = questionSix()
question7 = questionSeven()
question8 = questionEight()
question9 = questionNine()
question10 = questionTen()

displayOutput(question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)