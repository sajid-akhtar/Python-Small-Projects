from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password_func():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()

    try:
        with open("D:/Python/python/Password-Manager-GUI/data.json") as file1:
            data = json.load(file1)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No Details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("D:/Python/python/Password-Manager-GUI/data.json", "r") as file1:
                data = json.load(file1)
        except FileNotFoundError:
            with open("D:/Python/python/Password-Manager-GUI/data.json", "w") as file1:
                json.dump(new_data, file1, indent=4)
        else:
            data.update(new_data)
            with open("D:/Python/python/Password-Manager-GUI/data.json", "w") as file1:
                json.dump(data, file1, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas Setup
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="D:/Python/python/Password-Manager-GUI/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label 1 - Website
website_label = Label(text="Website: *")
website_label.grid(row=1, column=0)

# Label 2 - Email/Username
email_label = Label(text="Email/Username: *")
email_label.grid(row=2, column=0)

# Label 3 - EPassword
password_label = Label(text="Password: *")
password_label.grid(row=3, column=0)

# Entry 1 - Input for website
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

# Entry 2 - Input for email
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "abc@xyz.com")

# Entry 3 - Input for Password
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")


# Button 1 - Generate Password
generate_password = Button(text="Generate Password",
                           command=generate_password_func)
generate_password.grid(row=3, column=2, sticky="EW")

# Button 2 - Add
add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2, sticky="EW")

# Button 3 - Search
search = Button(text="Search", command=find_password, width=13)
search.grid(row=1, column=2, sticky="EW")

window.mainloop()
