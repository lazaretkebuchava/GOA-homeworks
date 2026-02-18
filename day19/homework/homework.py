# 1

numbers = [1, 11, 34, 5, 6, 10, 28, 90, 17, 19, 38]
for i in numbers:
    if i >= 10:
        print(i)

# 2

name = input("Enter your name: ")
print(name[0], name[-1])

# 3

names = ["lazare", "luka", "gio", "nika"]
print(names[::-1])

# 4 

lastname = input("Enter you last name: ")
print(lastname[:5][::-1])

# 5

numbers = [1,2,3,4,5,6]
num = int(input("Enter number 1-5: "))
result = []
for i in numbers:
    if i % num == 0:
        result.append(i)
print(result)