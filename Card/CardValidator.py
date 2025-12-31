card = input("Hello, Kindly Enter Card details to verify:  ")

if card.startswith("4"):
    print("**Credit Card Type: Visa Card")

elif card.startswith("5"):
    print("**Credit Card Type: MasterCard")

elif card.startswith("37"):
    print("**Credit Card Type: American Express Card")

elif card.startswith("6"):
    print("**Credit Card Type: Discover Card")

else:
    print("**Credit Card Type: Invalid Card")

print(card)

length = len(card)

if(length < 13 or length > 17):
    print("**Credit Card Digit Length: ", length)
else:
    print("**Credit Card Digit Length: ", length)

total=0
for index in range(len(card)-1,-1,-1):
        number =int(card[index])

        if index%2==0:
            number *=2
            if number>9:
                number-=9
        
        total+=number

if( total%10==0):
    print("**Credit Card Validity Status: Valid")
else:
    print("**Credit Card Validity Status: Invalid")


              



