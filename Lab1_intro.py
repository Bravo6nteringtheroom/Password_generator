#Password Generator
import random

#1-length = 16
length = 16
#2-UpperCase array + LowerCase array
letters = "abcdefghijklnmopqrstuvwxyz"
#3-Numbers included in the Password
Number_Set = "1234567890"
#4-Special Symbols included
Special_sybmols = "!@#$%^&*()_+-"

Array = [letters,Number_Set,Special_sybmols]

weight = [50,30,20]

function_case = [str.lower,str.upper]

def generate_password(length,Array,weight):
    generated_password = ""
    for x in range(length):
        current_character = random.choices(Array,weights=weight,k=1)[0]
        symbol = current_character[random.randint(0,len(current_character)-1)]
        # if symbol.isalpha() and random.random() < 0.5:
        #     symbol = symbol.upper()
        # else:
        #     symbol = symbol.lower()
        if symbol.isalpha():
            chosen_case = random.choices(function_case,weights=[80,20],k=1)[0]
            symbol = chosen_case(symbol)
        generated_password += symbol
    return generated_password

print()
for x in range(5):
    print("\033[32m"+"[+]"+generate_password(16,Array,weight)+"\033[0m")
    print()
