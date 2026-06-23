#1. Print Numbers from 1 to 10
#Use a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)
#2. Print Odd Numbers from 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
#3.Find the number of digits in a given number.
num = int(input("Enter a number: "))

count = 0

while num > 0:
    count += 1
    num = num // 10

print("Digits =", count)
#4.Find the factorial of a number.
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)
#5.Check whether a number is prime or not.
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")