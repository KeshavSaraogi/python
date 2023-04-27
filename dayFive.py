import random

letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_+=?/|"
numbers = "0123456789"

print("Welcome To Random Password Generator!")

letter = int(input("How many letters would you like in your password? "))
symbol = int(input("How many symbols would you like in your password? "))
number = int(input("How many numbers would you like in your password? "))

length = letter + symbol + number
password = ""

for i in range(letter):
    character = random.choice(letters)
    password += character

for i in range(symbol):
    character = random.choice(symbols)
    password += character

for i in range(number):
    character = random.choice(numbers)
    password += character

password = ''.join(random.sample(password, len(password)))
print(password)