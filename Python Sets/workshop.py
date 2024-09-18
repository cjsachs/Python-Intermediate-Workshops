# Python Sets Lesson

# Python sets are unordered collections of unique elements. They are useful when you need to store items without duplicates.
# Mutable, but the elements inside MUST be immutable (strings, numbers, or tuples)


# 1. Creating a Set: You can create a set using either curly braces{}, or the set() function.
# NOTE: Curly braces are used for dictionaries as well, so the way python differentiates the two is if a key:value pair was given or not.
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

my_set_again = set()
print(my_set_again)
print(type(my_set_again))


# Python will assume dictionary type with empty {}





# 2. Set Operations
# Adding Elements: Use .add() to add an element to a set.
my_set.add(6)
print(my_set)


# Remove Elements: .remove() to remove an element (throws an error if the element does not exist)
try:
    my_set.remove(7)
    print(my_set)
except:
    print("Key does not exist!")


# Checking for Membership: Use "in" or "not in" to check if an element is present in the set
if (10 in my_set):
    print("Found your number!")
else:
    print("Number not found!")

    
# Total Count of Elements: Return the number of elements with len()
print(len(my_set))


# Copy a Set With .copy()
my_set_copy = my_set.copy()
print(my_set)
print(my_set_copy)



# Clear All Elements: Remove all elements with .clear()
my_set_copy.clear()
print(my_set_copy)






# 3. Set Operations with Multiple Sets
# Union: .union() or "|" operator: combines all unique elements from both sets
set1 = {1,2,3}
set2 = {2,3,4}
combined_set = set1.union(set2)
print(combined_set)
combined_set_again = set1 | set2
print(combined_set_again)


# Intersection: .intersection() or "&" operator: returns elements that are common in both sets.
common_set = set1.intersection(set2)
print(common_set)
common_set_again = set1 & set2
print(common_set_again)

# Difference: .difference() or "-" operator: returns elements present in the first set but not in the second.
differ_set = set2.difference(set1)
print(differ_set)
differ_set_again = set1 - set2
print(differ_set_again)


# Symmetric Difference: .symmetric_difference() or "^": returns elements that are in either of the sets, but not both.
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)
symmetric_diff_again = set2 ^ set1
print(symmetric_diff)


# 4. Common Examples
# Remove Duplicates from a List
my_list = [1,2,2,3,4,4,5,5,5]
unique_elements = set(my_list)
print(unique_elements)


# Finding Common Items in Two Lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common_items = set(list1).intersection(set(list2))
print(common_items)