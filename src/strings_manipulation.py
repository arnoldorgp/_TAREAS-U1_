# STRING HANDLING IN PYTHON

# Name: Arnoldo René Gudiño Ponce
# Student ID: 2630202
# Group: MEC-01


# SUMMARY

"""
A string is a data type used to store text.
Strings are immutable, so they cannot be changed directly.
We can do operations like joining text, getting its length,
searching for words and getting parts of a text.
We can also use uppercase and lowercase letters to organize
the information.
In this activity we work with different string problems.
We also use validations to avoid some errors.
"""


# PROBLEM 1
# Full name formatter

"""
Description:
A full name is requested and it is displayed correctly.
The initials are also displayed.

Input:
Full name.

Output:
Formatted name and initials.

Validations:
The name cannot be empty and must have at least two words.

Test cases:
Normal: juan carlos tovar
Border: Ana Perez
Error: "   "
"""

def format_full_name():
    full_name = input("Write your full name: ")
    full_name = full_name.strip()

    if len(full_name) == 0:
        print("Error: invalid input")
        return

    words = full_name.split()

    if len(words) < 2:
        print("Error: enter at least two words")
        return

    formatted_name = []
    for word in words:
        formatted_name.append(word.title())

    formatted_name = " ".join(formatted_name)

    initials = ""
    for word in words:
        initials = initials + word[0].upper() + "."

    
    print("no se crea profe, si lo hice yo, ahi va el bueno")
   
format_full_name()

while True:
    full_name = input("Write your full name: ")
    full_name = full_name.strip()

    if len(full_name) == 0:
        print("Error: invalid input")
        print("Try again")

    else:
        words = full_name.split()

        if len(words) < 2:
            print("Error: enter at least two words")
            print("Try again")

        else:
            formatted_name = []

            for word in words:
                formatted_name.append(word.title())

            formatted_name = " ".join(formatted_name)

            initials = ""

            for word in words:
                initials = initials + word[0].upper() + "."

            print("Formatted name:", formatted_name)
            print("Initials:", initials)

            break

# PROBLEM 2
# Simple email validator

"""
Description:
An email is checked to see if it has a basic correct format.

Input:
An email address.

Output:
If the email is valid and its domain.

Validations:
The email cannot be empty, must have only one @
and must have a dot after the @.

Test cases:
Normal: arnoldo@gmail.com
Border: a@b.c
Error: arnoldo gmail.com
"""

while True:

    email_text = input("\nWrite your email: ")

    email_text = email_text.strip()

    if len(email_text) == 0:

        print("Error: invalid input")
        print("Try again")

    else:

        at_positions = []

        for i in range(len(email_text)):

            if email_text[i] == "@":
                at_positions.append(i)

        has_space = False

        for letter in email_text:

            if letter == " ":
                has_space = True

        if len(at_positions) != 1:

            print("Valid email: false")
            print("Try again")

        elif has_space:

            print("Valid email: false")
            print("Try again")

        else:

            at_position = at_positions[0]

            domain = email_text[at_position + 1:]

            if "." in domain and len(domain) > 2:

                print("Valid email: true")
                print("Domain:", domain)

                break

            else:

                print("Valid email: false")
                print("Try again")


# PROBLEM 3
# Palindrome checker

"""
Description:
A phrase is checked to see if it reads the same from left
to right and from right to left.

Input:
A phrase.

Output:
Indicates if it is a palindrome.

Validations:
The phrase cannot be empty and must have at least 3 characters.

Test cases:
Normal: Anita lava la tina
Border: ana
Error: "   "
"""

phrase = input("\nWrite a phrase: ")

phrase = phrase.strip()

if len(phrase) == 0:

    print("Error: invalid input")

else:

    clean_phrase = ""

    words = phrase.split()

    for word in words:
        clean_phrase = clean_phrase + word

    clean_phrase = clean_phrase.lower()

    if len(clean_phrase) < 3:

        print("Error: phrase is too short")

    else:

        reverse_phrase = clean_phrase[::-1]

        if clean_phrase == reverse_phrase:

            print("Is palindrome: true")

        else:

            print("Is palindrome: false")

# PROBLEM 4
# Sentence word stats

"""
Description:
A sentence is received and information about its words
is obtained.

Input:
A sentence.

Output:
Number of words, first, last, shortest and longest word.

Validations:
The sentence cannot be empty.

Test cases:
Normal: Python is an easy language
Border: Hello world
Error: "   "
"""

while True:

    sentence = input("\nWrite a sentence: ")

    sentence = sentence.strip()

    if len(sentence) == 0:

        print("Error: invalid input")
        print("Try again")

    else:

        words = sentence.split()

        if len(words) == 0:

            print("Error: no words")
            print("Try again")

        else:

            shortest_word = words[0]
            longest_word = words[0]

            for word in words:

                if len(word) < len(shortest_word):
                    shortest_word = word

                if len(word) > len(longest_word):
                    longest_word = word

            print("Word count:", len(words))
            print("First word:", words[0])
            print("Last word:", words[-1])
            print("Shortest word:", shortest_word)
            print("Longest word:", longest_word)

            break


# PROBLEM 5
# Password strength classifier

"""
Description:
A password is classified as weak, medium or strong.

Weak:
Less than 8 characters.

Medium:
8 or more characters but does not have everything needed
for a strong password.

Strong:
8 or more characters, uppercase, lowercase, number
and symbol.

Input:
A password.

Output:
Password strength.

Validations:
The password cannot be empty.

Test cases:
Normal: Hola1234!
Border: hola1234
Error: "   "
"""

while True:

    password_input = input("\nWrite a password: ")

    password_input = password_input.strip()

    if len(password_input) == 0:

        print("Error: invalid input")
        print("Try again")

    else:

        has_upper = False
        has_lower = False
        has_number = False
        has_symbol = False

        for letter in password_input:

            if letter.isupper():
                has_upper = True

            if letter.islower():
                has_lower = True

            if letter.isdigit():
                has_number = True

            if not letter.isalnum():
                has_symbol = True

        if len(password_input) < 8:

            print("Password strength: weak")

        elif has_upper and has_lower and has_number and has_symbol:

            print("Password strength: strong")

        else:

            print("Password strength: medium")

        break


# PROBLEM 6
# Product label formatter

"""
Description:
A label is created with the product name and its price.
The label must have exactly 30 characters.

Input:
Product name and price.

Output:
A 30-character label.

Validations:
The product name cannot be empty.
The price must be a positive number.

If the label has more than 30 characters, a warning
is displayed and the name and price are requested again.

Test cases:
Normal: Mouse / 250
Border: Pan / 20
Error: empty product
More than 30 characters: Product: rubik´s cube | Price: $10
"""

while True:

    product_name = input("\nWrite the product name: ")

    price_value = input("Write the price: ")

    product_name = product_name.strip()
    price_value = price_value.strip()

    if len(product_name) == 0:

        print("Error: invalid product")
        print("Try again")

    elif len(price_value) == 0:

        print("Error: invalid price")
        print("Try again")

    else:

        try:

            price_number = float(price_value)

            if price_number <= 0:

                print("Error: the price must be positive")
                print("Try again")

            else:

                label = "Product: " + product_name + " | Price: $" + price_value

                if len(label) > 30:

                    print("Error: the label has more than 30 characters")
                    print("Try again")

                else:

                    spaces = 30 - len(label)

                    for i in range(spaces):
                        label = label + " "

                    print('Label: "' + label + '"')

                    break

        except ValueError:

            print("Error: the price must be a number")
            print("Try again")


# CONCLUSIONS

"""
In this activity I learned that strings are used to work
with text.
I learned to use strip() to remove unnecessary spaces.
We also used split() to separate words from a sentence.
lower() and upper() are used to work with uppercase and
lowercase letters.
Slicing is used to get part of a string.
I also learned that strings are immutable, so when we make
changes, a new string is created.
Validations help prevent the program from receiving
incorrect data.
"""


# REFERENCES

# 1. Python Documentation - Built-in Types.
# https://docs.python.org/3/library/stdtypes.html

# 2. Python Documentation - Built-in Functions.
# https://docs.python.org/3/library/functions.html

# 3. W3Schools - Python Strings.
# https://www.w3schools.com/python/python_strings.asp

# 4. W3Schools - Python String Methods.
# https://www.w3schools.com/python/python_ref_string.asp

# 5. Programiz - Python Strings.
# https://www.programiz.com/python-programming/string