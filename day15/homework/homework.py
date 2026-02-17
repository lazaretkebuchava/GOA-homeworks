# 1

name = input("Enter Your Name: ")
if name == "Lazare":
    print("Hello")
else:
    print("Bye")


# 2

num1  = 27
num2 = int(input("Enter Your Favourite Number: "))
if num1 == num2:
    print("Perfect")
elif num1 < num2:
    print("More")
else:
    print("Less")




# 3

name = input("Enter Your Name: ")
age =  input("Enter Your Age: ")
if name == "Lazare" and age == 15:
    print("Twins")
else:
    print("Not Twins")

# 4

num3 = int(input("Enter Any Number: "))
if num3 % 3 == 0 and num3 % 5 == 0:
    print(True)
else:
    print(False)

#მოკლე ვერსია

print(num3 % 3 == 0 and num3 % 5 == 0)

# 5

password = input("Enter Password: ")
if len(password) < 8:
    print("სუსტი პაროლი")
else:
    print("ძლიერი პაროლი")