# Student Resource Portal

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard.")

elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions.")

else:
    print("Invalid Credentials.")
    print("Please try again.")


# Customer Final Bill Calculator

# Input total purchase amount
total_purchase_amount = float(input("Enter total purchase amount: "))

# Check if purchase is greater than 5000
if total_purchase_amount > 5000:

    # Get membership status
    membership = input("Do you have a membership card? (yes/no): ")

    # Check membership card
    if membership.lower() == "yes":

        # Apply 30% discount
        discount = total_purchase_amount * 0.30
        final_price = total_purchase_amount - discount

        print("\nPREMIUM CUSTOMER RESULTS")
        print("Total Saved:", discount)
        print("Final Bill:", final_price)

    else:
        # No membership card
        print("\nFINAL BILL (NO DISCOUNT)")
        print("Total:", total_purchase_amount)
        print("Discount: 0")

else:
    # Purchase amount not greater than 5000
    print("\nFINAL BILL (NO DISCOUNT)")
    print("Total:", total_purchase_amount)
    print("Discount: 0")




# Magic Forest Adventure Game

print("Welcome to the Magic Forest")

# Stage 1
direction = input("Go NORTH or SOUTH? ").lower()

if direction == "north":

    # Stage 2
    choice = input("Cross the RIVER or FOLLOW the PATH? ").lower()

    if choice == "river":
        print("Cross the River. END.")

    elif choice == "path":

        # Stage 3
        creature = input("Choose FAIRY, OGRE, or ELF: ").lower()

        if creature == "elf":
            print("YOU WIN!")

        elif creature == "ogre":
            print("GAME OVER")

        elif creature == "fairy":
            print("GAME OVER")

        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

else:
    print("GAME OVER")




# Traffic Light System

light = input("Enter traffic light color (red/yellow/green): ").lower()

if light == "red":
    print("STOP")

elif light == "yellow":
    print("GET READY")

elif light == "green":
    print("GO")

else:
    print("Error: Invalid traffic light color")



# Season Program

number = int(input("Enter a number (1-4): "))

match number:
    case 1:
        print("spring")

    case 2:
        print("summer")

    case 3:
        print("autumn")

    case 4:
        print("winter")

    case _:
        print("unknown")




# Bank Loan Approval System

age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))

# Check conditions
if age < 21 or age > 60:
    print("Loan Not Approved: Age condition failed")

elif income < 30000:
    print("Loan Not Approved: Income condition failed")

elif credit_score < 700:
    print("Loan Not Approved: Credit score condition failed")

else:
    print("Loan Approved")




# Student Grade Calculator

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

else:
    print("Grade: Fail")




# BMI Calculator

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine weight category
if bmi < 18.5:
    status = "Underweight"

elif bmi <= 25:
    status = "Normal weight"

elif bmi <= 30:
    status = "Overweight"

else:
    status = "Obese"

# Display result
print("Weight:", weight)
print("Height:", height)
print("BMI:", round(bmi, 1), status)




# Movie Ticket Booking System

age = int(input("Enter your age: "))

if age < 12:
    ticket_price = 0

elif age <= 60:

    membership = input("Do you have a membership card? (yes/no): ").lower()

    if membership == "yes":
        ticket_price = 150
    else:
        ticket_price = 200

else:
    ticket_price = 100

print("Ticket Price: Rs.", ticket_price)



# Employee Bonus Calculator

salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter years of service: "))

if years_of_service > 5:
    bonus = salary * 0.05
    print("Net Bonus Amount:", bonus)

else:
    print("No bonus awarded")



# Area of Circle Calculator

radius = float(input("Enter the radius of the circle: "))

# Calculate area
area = 3.14 * radius * radius

print("Area of the circle is:", area)


# Wages Calculation
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days worked: "))

wage_per_day = 0

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750

elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850

if wage_per_day == 0:
    print("Invalid age or gender input")
else:
    total_wage = wage_per_day * days
    print("Total wage:", total_wage)


# Fizz Buzz Program
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)



# Electric Bill Calculation
units = int(input("Enter electricity usage in units: "))

bill = 0

if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 8)

else:
    bill = (100 * 5) + (200 * 8) + ((units - 300) * 10)

print("Total electricity bill: Rs", bill)



# Rock paper scissors
p1 = input("Player 1 (rock/paper/scissors): ").lower()
p2 = input("Player 2 (rock/paper/scissors): ").lower()

if p1 == p2:
    print("It's a tie!")

elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "scissors" and p2 == "paper") or \
     (p1 == "paper" and p2 == "rock"):
    print("Player 1 wins!")

elif p2 in ["rock", "paper", "scissors"]:
    print("Player 2 wins!")

else:
    print("Invalid input")





# Positive Even or Odd Check
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")




# Store Discount Calculator
# total_amount = float(input("Enter total purchase amount: "))
is_member = input("Are you a member? (True/False): ").strip().lower() == "true"

if total_amount > 1000:
    if is_member:
        discount = 0.20  # 20%
    else:
        discount = 0.10  # 10%
else:
    discount = 0.0

final_amount = total_amount * (1 - discount)
print(f"Final amount after discount: RS {final_amount:.2f}")




# Planet Weight Converter
earth_weight = float(input("Enter your Earth weight: "))
print("1. Mercury  2. Venus  3. Mars  4. Jupiter  5. Saturn  6. Uranus  7. Neptune")
planet_num = int(input("Enter the planet number: "))

gravity = 0

if planet_num == 1:
    gravity = 0.38
elif planet_num == 2:
    gravity = 0.91
elif planet_num == 3:
    gravity = 0.38
elif planet_num == 4:
    gravity = 2.53
elif planet_num == 5:
    gravity = 1.07
elif planet_num == 6:
    gravity = 0.89
elif planet_num == 7:
    gravity = 1.14
else:
    print("Invalid planet number")

if gravity > 0:
    destination_weight = earth_weight * gravity
    print(f"Your weight on the destination planet is: {destination_weight:.2f}")



# Subject Marks and Grade Calculator
# Accepting marks for four subjects
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))

total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print(f"\nTotal Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")




# Simple ATM Simulation
balance = 5000
correct_pin = "123"
is_valid = True

user_pin = input("Enter your PIN: ")

if is_valid and user_pin == correct_pin:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"RS {amount} withdrawn successfully.")
            else:
                print("Insufficient balance!")
        elif choice == '2':
            print(f"Your current balance is: RS {balance}")
        elif choice == '3':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option. Please try again.")
else:
    print("Wrong PIN or Invalid Card.")




# Elevator Internal Logic
# Inputs
target_floor = int(input("Enter desired floor (0-10): "))
total_weight = float(input("Enter current weight in kg: "))
door_status = input("Is the door closed? (yes/no): ").lower()

# Logic Constraints
if not (0 <= target_floor <= 10):
    print("INVALID FLOOR")
elif total_weight > 500:
    print("OVERWEIGHT: LIFT CANNOT MOVE")
elif door_status != "yes":
    print("WARNING: CLOSE THE DOOR")
else:
    print("ACTIVATE ELEVATOR MOTION")




# User Registration Validation
# Inputs
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
email = input("Enter Email: ")
re_email = input("Re-enter Email: ")
password = input("Enter Password (min 6 characters): ")

# Validation logic
if not (first_name.isalpha() and first_name != ""):
    print("Error: First name must be letters only and not empty.")
elif not (last_name.isalpha() and last_name != ""):
    print("Error: Last name must be letters only and not empty.")
elif "@" not in email or "." not in email:
    print("Error: Invalid email format.")
elif email != re_email:
    print("Error: Emails do not match.")
elif len(password) < 6:
    print("Error: Password must be at least 6 characters.")
else:
    print("Registration Successful!")        

