num_1 = int(input("Enter first number:"))

num_2 = int(input("Enter second number:"))

num_3 = int(input("Enter third number:"))

largest = num_1

if(num_2 > largest):
    largest = num_2

if(num_3 > largest):
    largest = num_3

print("The largest number is:", largest)

