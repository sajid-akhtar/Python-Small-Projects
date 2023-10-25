import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator!")

nr_letters = int(input("No of alphabets in the password: "))
nr_numbers = int(input("No of numbers in the password: "))
nr_symbols = int(input("No of special characters in the password: "))

total_characters = nr_letters + nr_numbers + nr_symbols

password_list = []
for i in range(nr_symbols):
    password_list.append(random.choice(symbols))
for i in range(nr_letters):
    password_list.append(random.choice(letters))
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for i in range(len(password_list)):
    password += password_list[i]

print(f"Length of the password generated: {total_characters}")
print(f"Your password: {password}")
