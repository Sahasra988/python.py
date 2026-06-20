1.#Reverse a String
#Take a string from the user and print it in reverse order
#Input: hello
Output: olleh

s = input("Enter a string: ")
print(s[::-1])
2.#Count Vowels
#Count how many vowels are present in a string.
#Input: programming
Output: 3
s = input("Enter a string: ").lower()

count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)