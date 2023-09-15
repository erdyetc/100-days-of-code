import art
#This version uses one function for everything
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_input = True
#Shortened version
def caesar(direction,text,shift):
    final_text = ""
    #Can reverse direction quickly with the below if statement
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            final_position = position + shift
            if final_position > 25:
                final_position -= 26
            elif final_position < 0:
                final_position += 26
            final_text += alphabet[final_position]
        else:
            final_text += char
    if direction == "encode" or direction == "decode":
        print(f"The {direction}d text is {final_text}")
    else:
        print("You did not input \"encode\" or \"decode\"")
    
while continue_input == True:
    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    caesar(direction=direction_input,text=text_input,shift=shift_input)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        continue_input = False
        print("Goodbye")

""" Long version
def caesar(direction,text,shift):
    final_text = ""
    if direction == "encode":
        for char in text:
            final_position = alphabet.index(char)+shift
            if final_position > 25:
                final_position -= 26
                final_text += alphabet[final_position]
            else:
                final_text += alphabet[final_position]
        print(f"The encoded text is {final_text}")
    elif direction == "decode":
        for char in text:
            final_position = alphabet.index(char)-shift
            if final_position < 0:
                final_position += 26
                final_text += alphabet[final_position]
            else:
                final_text += alphabet[final_position]
        print(f"The decoded text is {final_text}")
    else: 
        print("You did not input 'encode' or 'decode'")
""" 

"""This version uses separate functions for encrypt and decrypt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift):
    encryption = ""
    for char in plain_text:
        final_position = alphabet.index(char)+shift
        if final_position > 25:
            final_position -= 26
            encryption += alphabet[final_position]
        else:
            encryption += alphabet[final_position]
    print(f"The encoded text is {encryption}")

def decrypt(cipher_text, shift):
    decryption  = ""
    for char in cipher_text:
        final_position = alphabet.index(char)-shift
        if final_position < 0:
            final_position += 26
            decryption += alphabet[final_position]
        else:
            decryption += alphabet[final_position]
    print(f"The decoded text is {decryption}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction == "encode":
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    encrypt(plain_text=text_input, shift=shift_input)
elif direction == "decode":
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    decrypt(cipher_text=text_input, shift=shift_input)
else:
    print("You did not input 'encode' or 'decode'")
#Could also just double the alphabet in the list because index only gives the indices of the first instance

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

   ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.  

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
"""