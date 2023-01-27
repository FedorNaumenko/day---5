# Random password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3', '4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', '<', '>', ',' '.', '/', '?']

print("Welcome to the PyPas Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = random.sample(letters, nr_letters)
password_symbols = random.sample(symbols, nr_symbols)
password_numbers = random.sample(numbers, nr_numbers)

new_password = password_letters + password_symbols + password_numbers
random.shuffle(new_password)
result = ' '.join(new_password)
print(result)

