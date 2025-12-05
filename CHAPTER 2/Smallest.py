
digit_1 = int(input("Enter number:"))

digit_2 = int(input("Enter number:"))

digit_3 = int(input("Enter number:"))

n = 3

sum = digit_1 + digit_2 + digit_3
print("The sum of three numbers is :%d%n",sum)


product = digit_1 * digit_2 * digit_3
print("The product of three numbers is:%d%n", product)


average = sum/n
print("The average of three numbers is:%d.2f", average)

if(digit_1 < digit_2 and digit_1 < digit_3):
    print("Digit_1 is the smallest")

elif(digit_2 < digit_1 and digit_2 < digit_3):
    print("Digit_2 is the smallest")

elif(digit_3 < digit_1 and digit_3 < digit_2):
    print("Digit_3 is the smallest")



digit_1 = int(input("Enter number:"))

digit_2 = int(input("Enter number:"))

digit_3 = int(input("Enter number:"))


if(digit_1 > digit_2 and digit_1 > digit_3):
   print("Digit_1 is the largest")

if(digit_2 > digit_1 and digit_2 > digit_3):
   print("Digit_2 is the largest")

if(digit_3 > digit_2 and digit_3 > digit_1):
   print("Digit_3 is the largest")












