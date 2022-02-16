#@azee-whie
#To-do Program!

import tkinter as tk
from tkinter import Scrollbar, messagebox
import pickle


win = tk.Tk()
win.geometry('600x500')
win.title('To-Do app')
win.config(bg='#9FD2FB')

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Error, Please enter task")

def save():
    task = task_list.get(0, task_list.size())
    pickle.dump(task, open("task.txt","wb" ))
def delete_task():
    task_list.delete(tk.ANCHOR)


def clear_entry(event, entry):
    entry.delete(0, tk.END)

frame = tk.Frame(win)
frame.pack(pady=10)

task_list = tk.Listbox(frame, width=25, height=8, font=('Times', 18), fg='#9FD2FB', selectbackground='#9FD2FB', activestyle="none",)
task_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrolbar = tk.Scrollbar(frame)
scrolbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_list.config(yscrollcommand = scrolbar.set)
scrolbar.config(command=task_list.yview)

task_entry = tk.Entry(win, font=('Times', 24))
task_entry.insert(0, "Enter Task here")
task_entry.bind("<Button-1>", lambda event: clear_entry(event, task_entry))
task_entry.pack(pady=20)

button_frame = tk.Frame(win)
button_frame.pack(pady=20)

addTask_btn = tk.Button(button_frame, text = 'Add your task here', font=('Times', 14), bg='#4398f8', fg = 'black', padx=20, pady=10, command=add_task)
addTask_btn.pack(fill = tk.BOTH, expand=False, side=tk.LEFT)

delTask_btn = tk.Button(button_frame, text = 'Delete your task here', font=('Times', 14), bg='#4398f8', fg = 'black', padx=31, pady=10, command=delete_task)
delTask_btn.pack(fill = tk.BOTH, expand=False, side=tk.LEFT)
SaveTask_btn = tk.Button(button_frame, text = 'Save task here', font=('Times', 14), bg='#4398f8', fg = 'black', padx=41, pady=10, command=save)
SaveTask_btn.pack(fill = tk.BOTH, expand=True, side=tk.LEFT)

win.mainloop()