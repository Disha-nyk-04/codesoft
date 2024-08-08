
import customtkinter as ctk
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import pickle
import os

def add_task():
    task = task_entry.get()
    if task:
        todo_list.insert(tk.END, task)
        task_entry.delete(0, ctk.END)
    else:
        messagebox.showwarning("Attention", "Please enter a task!")

def delete_task():
    try:
        selected_task = todo_list.curselection()[0]
        todo_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Attention", "Please select a task to delete!")

def save_tasks():
    tasks = todo_list.get(0, ctk.END)
    with open("tasks.dat", "wb") as f:
        pickle.dump(tasks, f)
        messagebox.showinfo("Info", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.dat", "rb") as f:
            tasks = pickle.load(f)
            todo_list.delete(0, ctk.END)
            for task in tasks:
                todo_list.insert(ctk.END, task)
    except FileNotFoundError:
        messagebox.showwarning("Attention", "No saved tasks found!")

window = ctk.CTk()
window.title("NOTE TAKER")
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=1)

icon_path = os.path.abspath("todolist/edit.ico")

# Ensure the image file exists
image_path = "todolist/my_image.png"
if os.path.exists(image_path):
    bg = tk.PhotoImage(file=image_path)
else:
    messagebox.showwarning("Attention", f"Image file '{image_path}' not found!")
    bg = None

label1 = ctk.CTkLabel(window, image=bg)
label1.place(x=0, y=0)

label2 = ctk.CTkLabel(window, text="YOUR TODO LIST", text_color="#000000", bg_color="#FF82AB", padx=5, pady=5, anchor="center")
label2.grid(row=0, column=0, padx=0, pady=0)

task_entry = ctk.CTkEntry(window, width=130, fg_color="#FFF68F")
task_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

todo_list = tk.Listbox(window,
                       bg="#FF82AB",
                       selectmode=tk.EXTENDED,
                       cursor="pencil",
                       selectbackground="#FFE4C4",
                       font="helvetica",
                       activestyle="dotbox",
                       relief="solid",
                       selectforeground="#FF4040")
todo_list.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

frame = ctk.CTkFrame(window, fg_color="#00E5EE")
frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

if bg:
    label = ctk.CTkLabel(frame, image=bg)
    label.place(x=0, y=0)

add_button = ctk.CTkButton(frame,
                           fg_color="#FF82AB",
                           corner_radius=20,
                           text_color="black",
                           text="Add Task",
                           command=add_task)
delete_button = ctk.CTkButton(frame,
                              fg_color="#FF82AB",
                              corner_radius=20,
                              text_color="black",
                              text="Delete Task",
                              command=delete_task)
save_button = ctk.CTkButton(frame,
                            fg_color="#FF82AB",
                            corner_radius=20,
                            text_color="black",
                            text="Save Tasks",
                            command=save_tasks)
load_button = ctk.CTkButton(frame,
                            corner_radius=20,
                            fg_color="#FF82AB",
                            text_color="black",
                            text="Load Tasks",
                            command=load_tasks)

add_button.grid(row=1, column=0, padx=10, pady=5)
delete_button.grid(row=2, column=0, padx=10, pady=5)
save_button.grid(row=3, column=0, padx=10, pady=5)
load_button.grid(row=4, column=0, padx=10, pady=5)

ctk.set_appearance_mode("light")

def on_resize(event):
    new_width = event.width
    new_height = event.height

window.bind("<Configure>", on_resize)
window.mainloop()
