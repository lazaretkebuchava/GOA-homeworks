# 1

# slicing - სიიდან გამოყოფა და ამოღება ელემენტების
# indexing - კონკრეტული ელემენტის გამოძახება

# განსხვავება - indexing-ის საშუალებით ვიძახებთ ერთ ელემენტს,slicing-ით რამდენიმეს სიიდან

# 2

names = ["gio" , "tedo" , "gabrieli" , "nikolozi" , "mate" , "saba"]

print(names[3:])

# 3

name = input("Enter Your Name!: ")

print(name[1:4])

# 4

lastname = input("Enter Your Last Name!: ")
if lastname[0:6] == "tkebu":
    print("Almost Same")
else:
    print("Bye")

# 5

names = ["gio" , "tedo" , "gabrieli" , "nikolozi" , "mate" , "saba" , "tengo"]

names[3] = "Random"

print(names[0:4])