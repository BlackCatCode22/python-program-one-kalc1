# pythonChapterThree.py
#
# Note: This program is sample code and is not an approved solution. This program is imcomplete. Use this code to
# guide your coding experience for this assignment.
#
# Programmer Name: Dennis Mohle
# Date: 8/10/23
#
# Demonstrate the Python programming concepts in Cengage module (chapter) three by...
#
# Writing the "largest of three" program in Python using one nested if statement, a compound if statement, and
# another solution from ChatGPT
#    use int, string, double, and bool variable types
#    demonstrate primitive variable usage by getting and displaying user name, outputting the quotient of the first
#    input number by the second input number
#    display, print(), the types of all variables used in the program
#
print("\n Welcome to the Largest of Three program!\n")
#
# Variable Declaration Section
#
# int variables:
num1 = 0
num2 = 0
num3 = 0
largest_num = 0

# string variables:
user_name = ""

# double variables
result_of_division = 0.0

# bool variables
play_again = False

print("\n num1 is of type: " + str(type(num1)))
print("\n user_name is of type: " + str(type(user_name)))
# TODO: Output the types of the variables: result_of_division and play_again.
print("result_of_division is of type:", str(type(result_of_division)))
print("play_again is of type:", str(type(play_again)))

# Get three integers from the user.
num1 = input("\n Please enter the first whole (integer) number: ")
print("\n num1 = " + num1)
# TODO: get two more ints from the user
num2 = input(" Please enter a second whole (integer) number: ")
print(" num2 = " + num2)

num3 = input(" Please enter a third whole (integer) number: ")
print(" num3 = " + num3)
# TODO: examine the type of num1, num2, and num3. why/how did the data type change from int to str?
# It was inputted from the user
# TODO: Get the data types of num1, num2, and num3 back to int so you can compare values.
int(num1)
int(num2)
int(num3)

# Get the user's name.
# TODO: get and print() the user's name
user_name = input("Hello, please enter your name: ")
print("Welcome, " + user_name + "!")

a_num1 = 11
a_num2 = 44
a_num3 = 22

# Example solution using a nested if statement
if (a_num1 > a_num2):
    if (a_num1 > a_num3):
        largest_num = a_num1
    else:
        largest_num = a_num3
else:
    if (a_num2 > a_num3):
        largest_num = a_num2
    else:
        largest_num = a_num3

print("\n\n Largest of three is: " + str(largest_num))

# TODO: Code up a nested-if statement solution after making num1, num2, and num3 proper data types to work
# with arithmetic operators
if num1 > num2:
    if num1 > num3:
        largest_of_three = num1
    else:
        largest_of_three = num3
else:
    if num2 > num3:
        largest_of_three = num2
    else:
        largest_of_three = num3

print("The largest of three is: " +str(largest_of_three))


# TODO: Code up a solution using compound if statements (use the 'and' operator)
# Example compound if statement:
n1 = 4
n2 = 5
n3 = 3
n4 = 4
if (n1 < n2) and (n1 < n3):
    print("\n\n" + str(n1) + " is smallest.")
else:
    print("\n\n" + str(n1) + " is not smallest.")

if num1 > num2 and num1 > num3:
    print(str(num1) + " is the largest of three")
if num2 > num1 and num2 > num3:
    print(str(num2) + " is the largest of three")
if num3 > num1 and num3 > num2:
    print(str(num3) + " is the largest of three")





# TODO: Code up a solution from ChatGPT
# The following is the response I got from ChatGPT:

# Get user name
user_name = input("Please enter your name: ")

# Get three input numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the largest of three numbers
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# Calculate the quotient of the first number by the second number
quotient = num1 / num2

# Display user name
print("Hello,", user_name)

# Display the quotient
print("Quotient of", num1, "divided by", num2, "is:", quotient)

# Display the largest number
print("The largest of the three numbers is:", largest)

# Print the types of variables
print("Variable types:")
print("user_name is of type:", type(user_name))
print("num1 is of type:", type(num1))
print("num2 is of type:", type(num2))
print("num3 is of type:", type(num3))
print("largest is of type:", type(largest))
print("quotient is of type:", type(quotient))
