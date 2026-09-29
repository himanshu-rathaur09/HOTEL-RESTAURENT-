name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Hello", name)
    print("You are an adult.")
else:
    print("Hello", name)
    print("You are a minor.")

print("Your age after 5 years will be", age + 5)