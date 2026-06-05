import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password
import pyperclip as pyper
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def get_password():
    clear_password()
    password = generate_password()
    password_entry.insert(0, password)
    pyper.copy(password)
    messagebox.showinfo(title="Password Manager Info", message="Password has been copied to clipboard!")

# ---------------------------- CLEAR PASSWORD ------------------------------- #

def clear_password():
    password_entry.delete(0, "end")

# ---------------------------- SAVE PASSWORD INTO PASSWORD DATABASE ------------------------------- #

def save_data():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    data_dict = {website:{"email": email_username, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Password Manager Warning!", message="Please make sure all fields are filled!")
    else:
        save_flag = messagebox.askokcancel(title = website, message = f"These are the details of the user:\n"
                                                                      f"e-mail: {email_username}\n"
                                                                      f"password: {password}\nIs this correct?")
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data_dict, file, indent = 4)
        else:
            if save_flag:
                data.update(data_dict)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent = 4)
                website_entry.delete(0, "end")
                email_username_entry.delete(0, "end")
                email_username_entry.insert(0, "example@email.com")
                password_entry.delete(0, "end")
            else:
                website_entry.delete(0, "end")
                email_username_entry.delete(0, "end")
                email_username_entry.insert(0, "example@email.com")
                password_entry.delete(0, "end")
        finally:
            website_entry.delete(0, "end")
            email_username_entry.delete(0, "end")
            email_username_entry.insert(0, "example@email.com")
            password_entry.delete(0, "end")

# ---------------------------- RETRIEVE FROM DATABASE ------------------------------- #

def search_data():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Password Manager Update", message="Database missing.")
    else:
        if website in data.keys():
            email_username= data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"E-mail/User Name: {email_username}\n"
                                                           f"Password: {password}\n")
        else:
            messagebox.showinfo(title = "Password Manager Update", message = f"Data for {website} not found!")

# ---------------------------- RESET PASSWORD DATABASE ------------------------------- #

def reset_data():
    with open("data.json", "w") as file:
        json.dump({}, file)
    messagebox.showinfo(title = "Password Manager Update" , message = "Password Database is empty!")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.minsize(200, 200)
window.configure(padx = 50, pady = 50, bg = "white")

canvas = tk.Canvas(window, width = 200, height = 200, bg = "white", highlightthickness = 0)
logo = tk.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 1, column = 1)

title_label = tk.Label(text = "Password Manager", font = ("Arial", 12, "bold"))
title_label.config(fg = "red", bg = "white")
title_label.grid(row = 0, column = 1)

website_label = tk.Label(text = "Website:", font = ("Arial", 12, "bold"))
website_label.config(fg = "black", bg = "white")
website_label.grid(row = 2, column = 0)

email_username_label = tk.Label(text = "E-mail/User Name:", font = ("Arial", 12, "bold"))
email_username_label.config(fg = "black", bg = "white")
email_username_label.grid(row = 3, column = 0)

password_label = tk.Label(text = "Password:", font = ("Arial", 12, "bold"))
password_label.config(fg = "black", bg = "white")
password_label.grid(row = 4, column = 0)

website_entry = tk.Entry(width = 44, font = ("Arial", 12, "bold"))
website_entry.grid(row = 2, column = 1, columnspan = 2, pady = 5)
website_entry.focus()

email_username_entry = tk.Entry(width = 44, font = ("Arial", 12, "bold"))
email_username_entry.grid(row = 3, column = 1, columnspan = 2, pady = 5)
email_username_entry.insert(0, "example@email.com")

password_entry = tk.Entry(width = 24, font = ("Arial", 12, "bold"))
password_entry.grid(row = 4, column = 1, pady = 5)

generate_password_button = tk.Button(text = "Generate Password", width = 21, font = ("Arial", 10, "bold"),
                                     command = get_password)
generate_password_button.config(fg = "black", bg = "white")
generate_password_button.grid(row = 4, column = 2, columnspan = 2, pady = 5)

add_button = tk.Button(text = "Add", width =40, font = ("Arial", 12, "bold"), command = save_data)
add_button.config(fg = "black", bg = "white")
add_button.grid(row = 5, column = 1, columnspan = 2,pady = 5)

clear_password_button = tk.Button(text = "Clear Password", width = 40, font = ("Arial", 12, "bold"),
                                  command = clear_password)
clear_password_button.config(fg = "black", bg = "white")
clear_password_button.grid(row = 6, column = 1, columnspan = 2,pady = 5)

reset_data_button = tk.Button(text = "Reset Database", width = 40, font = ("Arial", 12, "bold"), command = reset_data)
reset_data_button.config(fg = "black", bg = "white")
reset_data_button.grid(row = 7, column = 1, columnspan = 2,pady = 5)

search_data_button = tk.Button(text = "Search Database", width = 40, font = ("Arial", 12, "bold"),
                               command = search_data)
search_data_button.config(fg = "black", bg = "white")
search_data_button.grid(row = 8, column = 1, columnspan = 2,pady = 5)

window.mainloop()
