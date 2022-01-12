try:
    age = int(input("Enter your age:"))
    print(age)
except ValueError as e:
    print("Please enter numerical value")
    print(e)
else:
    print("No error thrown")
print("Execution continues .....")
