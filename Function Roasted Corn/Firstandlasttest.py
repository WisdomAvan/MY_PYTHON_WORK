name_in_string = input("Enter Any Word: ")

name_in_length = len(name_in_string)

first_letter = name_in_string[0]

second_letter = name_in_string[1]

last_letter = name_in_string[len(name_in_string)-1]

second_to_the_last =name_in_string[len(name_in_string)-2]

expected_output = (first_letter + second_letter + second_to_the_last + last_letter)

if (name_in_length < 2):
    print("")
elif( name_in_length == 2):
    print(name_in_length *2)
elif(string_from_user < 3)
    print(string_from_user)
else:
    print(expected_output)


