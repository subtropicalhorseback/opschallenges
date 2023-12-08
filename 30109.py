#Create if statements using these logical conditionals below. Each statement 
#     should print information to the screen depending on if the condition is met.
#
#    Equals: a == b
#    Not Equals: a != b
#    Less than: a < b
#    Less than or equal to: a <= b
#    Greater than: a > b
#    Greater than or equal to: a >= b
#Create an if statement using a logical conditional of your choice and include 
#     elif keyword that executes when other conditions are not met.
#Create an if statement that includes both elif and else to execute when both if 
#     and elif are not met.


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

if num1 == num2:
    print("That's the same number")

if num1 != num2:
    print("Good job, those are two different numbers")

if num1 < num2:
    print("Your first number",num1,"is less than your second number",num2)

if num1 <= num2:
    print("Your first number",num1,"is less than or equal to your second number",num2)

if num1 > num2:
    print("Your first number",num1,"is greater than your second number",num2)

if num1 >= num2:
    print("Your first number",num1,"is greater than or equal to your second number",num2)

num3 = (num1 + num2)
if num3 > 1000:
    print("Those are some big numbers")
elif num3 > 100:
    print("Those are good-sized numbers")
else:
    print("Thanks for making the math easier")
