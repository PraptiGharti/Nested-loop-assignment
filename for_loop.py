"""
Check if each number is even or odd
"""
for i in range(1, 6):
    if i % 2 == 0:
        print(f"Number {i} is even. ")
    else:
        print(f"Number {i} is odd.")

"""
Calculate the sum of all elements of the list
"""
num = [10,20,30,40]
sum = 0
for el in num:
    sum += el
    print(f"Added {el}. Running total is {sum}.")

print(f"Total Sum: {sum}")  

"""
"""
header = ' --- Email Greetings Generated ---'
print(header)
student_names = ["Ram", "Hari", "Sita"] 
for name in student_names:
    print(f"Hi {name}, your course approval is ready!.")

"""
"""
chapter = [45, 30, 50, 40]
print('--- Book Chapter Summary ---')
count = 1
for page in chapter:
    print(f"Chapter {count} has {page} pages. ")
    count += 1

"""
"""
List = [4,5,3,2]
product = 1
for el in List:
    product *= el
print(f"Multiplication of elements of list is {product}.")  

"""
Multiplication table of 11
"""
n = 11
for i in range(1, 11):
    print(f"{n}*{i}= {n * i}")

"""
reverse a list
"""
rev  = [3, 2, 1, 4, 5]

for el in rev:
    rev.reverse()
print(rev)    
    
"""
Finding common number from two list
"""
num1 =[1,2,3,4,5] 
num2 =[3,4,5,6,7]
print("Common numbers are:")
for i in num1:
    for j in num2:
      if i == j:
          print(i)

lst = [1, 2, 3, 4]
for i in lst:
    if i == 1 or i == 4:
        print(i)


string ='apple'
vowels = 'aeiou'
result = ''
for char in string:
    if char not in vowels:
        result += char
print(result)      

sentence = "Loop are fun"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count +=1
        else:
            consonant_count +=1
print("vowels:", vowel_count)
print("Consonant:", consonant_count)

num = [1,2,3,4,5]
odd = []
even = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)            

"""
prime numbers
"""
n = 7
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count +=1
if count == 2:
    print("Given number is prime")   


list = [1,2,3,4,"a","b"] 
integer = []
string = []
for el in list:
    if isinstance(el, int):
        integer.append(el)
    else:
        string.append(el)
print(integer)
print(string)            


text = "python123"
letters = 0
digit = 0
for char in text :
    if char.isalpha():
        letters +=1
    elif char.isdigit():
        digit +=1
print("letters:",letters)
print("digit:", digit  )            

username = input("Enter username: ")
password = input("Enter password: ")

# Example valid username and password
valid_username = "admin"
valid_password = "12345"

if username == valid_username and password == valid_password:
    print("Login successful")
else:
    print("Invalid username or password")



num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)



for i in range(1, 9):
    print("Table of", i)

    for j in range(1, 11):
        print(f"{i} x {j}= {i * j}")

    print()


lst = [1, 2, 3, 4]

for i in lst[:2]:
    print(i)


total = 0

for i in range(1, 11):
    if i % 2 != 0:
        total += i

print(total)


total = 0

for i in range(1, 11):
    if i % 2 == 0:
        total += i

print(total)


text = "Python is fun"
count = 0

for char in text:
    if char == " ":
        count += 1

print(count)




lst = [1, 2, 3, 4]
result = []

for i in lst:
    result.append(i ** 3)

print(result)


a = "programming"

print(a[::-1])

for i in range(50):
    if i == 8:
        break

    print(i)


text = "Python"

for char in text:
    print(char)



a = ["ram", "shyam", 1, 2]

for i in a:
    if isinstance(i, str):
        print("Hello!", i)


a = ["ram", "shyam", 1, 2]

result = []

for i in a:
    result.append("Dr." + str(i))

print(result)


lst = [1, 2, 3, 4]

new_list = []

for i in lst:
    new_list.append(i ** 2)

print(new_list)



lst1 = [111, 32, -9, -45, -17, 9, 85, -10]

new_list = []

for i in lst1:
    if i > 0:
        new_list.append(i)

print(new_list)


lst = [0, 1, 2, 3, 4, 5, 6]

for i in lst:
    if i == 3 or i == 6:
        continue

    print(i)


lst = [1, "a", 2.5, True]

types = []

for i in lst:
    types.append(type(i))

print(types)



for i in range(5):
    print(i)

else:
    print("Done")


for i in range(105, 6, -7):
    print(i, end=" ")


bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"

result = ""

for char in string:
    if char not in bad_chars and char != " ":
        result += char

print(result)



numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


total = 0

for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)

even_sum = 0
odd_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)



