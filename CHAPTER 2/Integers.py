number_of_integers =int(input("Type any integer  "))
print("Enter your number")

counter = 1
sum_odd = 0
sum_even = 0

while(counter <= number_of_integers):
    
    number = int(input())

    if(number % 2 ==0):
        sum_even = number + sum_even
    else:
        sum_odd = number + sum_odd

    counter = counter + 1
print("The sum of even and odd integers are ", sum_even, "and", sum_odd)

   


