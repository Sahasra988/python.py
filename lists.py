#1. Create and Print a List
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits)
#2. Find Length of a List
numbers = [10, 20, 30, 40, 50]
print(len(numbers))
#3. Access First and Last Element
numbers = [10, 20, 30, 40, 50]
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

#4. Add an Element
languages = ["Java", "C++", "JavaScript"]
languages.append("Python")
print(languages)

#5. Insert an Element
fruits = ["Apple", "Banana", "Orange"]
fruits.insert(1, "Mango")
print(fruits)

#6. Remove an Element
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.remove("Banana")
print(fruits)

#7. Sum of Elements
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("Sum =", total)