# 💬 README.md – Advanced Chat Application
## 🧠 Project Overview

This project is a GUI-based Chat Application built using Python. It includes user authentication (login & registration) and allows users to send messages in different chat rooms. Messages are saved locally for each room.

## 🚀 Features
✅ User Registration & Login system 🔐

✅ Password hashing using SHA-256

✅ Multiple chat rooms (General, Sports, Tech)

✅ Send and display messages

✅ Chat history saved locally 📁

✅ Simple and interactive GUI


## 🛠️ Technologies Used
Python
Tkinter – GUI development
JSON – User data storage
Hashlib (SHA-256) – Password security
File Handling – Chat history storage


## 📂 Project Structure
Chat_App/

│── main.py                  # Main application file

│── users.json               # Stores user credentials

│── General_history.txt      # Chat history (General room)

│── Sports_history.txt       # Chat history (Sports room)

│── Tech_history.txt         # Chat history (Tech room)

│── README.md                # Documentation


## ⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your_username/chat-application.git
cd chat-application
2. Run the application
python main.py
(No external libraries required – all are built-in)


## 🔐 Authentication System
User credentials are stored in users.json
Passwords are hashed using SHA-256 for security
Login verifies hashed password


## 💬 How It Works
Open the application
Register a new account or login
Select a chat room: General, Sports, Tech
Type your message and click Send
Messages are:
Displayed in chat window
Saved in corresponding room file


## 📁 Chat History
Messages are stored in text files:
General_history.txt
Sports_history.txt
Tech_history.txt
Each room maintains separate history


## ⚠️ Limitations
Works on single system (no real-time networking)
No multi-user live chat (offline simulation only)
No encryption for stored messages


## 🎯 Future Enhancements
🔹 Real-time chat using sockets 🌐

🔹 Online multi-user support

🔹 Message timestamps

🔹 User avatars/profile

🔹 End-to-end encryption 🔐

🔹 Better UI (modern chat interface)


## 🧩 Conclusion

This project demonstrates how to build a secure GUI-based chat application with authentication and file handling. It is useful for understanding user management, hashing, and basic chat system design.
