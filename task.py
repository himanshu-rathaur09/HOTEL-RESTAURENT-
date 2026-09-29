name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)

if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")