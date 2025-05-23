import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0','1','2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=','+',]

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy level
password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters)) # Used append method to append the elements in list.

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))


print(password_list)

#used shuffle method to shuffle the list.

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}.")
