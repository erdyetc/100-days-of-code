#Join 
"""list1 = ["a", "c", "b"]
string1 = "".join(list1)
print(string1)"""

#Function with no input
def greet():
    print("Hello")
    print("My name is Dex")
    print("I am a computer")

#Function with one input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"My name is Dex. Nice to meet you {name}")
    print("I am a computer")

#Functions with more than 1 input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location="Mexico",name="Edwina")

