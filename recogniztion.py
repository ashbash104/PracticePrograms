import speech_recognition as sr
import keyboard
import time

# obtain audio from the microphone
r = sr.Recognizer()

def start_listening():
    if keyboard.is_pressed("space"): 
        with sr.Microphone() as source:
            print("Recording Audio...") 
            r.adjust_for_ambient_noise(source) 
            audio = r.listen(source, 10)    
            if keyboard.is_pressed("q"):
                return False
            try:
                text = r.recognize_google(audio)

                # This is for saving on the file
                with open("source.txt", "w") as f:
                    print(text, file=f) 

                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Oops. I couldn't understand.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition")
            except sr.WaitTimeoutError:
                print('Please make sure to say something')
         

while True: 
    start_listening() 