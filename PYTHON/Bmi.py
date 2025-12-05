weight = int(input("Enter weight in kG:"))
height = int(input("Enter height in feet:"))
bmi = weight/(weight * weight)

if(bmi < 18.5):
    print("Under Weight")
elif(bmi > 18.5 and bmi <= 24.9):
    print("Normal")
elif(bmi >= 25 and bmi <= 29.9):
    print("Overweight")
elif(bmi >= 30):
    print("Obess")
