import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # for clipboard integration

# ---------------- Password Generator ----------------
def generate_password():
    length = int(entry_length.get())
    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_numbers = var_numbers.get()
    use_symbols = var_symbols.get()
    
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4")
        return
    
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    
    if not char_pool:
        messagebox.showerror("Error", "Select at least one character type")
        return
    
    # Ensure security rules: at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(char_pool))
    
    # Shuffle to avoid predictable order
    random.shuffle(password)
    password_str = "".join(password)
    
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password_str)

# ---------------- Copy to Clipboard ----------------
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x350")

# --- Password Length ---
tk.Label(root, text="Password Length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack()
entry_length.insert(0, "12")  # default length

# --- Options ---
frame_options = tk.Frame(root)
frame_options.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(frame_options, text="Include Uppercase", variable=var_upper).pack(anchor='w')
tk.Checkbutton(frame_options, text="Include Lowercase", variable=var_lower).pack(anchor='w')
tk.Checkbutton(frame_options, text="Include Numbers", variable=var_numbers).pack(anchor='w')
tk.Checkbutton(frame_options, text="Include Symbols", variable=var_symbols).pack(anchor='w')

# --- Generate Button ---
btn_generate = tk.Button(root, text="Generate Password", command=generate_password, bg="lightblue")
btn_generate.pack(pady=10)

# --- Password Display ---
tk.Label(root, text="Generated Password:").pack(pady=5)
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

# --- Copy Button ---
btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="lightgreen")
btn_copy.pack(pady=10)

root.mainloop()
