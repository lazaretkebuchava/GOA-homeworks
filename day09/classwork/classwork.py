 # 1

# Explicit Data Conversion - მონაცემის ტიპის შეცვლა მომხმარებლის ხელით.

# Implicit Data Conversion - მონაცემის ტიპის შეცვლა ავტომატურად

# Explicit Data Conversion

num1 = int("50")
num2 = int("70")
print(int(num1 * num2))

# Implicit Data Conversion

num1 = 10
num2 = 5
print(num1 / num2)

# 2

num1 = "10"
print(int(num1))

num1 ="35"
print(float(num1))

num1 = 50
print(str(num1))

# 3

num = 6/2
print(type(num))

# გამოიტანს მონაცემის კლასს - float-ს.არ გვაჩვენებს შედეგს

# 4

number = 6.0
number > 6

# True

# 5

num = int(input("Enter Number: "))
num1 = int(input("Enter Number: "))
num2 = num / num1
print(float(num2))