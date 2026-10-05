import speech_recognition as sr
import webbrowser
import pyttsx3

WAKE_WORD = "siri"
LANGUAGE = "en-IN"

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    else:
        speak("Sorry, I don't know that command")

def listen_once(r, source, timeout, limit):
  
    try:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=limit)
        return r.recognize_google(audio, language=LANGUAGE).lower()
    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Could not reach Google speech service:", e)
        return None

if __name__ == "__main__":
    speak("Initializing siri")
    r = sr.Recognizer()
    r.pause_threshold = 0.8         
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Calibrating for background noise...")
        r.adjust_for_ambient_noise(source, duration=1.5)

        while True:
            print("Listening for wake word...")
            word = listen_once(r, source, timeout=5, limit=4)

            if word is None:
                continue                     

            print("Heard:", word)

            if WAKE_WORD in word:            
                speak("Yes?")
                print("siri active... say your command")

                command = listen_once(r, source, timeout=6, limit=6)

                if command is None:
                    speak("I didn't catch that")
                else:
                    print("Command:", command)
                    process_command(command)  