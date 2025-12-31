import math

pizza_menu = print("""

WELCOME TO IYA SCAMBIRAH PIZZA JOINT
__________________________________________________________
|                   |                   |                |
|  Pizza Size       | Number Of Slices  | Price Per Box  |
|___________________|___________________|________________|
|                   |                   |                |
| Sapa Size         |      4            |  #2,000.00     |
|___________________|___________________|________________|
|                   |                   |                |
| Small Money       |      6            |  #2,400.00     |
|___________________|___________________|________________|
|                   |                   |                |
| Big Boys          |      8            |  #3,000.00     |
|___________________|___________________|________________|
|                   |                   |                |
| Odugwu            |      12           |  #4,200.00     |
|___________________|___________________|________________|
 """)



pizza_type =input("Enter Type Of Pizza: ").casefold()

number_of_people = int(input("How Many People Wants To Eat Pizza?:  "))

match pizza_type:
    
    case "sapa size":
        Pizza_name = "Sapa Size"
        number_of_slices = 4
        price = 2000


    case "small money":
        Pizza_name = "Small Money"
        number_of_slices = 6  
        price = 2400


    case "big boys":
        Pizza_name = "Big Boys"
        number_of_slices = 8 
        price = 3000

    case "odugwu":
        Pizza_name = "Odugwu"
        number_of_slices = 12
        price = 4200

number_of_boxes_needed = math.ceil(number_of_people / number_of_slices)
print(f"The Number Of Boxes You Will Need Is:{number_of_boxes_needed}")  

quantity_of_remaining_slice = (number_of_slices * number_of_boxes_needed - number_of_people)
        
print(f"The Number Of leftover Pizza Slice is: {quantity_of_remaining_slice}")

total_amount = (number_of_boxes_needed * price)
print(f"Your Total Amount: {total_amount}")
















