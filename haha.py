
number_1 = float(input("Enter first num: "))
number_2 = float(input("Enter second num: "))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input(("1", "2", "3", "4" ))

if operation == "1":
    total = (number_1 + number_2);
    print(total)
elif operation == "2":
    total = (number_1 - number_2);
    print(total)
elif operation == "3":
    total = (number_1 * number_2);
    print(total)
elif operation == "4":
    total = (number_1 / number_2);
    print(total)
else :
    print("error")