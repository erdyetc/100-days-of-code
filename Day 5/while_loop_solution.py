#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

allchar = letters + numbers + symbols
totalchar = nr_letters + nr_symbols + nr_numbers
password = []
count_letter = 0
count_symbol = 0
count_number = 0
while len(password) < totalchar:
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
            password.append(char)


for n in range(0,len(password)):
    password[n] = str(password[n])
print(''.join(password))