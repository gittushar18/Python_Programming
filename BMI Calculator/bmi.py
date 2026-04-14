import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ------------------ Database Setup ------------------
conn = sqlite3.connect("bmi_data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    weight REAL NOT NULL,
    height REAL NOT NULL,
    bmi REAL NOT NULL,
    category TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# ------------------ BMI Calculation ------------------
def calculate_bmi(weight, height):
    bmi = weight / (height/100) ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

# ------------------ Add Record ------------------
def add_record():
    username = entry_user.get().strip()
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")
        return
    
    bmi, category = calculate_bmi(weight, height)
    
    cursor.execute("INSERT INTO bmi_records (username, weight, height, bmi, category) VALUES (?, ?, ?, ?, ?)",
                   (username, weight, height, bmi, category))
    conn.commit()
    
    messagebox.showinfo("BMI Result", f"{username}'s BMI: {bmi} ({category})")
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    update_history(username)
    plot_bmi_trend(username)

# ------------------ Update History ------------------
def update_history(username):
    for row in tree.get_children():
        tree.delete(row)
    
    cursor.execute("SELECT weight, height, bmi, category, timestamp FROM bmi_records WHERE username=? ORDER BY timestamp", (username,))
    records = cursor.fetchall()
    for rec in records:
        tree.insert("", tk.END, values=rec)

# ------------------ Plot BMI Trend ------------------
def plot_bmi_trend(username):
    cursor.execute("SELECT timestamp, bmi FROM bmi_records WHERE username=? ORDER BY timestamp", (username,))
    records = cursor.fetchall()
    if not records:
        return
    
    timestamps, bmi_values = zip(*records)
    
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(timestamps, bmi_values, marker='o', linestyle='-', color='blue')
    ax.set_title(f"{username}'s BMI Trend")
    ax.set_xlabel("Time")
    ax.set_ylabel("BMI")
    ax.grid(True)
    
    canvas.draw()

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("BMI Calculator with History and Trend Analysis")
root.geometry("800x600")

# --- Input Frame ---
frame_input = tk.Frame(root, pady=10)
frame_input.pack()

tk.Label(frame_input, text="Username:").grid(row=0, column=0, padx=5)
entry_user = tk.Entry(frame_input)
entry_user.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Weight (kg):").grid(row=1, column=0, padx=5)
entry_weight = tk.Entry(frame_input)
entry_weight.grid(row=1, column=1, padx=5)

tk.Label(frame_input, text="Height (cm):").grid(row=2, column=0, padx=5)
entry_height = tk.Entry(frame_input)
entry_height.grid(row=2, column=1, padx=5)

btn_add = tk.Button(frame_input, text="Calculate BMI & Save", command=add_record, bg="lightgreen")
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

# --- History Frame ---
frame_history = tk.Frame(root)
frame_history.pack(pady=10)

columns = ("Weight", "Height", "BMI", "Category", "Timestamp")
tree = ttk.Treeview(frame_history, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(side=tk.LEFT, fill=tk.Y)

scrollbar = ttk.Scrollbar(frame_history, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscroll=scrollbar.set)

# --- BMI Trend Plot ---
frame_plot = tk.Frame(root)
frame_plot.pack(fill=tk.BOTH, expand=True, pady=10)

fig = plt.Figure(figsize=(7,3), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_plot)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run GUI
root.mainloop()
