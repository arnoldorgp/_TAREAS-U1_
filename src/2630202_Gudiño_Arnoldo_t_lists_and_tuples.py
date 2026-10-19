# COVER
"""
HANDLING LISTS AND TUPLES IN PYTHON

Name: Arnoldo René Gudiño Ponce
Student ID: 2630202
Group: MEC-01
"""

# EXECUTIVE SUMMARY
"""
In this activity, I worked with lists and tuples in Python. I used a list
to store shopping items, add a new product, count the items, and search
for a product. I also used tuples to store two points and calculate the
distance and midpoint between them. The program asks the user to enter
data and checks if the information is valid.
"""

# PRINCIPLES AND BEST PRACTICES
"""
- Lists are useful when we need to add or remove items.
- Tuples are useful for storing data that does not change.
- Use clear variable names to understand the code.
- Show messages to help the user know what to enter.
"""


# PROBLEM 1: SHOPPING LIST BASICS
"""
Problem 1: Shopping list basics (list operations)
Description:
Creates a shopping list from items separated by commas. It adds a new
item, counts the total items, and checks if a specific item is in the list.

Inputs:
- initial_items_text (string)
- new_item (string)
- search_item (string)

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- The initial text must not be empty.
- Extra spaces are removed and empty elements are avoided.
- New and search data must not be empty.

Test cases:
1) Normal: initial="apple, banana", new="orange", search="banana" -> Found: true
2) Border: initial=" milk ", new="bread", search="milk" -> Found: true
3) Error: initial=" ", new="", search="" -> Error: invalid input
"""

print(" PROBLEM 1: SHOPPING LIST BASICS ")

initial_items_text = input("Enter initial items separated by commas: ")
new_item = input("Enter a new item to add: ")
search_item = input("Enter an item to search: ")

if not initial_items_text.strip() or not new_item.strip() or not search_item.strip():
    print("Error: invalid input")
else:
    items_list = [item.strip() for item in initial_items_text.split(",")]
    
    clean_list = []
    for item in items_list:
        if item != "":
            clean_list.append(item)
    items_list = clean_list

    items_list.append(new_item.strip())
    
    total_items = len(items_list)
    found = search_item.strip() in items_list

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", str(found).lower())


# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
"""
Problem 2: Points and distances with tuples
Description:
Uses tuples to represent two points in a plane (x1, y1) and (x2, y2). 
Calculates the distance between them and finds their midpoint.

Inputs:
- x1, y1, x2, y2 (float)

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validations:
- Verify that the inputs can be converted to decimal numbers (float).

Test cases:
1) Normal: 0.0, 0.0, 3.0, 4.0 -> Distance: 5.0, Midpoint: (1.5, 2.0)
2) Border: 1.5, -2.5, 1.5, 2.5 -> Distance: 5.0, Midpoint: (1.5, 0.0)
3) Error: "abc", 1.0, 2.0, 3.0 -> Error: invalid input
"""

print("\n PROBLEM 2: POINTS AND DISTANCES WITH TUPLES ")

try:
    input_x1 = input("Enter x1: ")
    input_y1 = input("Enter y1: ")
    input_x2 = input("Enter x2: ")
    input_y2 = input("Enter y2: ")

    x1 = float(input_x1)
    y1 = float(input_y1)
    x2 = float(input_x2)
    y2 = float(input_y2)

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    midpoint = (mid_x, mid_y)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: invalid input")


# CONCLUSIONS
"""
In this activity, I learned how to work with lists and tuples in Python.
I used a list to manage shopping items and a tuple to store the coordinates
of two points. I also learned how to add items, search for information,
and calculate the distance between points. These exercises helped me
understand how lists and tuples work.
"""


# REFERENCES
"""
1. Python Software Foundation. Data Structures.
https://docs.python.org/3/tutorial/datastructures.html

2. Real Python. Python Lists and Tuples.
https://realpython.com/python-lists-tuples/

3. W3Schools. Python Lists.
https://www.w3schools.com/python/python_lists.asp

4. Programiz. Python List.
https://www.programiz.com/python-programming/list

5. GeeksforGeeks. Python Lists.
https://www.geeksforgeeks.org/python-lists/
"""