'''print("Welcome to python again:)")
weight = float(input("Enter your weight in kg :"))
h = float(input("Enter your height :"))
height = (h*12)*0.025
BMI = weight/height**2
#round function floating points ko round about krke bta deta h jitny bhi digits point k baad chahie.
print("Your BODY MASS INDEX is :" , round(BMI , 2))

Less than 18.5	Underweight (Kam Wazan)	 Aap is category mein hain.
18.5 - 24.9	Healthy Weight (Sehatmand Wazan)	-
25.0 - 29.9	Overweight (Zyada Wazan)	-
30.0 and above	Obesity (Motaapa)       
#-------------------CONDITIONAL STATEMENTS----------------------------
if BMI < 18.5:
    print("You're underweight :]")
elif BMI >= 18.5 and BMI < 25.0:
    print("you've Healthy weight :)")
elif BMI >= 25.0 and BMI < 29.9:
    print("You're overweight :(")
else:
    print("Obesity :/")'''
#----------------------------------------------------------------
print("Check weather the number is positive, negative or zero")
num= int(input("Enter your number :"))
if num==0:
    print("It's ZERO")
elif num > 0:
    print("it's POSITIVE")
elif num < 0:
    print("it's NEGATIVE")
else:
    print("NOT DIGIT")


























