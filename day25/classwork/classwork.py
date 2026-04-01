# 1 

# ფუნქცია - კოდის ბლოკი, რომელიც ასრულებს კონკრეტულ დავალებას

# 2

def sum_of_3(a, b, c):
    return a + b + c
result1 = sum_of_3(5, 10, 15)
print(result1)

# 3

def list_length(my_list):
    return len(my_list)
numbers = [10, 20, 30, 40]
result2 = list_length(numbers)
print(result2)

# 4

def average(numbers1):
    total = sum(numbers1)
    count = len(numbers1)
    return total / count
nums = [10, 20, 30, 40]
result3 = average(nums)
print(result3)

# 5

def add_to_list(text, index):
    my_list = ["apple", "banana", "orange"]
    my_list.insert(index, text)
    return my_list
result = add_to_list("grape", 1)
print(result)

# 6

def my_len(collection):
    count = 0
    for item in collection:
        count += 1
    return count
numbers = [10, 20, 30, 40, 50]
print(my_len(numbers))

# 7

def my_sum(numbers):
    total = 0            
    for num in numbers:     
        total += num          
    return total
nums = [5, 10, 15, 20]
print(my_sum(nums))