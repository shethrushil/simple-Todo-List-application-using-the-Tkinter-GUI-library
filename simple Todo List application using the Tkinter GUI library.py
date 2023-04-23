# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:22:20 2023

@author: rushilsheth
"""

from tkinter import *
from tkinter import messagebox

# Define a function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter a task")

# Define a function to delete a task from the list
def delete_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete")

# Define a function to update a task in the list
def update_task():
    try:
        task_index = task_list.curselection()[0]
        task = task_entry.get()
        if task != "":
            task_list.delete(task_index)
            task_list.insert(task_index, task)
            task_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Please enter a task")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to update")

# Create a new window
window = Tk()
window.title("Todo List")

# Create a frame for the task list
task_frame = Frame(window)
task_frame.pack(pady=10)

# Create a scrollbar for the task list
task_scrollbar = Scrollbar(task_frame)
task_scrollbar.pack(side=RIGHT, fill=Y)

# Create a listbox for the task list
task_list = Listbox(task_frame, width=50, height=10, yscrollcommand=task_scrollbar.set)
task_list.pack(side=LEFT, fill=BOTH)
task_scrollbar.config(command=task_list.yview)

# Create a frame for the task entry and buttons
entry_frame = Frame(window)
entry_frame.pack(pady=10)

# Create a label for the task entry
task_label = Label(entry_frame, text="Task:")
task_label.pack(side=LEFT)

# Create an entry field for the task
task_entry = Entry(entry_frame, width=40)
task_entry.pack(side=LEFT)

# Create a button to add tasks to the list
add_button = Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=LEFT, padx=10)

# Create a button to delete tasks from the list
delete_button = Button(entry_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=LEFT)

# Create a button to update tasks in the list
update_button = Button(entry_frame, text="Update Task", command=update_task)
update_button.pack(side=LEFT, padx=10)

# Run the main loop
window.mainloop()
