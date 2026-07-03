# Sum of First N Numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

#Count Digits in a Number
num = input("Enter a number: ")
count = 0
for digit in num:
    count += 1
print("Number of digits:", count)

# Sum of Even Numbers
sum_even = 0
for i in range(2, 51, 2):
    sum_even += i
print("Sum of Even Numbers =", sum_even)