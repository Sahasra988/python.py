#Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Login System
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#ATM Withdrawal
balance = 10000
amount = float(input("Enter withdrawal amount: "))
if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")