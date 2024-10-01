# Write a program to check whether a number is odd or even.
x = int(input("Enter a number: "))
if x >= 0:
    if x % 2 == 0:
        print(f"{x} is a even number.")
    else:
        print(f"{x} is a odd number.")
else:
    print("Invalid input")