import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io

# —— API Setup ——
API_KEY = "c1436d9dc37598ff68a56f6889259404"  # replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_URL = "https://openweathermap.org/img/wn/"

# —— Fetch Weather from API ——
def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return None
    return response.json()

# —— Display Weather ——
def display_weather():
    city = entry_city.get().strip()
    if not city:
        messagebox.showwarning("Input required", "Please enter a city name!")
        return
    
    data = fetch_weather(city)
    if not data:
        messagebox.showerror("Error", "Could not retrieve data. Check city name.")
        return

    # Current weather details
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Update labels
    lbl_temp.config(text=f"{temp} °C")
    lbl_desc.config(text=desc)
    lbl_humidity.config(text=f"Humidity: {humidity}%")
    lbl_wind.config(text=f"Wind Speed: {wind_speed} m/s")

    # Fetch & display icon
    icon_id = data["weather"][0]["icon"]
    icon_response = requests.get(f"{ICON_URL}{icon_id}@2x.png")
    icon_image = Image.open(io.BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)
    lbl_icon.config(image=icon_photo)
    lbl_icon.image = icon_photo

# —— Build GUI ——
root = tk.Tk()
root.title("Weather App")
root.geometry("380x450")
root.resizable(False, False)

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=8)
entry_city = tk.Entry(root, font=("Arial", 14), justify='center')
entry_city.pack(pady=5)

btn_search = tk.Button(root, text="Get Weather", command=display_weather, bg="#4caf50", fg="white")
btn_search.pack(pady=10)

lbl_icon = tk.Label(root)
lbl_icon.pack()

lbl_temp = tk.Label(root, text="", font=("Arial", 24))
lbl_temp.pack(pady=5)

lbl_desc = tk.Label(root, text="", font=("Arial", 16))
lbl_desc.pack()

lbl_humidity = tk.Label(root, text="", font=("Arial", 14))
lbl_humidity.pack(pady=4)

lbl_wind = tk.Label(root, text="", font=("Arial", 14))
lbl_wind.pack(pady=4)

root.mainloop()
