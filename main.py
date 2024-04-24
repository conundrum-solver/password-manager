from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

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
    if website == "" or username == "" or user_password == "":
        messagebox.showwarning(title="Missing info", message="Some information is missing")

    else:
        is_ok = messagebox.askokcancel(title="Add password?", message="Add information to database?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {user_password}" + "\n")
        website_entry.delete(0, 'end')
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        website_entry.focus()

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

website_entry = Entry(width=39, justify="left")
website_entry.grid(sticky=W, row=1, column=1, columnspan=2)

website_entry.focus()

username_entry = Entry(width=39, justify="left")
username_entry.grid(sticky=W, row=2, column=1, columnspan=2)

password_entry = Entry(width=21, justify="left")
password_entry.grid(sticky=W, row=3, column=1)

password_button = Button(text="Generate Password", justify="left", command=generate_password)
password_button.grid(sticky=W, row=3, column=2)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(sticky=W, row=4, column=1, columnspan=2)



window.mainloop()
