import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make JARVIS speak
def speak(Jarvis):
    engine.say(Jarvis)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)   

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, the speech recognition service is down.")
            speak("Sorry, the speech recognition service is down.")
            return ""

# Function to process commands
def process_command(command):
    if "hello" in command:
        speak("Hello, how can I assist you today?")
    elif "your name" in command:
        speak("I am JARVIS, your personal assistant.")
    elif "how are you" in command:
        speak("I am just a computer program, but I am here to help you.")
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to respond to that.")
    
    return True

# Main function
def jarvis():
    speak("Initializing JARVIS.")
    running = True
    while running:
        command = recognize_speech()
        if command:
            running = process_command(command)

if __name__ == "__main__":
    jarvis()
