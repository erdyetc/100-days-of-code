#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""password = ""
for nrletter in range(0, nr_letters):
    letter = random.choice(letters)
    password += str(letter)
for nrsymbol in range(0, nr_symbols):
    symbol = random.choice(symbols)
    password += str(symbol)
for nrnumber in range(0, nr_numbers):
    number = random.choice(numbers)
    password += str(number)
print(password)
"""
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
allchar = letters + numbers + symbols
totalchar = nr_letters + nr_symbols + nr_numbers
password = []
count_letter = 0
count_symbol = 0
count_number = 0
"""for nrchar in range(0, totalchar):
    char = random.choice(allchar)
    if char in letters:
        count_letter += 1
        if count_letter <= nr_letters:
            password.append(char)
    if char in symbols:
        count_symbol += 1
        if count_symbol <= nr_symbols:
            password.append(char)
    if char in numbers:
        count_number += 1
        if count_number <= nr_letters:
            password.append(char)"""

"""for n in range(0,len(password)):
    password[n] = str(password[n])
print(''.join(password))

I think I need a "while" loop for this method work --> the number of loops is not defined
"""

password = []
for nrletter in range(0, nr_letters):
    letter = random.choice(letters)
    password.append(letter)
for nrsymbol in range(0, nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)
for nrnumber in range(0, nr_numbers):
    number = random.choice(numbers)
    password.append(number)
    #can also just do: password.append(random.choice(numbers))

random.shuffle(password)
for n in range(0,len(password)):
    password[n] = str(password[n])
print(''.join(password))

"""can also do:
password_str = ""
for char in password:
    password_str += char
print(password_str)
"""