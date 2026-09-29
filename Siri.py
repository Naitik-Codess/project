import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine  = pyttsx3.init()

def speak(text):
       engine.say(text)
       engine.runAndWait()

def  processCommaand (c):
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

        WAKE_WORD = "siri"

        LANGUAGE = "en-IN"
 
if __name__ == "__main__":
       speak("Initializing siri .....")
       r = sr.Recognizer()

       with sr.Microphone() as source:
        # Calibrate for background noise once
        r.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                word = r.recognize_google(audio)
                print("Heard:", word)

                if word.lower() == "siri":
                    speak("Yes?")
                    print("siri active...")

                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                processCommaand(command)

            except sr.WaitTimeoutError:
                # Nobody spoke - just try again
                continue
            except sr.UnknownValueError:
                # Speech wasn't understood - just try again
                continue
            except sr.RequestError as e:
                print("Could not reach Google speech service; {0}".format(e))
            except Exception as e:
                print("Error:", e)