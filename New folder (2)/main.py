import tkinter
from tkinter import messagebox
import GUI



window = tkinter.Tk()
window.title("Login form")
window.geometry('600x450')
window.configure(bg='#000000')

def login():
    username = "rasi"
    password = "20041108"
    if username_entry.get()==username and password_entry.get()==password:
        window.destroy()
        GUI.main_window()
    else:
        messagebox.showerror(title="Error", message="Invalid login,Please try again")

frame = tkinter.Frame(bg='#000000')

#creating widgets
login_label = tkinter.Label(
    frame, text="Login",font=("Elephant",20),bg='#000000', fg="#EF9838")
username_label = tkinter.Label(
    frame, text="Username  ",bg='#000000',fg="#ffffff",font=("Arial",15))
username_entry = tkinter.Entry(frame,fg="#000000",font=("Arial",15))
password_entry = tkinter.Entry(frame, show="*",fg="#000000",font=("Arial",15))
password_label = tkinter.Label(
    frame, text="Password  ",bg='#000000',fg="#ffffff",font=("Arial",15))
login_button = tkinter.Button(
    frame, text="Login",bg="#ff1363",font=("Calisto MT",15), command=login)

#Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2,sticky="news",pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1,pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady=20)
login_button.grid(row=3, column=0, columnspan=2,pady=30)

frame.pack()

window.mainloop()