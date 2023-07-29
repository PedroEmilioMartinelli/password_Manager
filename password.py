import random

print("Hello, I am a software password manager")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}*;/,._-"

all = lower + upper + number + symbols

length = input("How many characters do you want in the password?\n" + "ps: max 60 characters\n")

if int(length) <=60:
    password = "".join(random.sample(all,int(length)))
    print("Your password is:\n" + password)
else:
    print("the maximum number of characters I can generate is 60. Please reduce the character count so I can create your password")
    exit()












