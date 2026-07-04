#1. Count Vowels and Consonants
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
#2.Reverse a String
text = input("Enter a string: ")
reverse_text = text[::-1]
print("Reversed String:", reverse_text)
#3. Check Palindrome
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")