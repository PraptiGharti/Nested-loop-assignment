
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


numbers = [10, 23, 34, 56, 10, 10]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] == 10:
        count +=1
    i += 1
print(f"10 appears {count} times.")


sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
i = 0

while i < len(sentence):
    ch = sentence[i].lower()

    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

    i += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


num = abs(int(input("Enter an integer: ")))

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Total digits:", count)

n = int(input("Enter a positive integer: "))

while n != 1:
    print(n, end=", ")

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(1)


ch = ord('A')

while ch <= ord('Z'):
    print(chr(ch), end=" ")
    ch += 1


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

while start <= end:
    print(start)
    start += 1


num = 49

while num >= 1:
    print(num, end=" ")
    num -= 2


num = 7

while num <= 100:
    print(num, end=" ")
    num += 7


total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    total += num

print("Total Sum =", total)


age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Invalid age")
    age = int(input("Enter your age again: "))

print("Valid age:", age)



total = 0
count = 0

while True:
    score = float(input("Enter score (-1 to stop): "))

    if score == -1:
        break

    total += score
    count += 1

if count > 0:
    average = total / count
    print("Average Score =", average)
else:
    print("No scores entered.")


numbers = []
n = int(input("How many numbers do you want to enter? "))

i = 0
while i < n:
    num = int(input("Enter a number: "))

    j = 0
    duplicate = False

    while j < len(numbers):
        if numbers[j] == num:
            duplicate = True
            break
        j += 1

    if duplicate:
        print("Duplicate number entered!")
    else:
        numbers.append(num)

    i += 1

print("Numbers entered:", numbers)


correct_password = "secret123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break

    attempts += 1

if attempts == 3:
    print("Access Denied")

num = int(input("Enter an integer: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Integer:", reverse)

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
    count += 1


text = input("Enter a string: ")

result = ""
i = 0

while i < len(text):
    if text[i].lower() not in "aeiou":
        result += text[i]
    i += 1

print("Without vowels:", result)


text = input("Enter a string: ")

count = 0
i = 0

while i < len(text) - 1:
    if text[i:i+2] == "hi":
        count += 1
    i += 1

print("Occurrences of 'hi':", count)


numbers = [12, 25, 7, 30, 18, 40, 55, 9]

i = 0

while i < len(numbers):
    if numbers[i] % 5 == 0:
        print(numbers[i])
    i += 1


text = input("Enter a string: ")

result = ""
i = 0

while i < len(text):
    ch = text[i]

    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

    i += 1

print("Converted String:", result)

def count_case(text):
    upper = 0
    lower = 0
    i = 0

    while i < len(text):
        if text[i].isupper():
            upper += 1
        elif text[i].islower():
            lower += 1
        i += 1

    print("No. of upper case characters :", upper)
    print("No. of lower case characters :", lower)

count_case("The quick Brow Fox")


while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)
    elif choice == 2:
        print("Result =", num1 - num2)
    elif choice == 3:
        print("Result =", num1 * num2)
    else:
        print("Invalid choice")


positive = 0
negative = 0

while True:
    num = int(input("Enter number (0 to stop): "))

    if num == 0:
        break
    elif num > 0:
        positive += 1
    else:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)



start = int(input("Enter start: "))
end = int(input("Enter end: "))

while start <= end:
    if start > 1:
        i = 2
        prime = True

        while i <= start // 2:
            if start % i == 0:
                prime = False
                break
            i += 1

        if prime:
            print(start, end=" ")

    start += 1


numbers = [12, 40, 21, 31, 10, 7, 5]

i = 0
while i < len(numbers):
    if numbers[i] < 20:
        print(numbers[i])
    i += 1


numbers = [45, 60, 12, 75, 30, 55, 8, 90]

i = 0
while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0
    i += 1

print(numbers)


numbers = [15, 25, 30, 45, 60, 12, 90, 7]

count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        count += 1
    i += 1

print("Count =", count)



numbers = [10, 15, 25, 30, 45]

sorted_list = True
i = 0

while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break
    i += 1

if sorted_list:
    print("Sorted")
else:
    print("Not Sorted")


ch = ord('a')

while ch <= ord('z'):
    print(chr(ch), end=" ")
    ch += 1


chapters = [45, 30, 50, 40]

i = 0

while i < len(chapters):
    print("Chapter", i + 1, "has", chapters[i], "pages")
    i += 1


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

i = 0

while i < len(list1):
    if list1[i] in list2:
        print(list1[i])
    i += 1


tables = [2, 4, 6, 7, 8]

i = 0
while i < len(tables):
    num = tables[i]

    print("\nTable of", num)

    j = 1
    while j <= 10:
        print(num, "x", j, "=", num * j)
        j += 1

    i += 1


numbers = [10, 20, 30, 40, 20]

has_duplicate = False
i = 0

while i < len(numbers):
    j = i + 1

    while j < len(numbers):
        if numbers[i] == numbers[j]:
            has_duplicate = True
            break
        j += 1

    if has_duplicate:
        break

    i += 1

if has_duplicate:
    print("Has Duplicates")
else:
    print("No Duplicates")











