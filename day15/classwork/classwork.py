# 1

# Conditional Statements - Python-ში Conditional Statements გამოიყენება კოდის კონკრეტული ბლოკების შესასრულებლად იმის მიხედვით, არის თუ არა პირობა true ან false.

# 2

age = 16
if age >= 18:
    print("Adult")
elif age >= 13 and age < 18:
    print("Teen")
else:
    print("Child")

# 3

name = "Giorgi"
age1 = 17
if name == "Giorgi" and age1 > 18:
    print("Adult Giorgi")
elif name == "Giorgi" and age1 < 18:
    print("not adult Giorgi")
else:
    print("not Giorgi")

# 4

num1 = 36
num2 = 18
if num1 % num2 == 0:
    print(True)
else:
    print(False)

# მოკლე ვერსია
print(num1 % num2 == 0)

# 5
movie = input("Enter Your Favourite Movie Name: ")
name = input("Enter Your Name ")
if name == "Avto":
    print("you are Avto")
elif name == "Levani" and movie == "Titanic":
    print("Levani loves titanic")
else:
    print("someone likes other film")