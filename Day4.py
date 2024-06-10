# Lists 
# List Methods:

companies = ["Google", "Facebook", "Meta", "Netflix"]

# Append 
companies.append("Apple")
print(f"Append: {companies}")

# Insert 
companies.insert(2, "CISCO")
print(f"Insert: {companies}")

# Remove
companies.remove("Facebook")
print(f"Remove: {companies}")

# Copy
# Shallow Copy
shallow_copy = companies.copy()
shallow_copy[0] = "OpenAI"
print(f"Shallow Copy: {shallow_copy}, Original: {companies}")

# Deep Copy
import copy
deep_copy = copy.deepcopy(companies)
deep_copy[0] = "IBM"
print(f"Deep Copy: {deep_copy}, Original: {companies}")

# Count
companies.append("Google")
googleCount = companies.count("Google")
print(f"Google Count: {googleCount}")

# Extend
more_companies = ["Tesla", "SpaceX", "Twitter"]
companies.extend(more_companies)
print(f"Extending: {companies}")

# Index
openAiIndex = companies.index("Tesla")
print(f"Index of OpenAI: {openAiIndex}")

# Sort
companies.sort
print(f"Sort: {companies}")

# Reverse
companies.reverse()
print(f"Reverse: {companies}")

# Clear 
companies.clear()
print(f"Clear: {companies}")

# Pop
removed_company = more_companies.pop()
print(f"Pop: {removed_company}, Remainings: {more_companies}")


# Indexing
company = ["Google", "Facebook", "Meta", "Netflix"]

# accessing elements using positive indexing
first = company[0]
second = company[1]
third = company[2]
fourth = company[3]
print("First: ", first)
print("Second: ", second)
print("Third: ", third)
print("Fourth: ", fourth)

# Accessing elements using negative indexing
second_last = company[-2]
third_last = company[-3]
print("Second last: ", second_last)
print("Third last: ", third_last)

# Slicing
company = ["Google", "Facebook", "Meta", "Netflix", "Amazon", "Cisco", "Tesla", "SpaceX", "IBM"]

subset1 = company[1:4]
print("Positive slicing: ", subset1)

# Slice with a step
subset2 = company[1:7:2]
print("Slice with a step: ", subset2)

# Negative slicing
subset3 = comapny[-3:] 
print("Slice with negative slicing: ", subset3)


# Tuples
y= ("apple", "banana", "cherry")
print(y)

# Allow Duplicates:
x= ("apple", "banana", "cherry", "apple", "cherry")
print(x)

#Tuple Length:
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

#Print the second item in the tuple:
w = ("apple", "banana", "cherry")
print(w[1])

#Return the third, fourth, and fifth item:
e = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(e[2:5])

#This example returns the items from the beginning to, but NOT included, "kiwi":
t= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[:4])

#This example returns the items from index -4 (included) to index -1 (excluded)
le = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(le[-4:-1])

#Convert the tuple into a list , add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
     
# Delete tuple:
thistuple = ("apple", "banana", "cherry")
del thistuple

# Using Asterisk*:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# You can loop through the tuple items by using a for loop.
i = ("apple", "banana", "cherry")
for x in i:
  print(x)
     
     
repeated_number = 5  # Number to repeat
repetitions = 3  # Number of repetitions

repeated_tuple = tuple(range(repeated_number)) * repetitions

print("Tuple with repeated elements:", repeated_tuple) 
# Output: Tuple with repeated elements: (0, 1, 2, 3, 4, 0, 1, 2, 3, 4)

tuple = ("apple", "banana", "cherry")
i = 0
while i < len(tuple):
  print(tuple[i])
  i = i + 1
     
     
# Dictionary
# Representing a person object
person = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY'
    }
}

# Accessing nested data
print(person['name'])  
print(person['address']['city'])  

# Configuration settings for an application
config = {
    'debug': True,
    'log_file': 'app.log',
    'database': {
        'host': 'localhost',
        'user': 'root',
        'password': 'secret'
    }
}

# Accessing configuration values
debug_mode = config['debug']
log_file = config['log_file']
db_host = config['database']['host']

# Counting word occurrences in a sentence
sentence = "Hello, world! Hello, Python!"
word_counts = {}

for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)  


# Data manipulation and filtering
data = [
    {'name': 'John', 'age': 25, 'city': 'New York'},
    {'name': 'Jane', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Bob', 'age': 35, 'city': 'Chicago'}
]

# Filtering data based on a condition
filtered_data = [person for person in data if person['age'] > 30]
print(filtered_data)  

# Grouping data by city
grouped_data = {}
for person in data:
    city = person['city']
    if city in grouped_data:
        grouped_data[city].append(person)
    else:
        grouped_data[city] = [person]

print(grouped_data)



# List of numbers
numbers = [1, 2, 3, 4, 5]

# Dictionary with squares of numbers
squares = {num: num**2 for num in numbers}
print(squares)


# Original dictionary
original = {'a': 1, 'b': 2, 'c': 3}

# New dictionary with keys and values swapped
swapped = {value: key for key, value in original.items()}
print(swapped)

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dictionary with even numbers as keys and their cubes as values
even_cubes = {num: num**3 for num in numbers if num % 2 == 0}
print(even_cubes)


# List of keys
keys = ['a', 'b', 'c', 'd', 'e']

# List of values
values = [1, 2, 3, 4, 5]

# Dictionary from keys and values
new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)


# Sets
# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
print("Union:",union_set)


grocery_list = {"apples", "bananas", "milk", "bread"}
household_list = {"detergent", "paper towels", "milk", "bread"}

shopping_list = grocery_list | household_list

print("Shopping list:",shopping_list)


# Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2  # Output: {3}
print("Intersection:",intersection_set)

# Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2  # Output: {1, 2}
print("Difference:",difference_set)