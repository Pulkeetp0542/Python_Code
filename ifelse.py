print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter you age"))
    if age >= 18:
        print("Eligible for ride")
    else:
        print("Not Eligible")
else:
    print("Sorry,You are not eligible for the ride")