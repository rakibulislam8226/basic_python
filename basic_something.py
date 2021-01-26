# if condition
i = 8
if i >= 5:
    print(" Subahanallah")

# if elif else condition
is_boy = True
is_tall = False  # using  boolean
if is_boy:
    print("you are a boy.")
else:
    print("you ain't a boy.")
if is_boy and is_tall:
    print("you are tall")
elif is_boy and not is_tall:
    print('you are a short boy')
elif not is_boy and is_tall:
    print('you are not a boy but tall')
else:
    print("you are neither male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num3 >= num3 and num2 >= num1:
        return num2
    else:
        return num3


print(max_num(300, 500, 350))

# simple calculator using if elif else
number1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))
if operator == "+":
    print("the sum is: " + str(number1 + number2))
elif operator == "-":
    print(number1 - number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "*":
    print(number1 * number2)
else:
    print("Invalid operator")

# for loop
i = 10
for i in range(1, 10, 2):
    print(f"{i} Allhamdulilla")

# for loop another
friends = ["rakib", "shakib", "tamim"]
for i in friends:
    print(i)

# 2d list
num = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(num[2][1])  # row, column
for row in num:
    print(row)
for row in num:
    for col in row:
        print(col)

# while loop
i = 1
while i <= 10:
    print(f" {i} Bismillah")
    i += 1
print("while loop done")

# while loop if condition guessing game
secret_word = "allah"
guess = ""
guess_start = 1
guess_limit = 3
while guess != secret_word:
    guess = input("Enter guess: ")
    if guess_start < guess_limit:
        guess_start += 1
        if guess == secret_word:
            print("you win")
            break
        else:
            print("you are wrong")
    else:
        break

# string datatype with functions
x = "Allhamdulilla for everything's"
print(x)
print(len(x))
print(x.index("h"))
print(x.index("ham"))
print(x.replace("everything's", "everything"))
print(x.upper())
print(x.upper().isupper())

# number something
from math import *  # access a lot more math

print(55)
print(55 * 2 + 9)
print(55 * (2 + 9))
print(55 % 8)  # give the remainder
print(pow(5, 2))  # 5^2
print(max(5, 2))
print(min(5, 2))
print(round(5.8))
print(round(5.3))
x = 55
print(str(x) + " is my favorite number")
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))  # squire root

# get input from user also a calculator
name = input("Enter your name: ")
number = input("Enter your number: ")
print("Assallamuolykum " + name + ". your number are " + number + ".")

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = float(number1) + float(number2)
print(sum)

# mad libs game (random)
religion = input("Enter your religion: ")
homeland = input("Enter your homeland: ")
age = input("Enter your age: ")
print(f"i love {religion}")
print(f"{homeland} is a good country.")
print("your are " + age + " years old")

# lists
w = [7, 6, 3, 4, 5, 8]
x = ['rakib', 'shakib', 'din', 'maruf', 'mahmud']
print(x[0])
print(x[-1])
print(x[1:])
print(x[1:4])  # start with 1 but not include 4
x[2] = 'sajib'
print(x)
x.extend(w)
print(x)
x.append('mashrafi')  # add a item
print(x)
x.insert(1, "fiz")
print(x)
x.remove('maruf')
print(x)
x.clear()
print(x.index("mahmud"))
print(x.count("mahmud"))
w.sort()
print(w)
w.reverse()
print(w)
v = x.copy()
print(v)
for item in x:
    if item=="din":
        continue
    print(item)
    if item=="din":
        break


# function (a collection of py code in a specific task)
def say_hi():
    print("Assallamuolykum")


print('hi')
say_hi()


def welcome(name):
    print('assallamuolykum ' + name)


welcome('rakib')
welcome('mohammad')


def whatever(name, age):
    print("Hello " + name + " you are " + str(age))


whatever('rakib', 22)


# return statement
def cudeic_number(number):
    return number * number * number  # after return no code allow


print(cudeic_number(4))
result = cudeic_number(5)
print(result)

# month conversations dictionary(key will be unique)
monthConversations = {
    "jan": "January",  # also can use number like 1
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}
print(monthConversations["mar"])  # inside of this if input are different then program will be wrong
print(monthConversations.get("dec"))
print(monthConversations.get("jec"))  # there will be no wrong if input are wrong
print(monthConversations.get("jec", "Not a valid key"))  # there will be no wrong if input are wrong

# catching error
# num=10/0
# x=int(input("Enter a number: "))
# print(x)
# to solve this
try:
    num = 10 / 0
    x = int(input("Enter a number: "))
    print(x)
except ZeroDivisionError:  # as err /n print()err then the original error will be showed
    print("Divided by zero")
except ValueError:
    print("Invalid value")

# reading/write/append files
# in open there will be the file name which i want to open but all those will be insert in the same folder
# and will be .txt file. for read "a", for write "w", for read and write "r+", for append "a",
reading = open("text1.html", "w")  # if open then have to close at the end
# print(reading.readable())  # it show the boolean value that my reading file is allow to readable or not
# print(reading.read())
# print(reading.readline())  # for reading a single line
# print(reading.readlines())  # for reading a all lines
# print(reading.readlines()[0])  # to print the index
# for read in reading.readlines():
#     print(read)
# for create new document, used new file name with extension.using "w" mood.
# writing  # when used "w" everything will be exit and new line will be added.
reading.write("<p>mush -> wk batsman</p>")
reading.close()

# modules and pip
# importing functionality form external python file
# to search all the python modules type list of python modules in google
# to install python docx, go to cmd and type pip install python-codx and uninstall type pip uninstall python-docx
import check_import

print(check_import.name_age("rakib", 22))
print(check_import.college)


# class and object
# if i want to import this student class from this file i have to type from basic_something import student
class Student:
    def __init__(self, name, id, cgpa, location):
        self.name = name
        self.id = id
        self.cgpa = cgpa
        self.location = location

    def on_honor_roll(self):
        if self.cgpa >= 3.5:
            return True
        else:
            return False


student1 = Student("rakib", 191002, 3.5, "jessore")
student2 = Student("shakib", 1910026, 3.6, "jessore")
print(student1.id)
print(student1.on_honor_roll())


# building a multiple choice
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions_prompts = [
    "Where is Green University?\n(a) Khulna\n(b) Dhaka\n(c) Jessore\n(d) Kishorgong\n\n",
    "What is the capital of Bangladesh?\n(a) Dhaka\n(b) Khulna\n(c) Jessore\n(d) Kishorgong\n\n",
    "What colour are Bananas?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]
# obj of class
questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)


# inheritance
class Chef:
    def make_chicken(self):
        print("The chef can makes chicken.")

    def make_salad(self):
        print("The chef can makes salad.")

    def make_special_dish(self):
        print("The chef can makes bbq ribs.")


class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef can make mango juice")

    def make_fried_rice(self):
        print("The chef can makes fried rice")


myChef = Chef()
myChef.make_special_dish()

chineseChef = ChineseChef()
chineseChef.make_chicken()
chineseChef.make_special_dish()

# marks calculation
marks = int(input("Enter your marks: "))


def grade(grade):
    print(f"You got {grade}")


if marks >= 80:
    print("You got A+")
elif marks <= 79 and marks >= 75:
    print("You got A")
elif marks <= 74 and marks >= 60:
    grade("A-")
elif marks <= 59 and marks >= 55:
    print("You got B+")
elif marks <= 54 and marks >= 50:
    grade("B")
elif marks <= 49 and marks >= 45:
    print("You got B-")
else:
    print("Fail")

# even odd number
num=int(input("Enter the number: "))
if num%2==0:
    print("The number is Even.")
else:
    print("The number is odd")