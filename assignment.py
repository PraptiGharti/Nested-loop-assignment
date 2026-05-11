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