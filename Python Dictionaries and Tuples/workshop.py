# Python Dictionary Lesson
# A dictionary in Python is a collection of key-value pairs. Each key is associated with a value, and both the keys and values can be of any data type. (By convention, keys are usually strings)

#1. Creating a Dictionary: Create a dictionary by enclosing key-value pairs in curly braces {}, seperated by colons :
# Empty Dictionary
my_dict = {}

# Dictionary with values
person = {
    "name": "christian",
    "age": 99,
    "city": "Farmington"
}



#2. Accessing Values: You can access values in a dictionary by using their keys inside square brackets []
# NOTE: If the key doesn't exist, python will raise a "KeyError". To avoid this, you can use the .get() method which returns "None"(or a default value).
# Accessing values by key
firstName = person["name"]
age = person.get("ageee", "Key does not exist")
print(age)

#3. Adding and Modifying Values: You can add a new key-value pair or modify an existing one by assigning a value to a key.
# Adding a new key-value pair
person["instructor"] = True
print(person)

# Modifying an existing key-value pair
person["age"] = 100
print(person)



#4. Removing Values: You can remove key-value pairs using the del statement(), .pop(), or .popitem()
# Remove a specific key-value pair
del person["city"]
print(person)

# Using .pop() to remove and return the value
name = person.pop("name")
print(name)
print(person)



#5. Dictionary Methods:
# .keys(): returns all keys in the dictionary
# .values(): returns all values
# .items(): returns all key-value pairs as tuples
print(person.keys())
print(person.values())
print(person.items())


#6. Iterating through a dictionary: looping with for loop
# looping through keys
for key in person.keys():
    print(key)

# looping through key-value pairs
for key, value in person.items():
    print(key, value)


#7. Nesting Dictionaries
people = {
    "student1": {
        "name": "Amilcar",
        "age": 101
    },
    "student2": {
        "name": "Rene",
        "age": 102,
        "favTeam": {
            "name": "Seahawks",
            "city": "Seattle",
            "players": ["dk metcalf", "tyler lockett", "geno smith"]
        }
    }
}
print(people)

# accessing values in a nested dictionary
print(people["student2"]["favTeam"]["players"][1])


#8. Common Operations with Dictionaries
# Checking if a key exists: use the "in" keyword
if "favTeam" in people["student2"]:
    print("Found favorite team")

# Dictionary Length: Use len() to get the number of key-value pairs
print(len(people["student2"]["favTeam"]))




# Python Tuples Lesson
# A tuple is a collection of items that is ORDERED and IMMUTABLE. Tuples are similar to lists, but with immutability and faster performance.

#1. Creating a Tuple
my_tuple = (1,2,3)
print(my_tuple)

# Tuples can contain elements of different data types
mixed_tuple = (12, 3, "apples")
print(mixed_tuple)

# Single Element Tuple: You need to add a comma after the element, otherwise Python will treat it as a simple value.

# without comma, its not a tuple
single_ele_tuple = (1,)
print(single_ele_tuple)


#2. Accessing Tuple Elements: Tuples are indexed, just like lists.
fruits = ("peaches", "oranges", "strawberries", "blueberries", "pineapple")
print(fruits[1])



#3. Slicing a Tuple: Slice a tuple to access a range of elements
print(fruits[:-1])