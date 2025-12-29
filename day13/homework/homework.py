#1

for i in range(1 , 51 , +2):
    print(i)

#2

name = input("Enter your name!: ")
for i in name:
    print(i)

#3

for i in range(1,151):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")

#4

for i in range(20,-1,-1):
    print(i)

#5

original_password = "ok"
user_password = ""
while user_password != original_password:
    user_password = input("Enter Password!: ")
print("Password Is Correct")