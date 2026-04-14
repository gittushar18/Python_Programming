# ==========================
# Basic Voice Assistant
# ==========================

# Required Libraries
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# ==========================
# 1. Text-to-Speech Setup
# ==========================
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# ==========================
# 2. Listen to Voice Command
# ==========================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Sorry, the speech service is not available right now.")
        return ""
    return command.lower()

# ==========================
# 3. Task Functions
# ==========================
def tell_time():
    """Tell the current time"""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def tell_date():
    """Tell the current date"""
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today is {today}")

def search_wikipedia(query):
    """Search Wikipedia and speak summary"""
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except Exception:
        speak("Sorry, I could not find anything on Wikipedia.")

def search_web(query):
    """Open a web search for the query"""
    speak(f"Searching the web for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# ==========================
# 4. Command Processing
# ==========================
def process_command(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "")
        search_wikipedia(query)
    elif "search" in command:
        query = command.replace("search", "")
        search_web(query)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I cannot perform that task yet.")

# ==========================
# 5. Main Loop
# ==========================
def main():
    speak("Hello! I am your basic voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            process_command(command)

# ==========================
# Run Assistant
# ==========================
if __name__ == "__main__":
    main()

elif "exit" in command or "quit" in command:
    speak("Goodbye!")
    exit()