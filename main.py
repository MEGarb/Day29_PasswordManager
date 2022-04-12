import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_entry.get()
    user = user_entry.get()
    passwrd = password_entry.get()

    if len(web) <= 0 or len(user) <= 0 or len(passwrd) <= 0:
        messagebox.showinfo(title="Empty fields are not permitted.", message="You have left a field empty. Please fill out all fields")

    elif messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {user}"
                           f"\nPassword: {passwrd} \nIs it ok to save?"):
        file = open("data.txt", 'a')
        file.write(f"{web}  ||  {user}  ||  {passwrd}\n")
        file.close()
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.insert(0, "fake@gmailfake.com")
user_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command= generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width= 36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
