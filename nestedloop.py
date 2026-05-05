"""
To check whether you can ride roller coaster 
"""
age = int(input("enter your age: "))
height = float(input("enter your height: "))
if (age >= 12 and height >= 140):
    print("You can ride the roller coaster") 
else:
    print("You cannot ride")


"""
Design of Traffic Light System
"""
color = input("enter a color: ")
match color:
    case "Red": print("Stop")
    case "Yellow" : print("Wait")
    case "Green": print (" Go")
    case _ : print("Invalid colour")


"""
Using match statement that takes a number 1-4 and prints the 
corresponding seasons
"""
number = input("enter a number: ")
match number:
    case 1: print("spring")
    case 2: print("winter")
    case 3: print("autumn")
    case _: print("invalid")


"""
Design a Bank Loan Approval System. Approve only if 
all three conditions are matched.
If not approved, print which condition failed. If multiple
fail, pick the most important one.
"""
loan = int(input("enter a loan: "))
age = int(input("enter your age: "))
monthly_income = int(input("enter your monthly income: "))
credit_score = int(input("enter your credit score: "))
if (age >=21 and age <= 60):
    if(monthly_income <=30,000):
        if credit_score == 700:
            print("Loan approved")
        else:
            print("Your credit score is low than 700")
    else:
        print("Your montly income is low ")
else:
    print("Loan dennied due to age restriction")


"""
To print the ticket price based on the user's age and
membership status.
"""
user_age = int(input("enter your age: "))
membership = input("Do you have a membership card (yes/no)?: ")
if user_age < 12: 
    print("Free ticket!")
elif(user_age >=12 and user_age <=60):
    if membership == "yes":
        print("The cost of ticket is Rs. 150")
    else:
        print("The cost of ticket is Rs. 200")
else:
    print("The cost is Rs. 100")            


"""
Ask user for their salary and year of service and print
the net bonus amount
"""
salary = int(input("enter your salary: "))
service = int(input("enter your service: "))
if service > 5:
    net_salary = salary* 0.05
    # 5% = 0.05
    print(f"Your net bonus amount is {net_salary}")  
else:
    print("No bonus amount")

"""
Accepts the radius of circle from user and compute the area
"""
radius = float(input("Enter the radius of circle: "))
area = 3.14 * radius * radius
# pi = 3.14 
print(f"The area of the circle is {area}")

"""
Accept the age, gender('M', 'F'), number of days and display
the wages accordingly
"""
age = int(input("Enter your age: "))
gender = input("Enter your gender(M/F): ")
days = int(input("How many days you work?: "))
wage_per_day = 1
if (age >= 18 and age < 30):
    if gender.upper() == "M":
        wage_per_day = 700 
    elif gender.upper() == "F":
        wage_per_day == 750
    else:
        print("Invalid gender")

elif (age >= 30 and age <= 40):
    if(gender.upper() == "F"):
        wage_per_day = 850
    elif gender.upper() == "M":
        wage_per_day = 800
    else:
        print("Invalid gender")
else:
    print("Invalid age")

total_wage = wage_per_day * days

print(f"Wage per day: {wage_per_day}")
print(f"Total wage: {total_wage}")

"""
Accept input from user and check whether the given number 
is multiple of 3 and 5
"""
num = int(input("Enter a number: "))
if (num % 3==0 and num % 5==0):
    print("Fizz Buzz")
elif(num % 3 ==0 and num % 5!=0):
    print("Fizz")
elif(num % 5 ==0 and num % 3!=0):
    print("Buzz")
else:
    print("value as usual")            
