import os
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple File Manager")
root.geometry("400x450")

# Entry for file name
filename_entry = tk.Entry(root, width=40)
filename_entry.pack(pady=5)
filename_entry.insert(0, "Enter file name")

# Entry for content
content_entry = tk.Entry(root, width=40)
content_entry.pack(pady=5)
content_entry.insert(0, "Enter content")

# Entry for folder name
folder_entry = tk.Entry(root, width=40)
folder_entry.pack(pady=5)
folder_entry.insert(0, "Enter folder name")

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

# Create folder
def create_folder():
    folder_name = folder_entry.get()

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        messagebox.showinfo("Success", "Folder created!")
    else:
        messagebox.showerror("Error", "Folder already exists!")

# Delete folder (with confirmation)
def delete_folder():
    folder_name = folder_entry.get()

    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        confirm = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete this folder?\n(Folder must be empty)"
        )
        if confirm:
            os.rmdir(folder_name)
            messagebox.showinfo("Deleted", "Folder deleted!")
    else:
        messagebox.showerror("Error", "Folder not found!")

# List folders
def list_folders():
    folders = [f for f in os.listdir() if os.path.isdir(f)]

    if folders:
        messagebox.showinfo("Folders", "\n".join(folders))
    else:
        messagebox.showinfo("Folders", "No folders found.")

# Buttons
tk.Button(root, text="Create File", width=20, command=create_file).pack(pady=3)
tk.Button(root, text="Read File", width=20, command=read_file).pack(pady=3)
tk.Button(root, text="Append File", width=20, command=append_file).pack(pady=3)
tk.Button(root, text="Delete File", width=20, command=delete_file).pack(pady=3)

tk.Label(root, text="Folder Operations").pack(pady=8)

tk.Button(root, text="Create Folder", width=20, command=create_folder).pack(pady=3)
tk.Button(root, text="Delete Folder", width=20, command=delete_folder).pack(pady=3)
tk.Button(root, text="List Folders", width=20, command=list_folders).pack(pady=3)

# Start GUI
root.mainloop()