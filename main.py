from tkinter import *

from tkinter import messagebox

from random import choice

import pyperclip

import json
# ---------------------------- SEARCH ENGINE ------------------------------- #
def search():   
    "Search your website account if it's exist"
    website_text = website_entry.get().capitalize()
    # global new_account_list
    
    try:
        with open ("data.json",'r') as data_file:
            data = json.load(data_file)
            your_username = data[website_text]['Username']
            your_password = data[website_text]['Password']
        if user_name_entry.get()!='' or password_entry.get()!='':
            messagebox.showerror(title="Error",message="Only Website box needed")
            user_name_entry.delete(0,END)
            password_entry.delete(0,END)
        else:
            messagebox.showinfo(title="Your Account",message=f"Username: {your_username}\n\nPassword: {your_password}\n\nThe password has been copied to your clipboard")
            pyperclip.copy(your_password.replace("Password: ",""))
    except KeyError as web:
        if website_text=='':
            messagebox.showerror(title="Error",message="Please type in the Website box")
        else:
            messagebox.showerror(title="Error",message=f"This {web} website haven't added yet")
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="Don't have any file to read")

        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    "Generate an random password and copy to your clipboard"
    password_entry.delete(0,END)
    ASCII_character = [ chr(i) for i in range(32,127)] 
    random_password=''
    for i in range(13):
        random_password+=choice(ASCII_character)
    password_entry.insert(0,random_password)
    pyperclip.copy(random_password)
    messagebox.showinfo(title='Annoucement',message="It's copied")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    "Get all your website,username,password information"
    web = website_entry.get()
    acc = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        web : {
            'Username':acc,
            'Password':password,
            }
        }
    if len(web)==0 or len(acc)==0 or len(password)==0:
        messagebox.showerror(title="Error",message="You should fill all necessary information")
    else:
        is_ok = messagebox.askokcancel(title="Your account",message=f'{web.capitalize()}\nUsername: {acc}\nPassword: {password}')
        if is_ok:
            try:
                with open('data.json','r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                    print(data)
                with open('data.json','w') as data_file:
                    json.dump(data,data_file,indent=4)
                website_entry.delete(0,END)
                user_name_entry.delete(0,END)
                password_entry.delete(0,END)
            except FileNotFoundError:
                with open('data.json','w') as data_file:
                    json.dump(new_data,data_file,indent=4)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(width=720,height=580,padx=50,pady=50,bg="#D3ECA7")
window.iconbitmap("icon.ico")
window.title("Password Manager")

canvas = Canvas()
canvas.config(width=250,height=250,bg="#D3ECA7",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(130,130,image=logo)
canvas.grid(column=0,row=0,padx=0,pady=10,columnspan=3)

title = Label(text="Password Manager",font=("Arial",30,"bold"),fg="#B33030",bg="#D3ECA7")
title.grid(column=0,row=1,columnspan=3)
website = Label(text="Website:",fg="#19282F",bg="#D3ECA7",font=("Arial",10,"bold"),padx=0,pady=5)
website.grid(column=0,row=2)
website_entry = Entry(width=34,fg="#19282F",bg="white",highlightthickness=1)
website_entry.grid(column=1,row=2,columnspan=1,padx=3)
website_entry.focus()

user_name = Label(text="Email/Username:",fg="#19282F",bg="#D3ECA7",font=("Arial",10,"bold"),padx=0,pady=5)
user_name.grid(column=0,row=3)
user_name_entry = Entry(width=52,fg="#19282F",bg="white",highlightthickness=1)
user_name_entry.grid(column=1,row=3,columnspan=2)

password_text = Label(text="Password:",fg="#19282F",bg="#D3ECA7",font=("Arial",10,"bold"),padx=0,pady=5)
password_text.grid(column=0,row=4)
password_entry = Entry(width=34,fg="#19282F",bg="white",highlightthickness=1)
password_entry.grid(column=1,row=4,padx=3)

generate_password = Button(text='Generate',fg="#19282F",width=14,font=("Arial",8,"bold"),bg="#A1B57D",border=1,command=generate)
generate_password.grid(column=2,row=4)

add_button = Button(text='Add',width=44,font=("Arial",8,"bold"),command=get_data,bg="#A1B57D",fg="#19282F")
add_button.grid(column=1,row=5,columnspan=2)

search_button = Button(text='Search',width=14,font=("Arial",8,"bold"),bg="#A1B57D",border=1,command=search,fg="#19282F")
search_button.grid(column=2,row=2,columnspan=1)

window.mainloop()