# 1

# .upper() - ადიდებს ასოების ზომას ცვლადის მნიშვნელობისთვის
# .lower() - აპატარავებს ასოების ზომას ცვლადის მნიშვნელობისთვის
# .capitalize() - ცვლადის მნიშვნელობის პირველ ასოს ადიდებს

# 2

name = input("Enter your name! ")
print(name.capitalize())

# 3 

names = ["lazare" , "vano" , "giorgi" , "luka" , "mate"]

for i in names:
    print(i.capitalize())

# 4

lastname = input("Enter your last name! ")
if lastname == "t":
    print(True)
else:
    print(False)

# 5

surname = input("Enter your surname: ")
case = input("Which case do you want? (upper , lower , capitalize , none): ")

if case == "upper":
    print(surname.upper())
elif case == "lower":
    print(surname.lower())
elif case == "capitalize":
    print(surname.capitalize())
elif case == "none":
    print(surname)
else:
    print("incorrect input")

# 6

sentence = input("Enter a sentence: ")
symbol = input("Enter a symbol: ")

index = sentence.find(symbol)

print(index)

# 7

sentence = input("Enter a sentence: ")
symbol = input("Enter a symbol: ")

for i in range(len(sentence)):
    if sentence[i] == symbol:
        print(i)