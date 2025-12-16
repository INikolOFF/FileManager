import os
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple File Manager")
root.geometry("400x300")

# Entry for file name
filename_entry = tk.Entry(root, width=40)
filename_entry.pack(pady=5)
filename_entry.insert(0, "Enter file name")

# Entry for content
content_entry = tk.Entry(root, width=40)
content_entry.pack(pady=5)
content_entry.insert(0, "Enter content")

# Create file
def create_file():
    filename = filename_entry.get()
    content = content_entry.get()

    with open(filename, "w") as file:
        file.write(content)

    messagebox.showinfo("Success", "File created!")

# Read file
def read_file():
    filename = filename_entry.get()

    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
        messagebox.showinfo("File Content", content)
    else:
        messagebox.showerror("Error", "File not found!")

# Delete file (with confirmation)
def delete_file():
    filename = filename_entry.get()

    if os.path.exists(filename):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this file?")
        if confirm:
            os.remove(filename)
            messagebox.showinfo("Deleted", "File deleted!")
    else:
        messagebox.showerror("Error", "File not found!")

# Append to file
def append_file():
    filename = filename_entry.get()
    content = content_entry.get()

    if os.path.exists(filename):
        with open(filename, "a") as file:
            file.write("\n" + content)
        messagebox.showinfo("Success", "Text appended!")
    else:
        messagebox.showerror("Error", "File not found!")

# Buttons
tk.Button(root, text="Create File", width=20, command=create_file).pack(pady=3)
tk.Button(root, text="Read File", width=20, command=read_file).pack(pady=3)
tk.Button(root, text="Append File", width=20, command=append_file).pack(pady=3)
tk.Button(root, text="Delete File", width=20, command=delete_file).pack(pady=3)

# Start GUI
root.mainloop()