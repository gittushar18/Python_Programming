# ==========================
# Basic Voice Assistant (Final)
# ==========================

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
    engine.say(text)
    engine.runAndWait()

# ==========================
# 2. Listen Function
# ==========================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return ""

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# ==========================
# 3. Task Functions
# ==========================
def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("I couldn't find anything on Wikipedia.")

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# ==========================
# 4. Command Processing
# ==========================
def process_command(command):

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

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

    elif "stop listening" in command:
        speak("Stopping listening now.")
        return False

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I cannot perform that task.")

    return True

# ==========================
# 5. Main Function
# ==========================
def main():
    speak("Hello! I am your voice assistant.")

    running = True
    while running:
        command = listen()
        if command:
            running = process_command(command)

# ==========================
# Run Assistant
# ==========================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped by user")
        speak("Assistant stopped")
