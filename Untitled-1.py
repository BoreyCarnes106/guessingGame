name = input("What is your name? ")
age = int(input("How old are you? "))
print("Hello, " + name + "!")
if age >= 13 and age <= 19: 
    print("you are a teenager")
elif age < 13: 
    print("You are a child")