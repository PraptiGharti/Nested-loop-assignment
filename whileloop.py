"""
number = []
while True:
    num = int(input("Enter any number: "))
    if num in number:
        print("Duplicate number")
        break

    number.append(num)


print("Program stopped because of duplicate numbers.")


user = int(input("Enter a positive number: "))
fact = 1
i = 1
if user> 0:
    while i <= user:
        fact *= i
        i+=1
    print(f"Factorial of {user} is {fact}")

else:    
   print("Please enter positive number.")


num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    sum+=i
    i +=1
print(f"Sum of 1 to up to {num} is {sum}")
"""

numbers = [10, 23, 34, 56, 10, 10]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] == 10:
        count +=1
    i += 1
print(f"10 appears {count} times.")




