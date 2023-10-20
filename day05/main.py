import string
import random

length = int(input("Enter password length: "))

num_upper = int(input("Enter number of uppercase letters: "))
num_lower = int(input("Enter number of lowercase letters: "))
num_digits = int(input("Enter number of digits: "))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits

total = num_upper + num_lower + num_digits

if total > length:
    print("Total number of characters exceeds password length")
else:
    password = []

    for i in range(num_upper):
        password.append(random.choice(upper))

    for i in range(num_lower):
        password.append(random.choice(lower))

    for i in range(num_digits):
        password.append(random.choice(digits))

    # If total characters is less than password length
    # add random characters to make it equal to length
    if total < length:
        characters = upper + lower + digits
        for i in range(length - total):
            password.append(random.choice(characters))

    # Shuffle the password characters randomly
    random.shuffle(password)

    # Convert password list to string
    password = "".join(password)

    print(password)
