# 🌦️ README.md – Weather App (Python GUI)
## 🧠 Project Overview

This project is a GUI-based Weather Application built using Python. It fetches real-time weather data from the OpenWeatherMap API and displays temperature, weather conditions, humidity, wind speed, and an icon for the selected city.

## 🚀 Features
✅ Real-time weather data
✅ Search weather by city name
✅ Displays: Temperature (°C), Weather description, Humidity, Wind speed
✅ Weather icon display 🌤️
✅ Simple and clean GUI


## 🛠️ Technologies Used
Python
Tkinter – GUI development
Requests – API calls
Pillow (PIL) – Image handling
OpenWeatherMap API – Weather data


## 📂 Project Structure
Weather_App/

│── main.py                        # Main application file

│── README.md                      # Documentation


## ⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your_username/weather-app.git
cd weather-app
2. Install required libraries
pip install requests pillow
(Tkinter comes pre-installed with Python)
3. Get API Key
Go to: https://openweathermap.org/api
Sign up and generate your API key
4. Add your API key
API_KEY = "your_api_key_here"
5. Run the application
python main.py


## 📊 How It Works
Enter a city name
Click “Get Weather”
App fetches data from API
Displays:
🌡️ Temperature
🌤️ Weather condition
💧 Humidity
🌬️ Wind speed
🖼️ Weather icon


## 🔗 API Details
API Used: OpenWeatherMap Current Weather API
Endpoint:
https://api.openweathermap.org/data/2.5/weather


## ⚠️ Error Handling
❌ Empty input → Warning message
❌ Invalid city → Error message
❌ API failure → Graceful handling


## 🎯 Future Enhancements
🔹 5-day weather forecast

🔹 Auto-detect location

🔹 Dark mode UI 🌙

🔹 Temperature unit toggle (°C / °F)

🔹 Background changes based on weather


##🧩 Conclusion

This project demonstrates how to integrate APIs with GUI applications in Python. It helps understand real-time data fetching, JSON parsing, and user interface design.
