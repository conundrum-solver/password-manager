from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    user_password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": user_password,
        }
    }
    if len(website) == 0 or len(username) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Missing info", message="Some information is missing")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            info = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="Data file doesn't exist. Save a new password to get "
                                                             "started")
    else:
        if website in info:
            user = info[website]["username"]
            password = info[website_entry.get()]["password"]
            messagebox.showinfo(title="Search result", message=f"Username: {user}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Website not found",
                                 message="The data file doesn't contain information for this site. Check the spelling "
                                         "and try again")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
app_icon = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_icon)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website: ", bg="white", highlightthickness=0)
website_label.grid(sticky=W, row=1, column=0)

username_label = Label(text="Email/Username: ", bg="white", highlightthickness=0, justify="left")
username_label.grid(sticky=W, row=2, column=0)

password_label = Label(text="Password: ", bg="white", highlightthickness=0, justify="left")
password_label.grid(sticky=W, row=3, column=0)

website_entry = Entry(width=21, justify="left")
website_entry.grid(sticky=W, row=1, column=1, columnspan=2)

website_entry.focus()

username_entry = Entry(width=39, justify="left")
username_entry.grid(sticky=W, row=2, column=1, columnspan=2)

password_entry = Entry(width=21, justify="left")
password_entry.grid(sticky=W, row=3, column=1)

search_button = Button(width=14, text="Search", justify="left", command=search)
search_button.grid(sticky=W, row=1, column=2)

password_button = Button(text="Generate Password", justify="left", command=generate_password)
password_button.grid(sticky=W, row=3, column=2)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(sticky=W, row=4, column=1, columnspan=2)

window.mainloop()
