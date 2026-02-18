# 1

numbers = [1, 11, 34, 5, 6, 7, 28, 90, 17, 19, 38]
for i in numbers:
    if i > 10:
        print(i)

# 2

randoms = ["luka", 3, 3.17, "apple", 4.8, True, False]
for i in randoms:
    print(type(i))

# 3

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in numbers1:
    sum += i
print(sum)

# 4

names = ["lazare", "luka", "gio", "nika", "zura", "saba"]
for i in range(len(names)):
    print(names[i], i)

# 5

names1 = ["lazare", "luka", "gio", "nika", "zura", "saba"]
for i in range(len(names1)):
    if i % 2 == 0:
        print(names1[i])

# 6 

int = [-1, 2, -3, 0, 5, 6, -7, 8, 0, -10, 11, 12, 0, -14, 15, 16, -17, 18, -19, 20]
positive = 0
negative = 0
for i in int:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        print("zero")
print(positive)
print(negative)