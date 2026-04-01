# 1

# for loop - გამოიყენება იმ შემთხვევაში თუ წინასწარ ვიცით რამდენჯერ უნდა გამეორდეს ციკლი
# while loop - გამოიყენება იმ შემთხვევაში როდესაც წინასწარ არ გვაქ განსაზღვრული ციკლის რაოდენობა


# 2

word = "lesson"

for i in word:
    print(i)

# 3

num = 2

while num <= 25:
    print(num)
    num += 3

# 4

my_list = ["a", "b", "c", "d", "e"]

user_input = input("Enter something: ")
my_list.insert(4, user_input)
print(my_list)

# 5

numbers = [10, 24, 5, 7, 24, 30]

numbers.remove(24)

print(numbers)

# 6

y_list = ["a", "b", "c", "d", "e"]

user_input = input("Enter something: ")
my_list.insert(4, user_input)
my_list.pop(3)
print(my_list)