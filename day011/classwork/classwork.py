# 1

# Control flow - გამოსახულება რომელშიც ასახულია ალგორითმი,თანმიმდევრობა,გმეორება და არჩევანი
# algorithm - პროცესი რომელიც თანმიმდევრული ნაბიჯებით მიგვიყვანს მიზნამდე

# 2

# % - გვიბრუნებს გაყოფის შედეგად ნაშთს
# // - გვიჩვენებს რამდენჯერ მოთავსდება ერთი კონკრეტული რიცხვი მეორეში

num = 10
num1 = 2
print(num % num1)

num = 25
num1 = 10
print(num % num1)

num = 20
num1 = 3
print(num // num1)

num = 29
num1 = 17
print(num // num1)

# 3 
num = 17
name = "lazare"
result = num > 15 and name == "lazare"
print(result)

# 4

age = int(input("Enter your age!: "))
name = input("enter your name!: ")
print(age > 18 or name == "Andrew")

# 5

# არასწორია

print(num>18 or 2>1)
num = 17

# სწორია 

num = 17
print(num>18 or 2>1)

#-----------------------------------------------------------------------------

# არასწორია

#age = 18
#print(Age >= 18 and 10==10)

# სწორია

age = 18
print(age >= 18 and 10==10)

#-------------------------------------------------------------------------------

# სწორია

random = "saba"
print("saba"==random or 17%2==0)