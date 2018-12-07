#*******************************#
#Title: Error Handling Script
#Dev: CBenner
#Date: Dec 6th, 2018
#ChangeLog: (Who, When, What)
#None Yet
#*******************************#

#Some simple code to demonstrate error handling#

strNumber1 = float(input("Enter the first number: ")) #This line of code asks for the first user input
strNumber2 = float(input("Enter the second number: ")) #This line of code asks for the second user input

def quotient(x,y):
    try: #This is the try clause
        result = x//y
        print("Yes, your answer is :", result)
    except ZeroDivisionError: ##This is the except clause
        print("Whoops! You are dividing by zero - which is undefined")

quotient(strNumber1,strNumber2)



