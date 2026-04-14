import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import json
from hashlib import sha256

# Authentication
def register_user(username, password):
    users = {}
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        pass
    hashed_pw = sha256(password.encode()).hexdigest()
    users[username] = hashed_pw
    with open("users.json", "w") as f:
        json.dump(users, f)

def authenticate_user(username, password):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
        hashed_pw = sha256(password.encode()).hexdigest()
        return users.get(username) == hashed_pw
    except FileNotFoundError:
        return False

# Tkinter Chat App
class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Chat Application")
        self.geometry("600x600")
        self.rooms = ["General", "Sports", "Tech"]
        self.current_room = tk.StringVar(value=self.rooms[0])
        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(pady=100)
        tk.Label(self.login_frame, text="Username").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        tk.Label(self.login_frame, text="Password").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()
        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.login_frame, text="Register", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate_user(username, password):
            messagebox.showinfo("Success", "Login successful")
            self.login_frame.destroy()
            self.create_chat_frame()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        register_user(username, password)
        messagebox.showinfo("Success", "Registration successful")

    def create_chat_frame(self):
        self.chat_frame = tk.Frame(self)
        self.chat_frame.pack(fill="both", expand=True)
        tk.Label(self.chat_frame, text="Select Room:").pack()
        tk.OptionMenu(self.chat_frame, self.current_room, *self.rooms).pack()
        self.chat_display = ScrolledText(self.chat_frame)
        self.chat_display.pack(fill="both", expand=True)
        self.chat_display.config(state="disabled")
        self.msg_entry = tk.Entry(self.chat_frame)
        self.msg_entry.pack(fill="x", side="left", expand=True)
        tk.Button(self.chat_frame, text="Send", command=self.send_message).pack(side="right")

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            self.chat_display.config(state="normal")
            self.chat_display.insert("end", f"You: {msg}\n")
            self.chat_display.config(state="disabled")
            self.msg_entry.delete(0, "end")
            # Save message to room history
            with open(f"{self.current_room.get()}_history.txt", "a") as f:
                f.write(f"You: {msg}\n")

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
