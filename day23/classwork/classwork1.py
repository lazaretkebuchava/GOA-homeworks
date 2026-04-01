# 1

names = ["ნიკა", "გიორგი", "ლუკა", "საბა", "დათო"]

if "გიორგი" in names:
    names.remove("გიორგი")
    print(names)
else:
    print(names)

# 2

names1 = ["ნიკა", "გიორგი", "ლუკა", "საბა", "დათო"]
names1.remove(names1[-1])
print(names1)

# 3

names2 = ["ნიკა", "ლუკა", "საბა", "დათო"]

names2.insert(2, "ალექსანდრე")

print(names2)

# 4

names3 = ["ნიკა", "ლუკა", "საბა", "დათო"]
name = input("Enter your name! ")
names3.append(name)
print(names3)

#5

numbers = [10, 20, 30, 40, 50]
favorite_number = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))
index = int(input("შეიყვანეთ ინდექსი, სადაც გინდათ დამატება: "))
if 0 <= index < len(numbers):
    numbers.insert(index, favorite_number)
    print(numbers)
else:
    print("invalid index")
    
# 6,7?