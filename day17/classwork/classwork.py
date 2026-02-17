#1

# Lists - რიგობრივი ნივთების კოლექცია რომლის შეცვლაც შესაძლებელია.ვიყენებთ მაშინ როდესაც არ გვინდა ცვლადები ცალცალაკე გამოვიტანოთ.

#2

names = ["giorgi","Nikolozi","Mate","Aleqsi","Andria"]

print(names[2])

#3

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 3 == 0:
        print("divisible by 3")

#4

name = "lazare"

print(name[-3:])

#5

names = ["lazare","soso","misha"]

user_name = input("Enter Your Name ")

count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1

print("count:", count)

#6

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print(even_sum)

#7

names = ["giorgi", "nino", "guga", "ana", "luka", "gabrieli"]

for name in names:
    if name.startswith("g"):
        print(name, True)