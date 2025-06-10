import pyttsx3
import speech_recognition as sr
import eel

def speak_bot(text):
  engine=pyttsx3.init('sapi5')
  voices=engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)
  engine.setProperty('rate', 174)
  engine.say(text)
  engine.runAndWait()

@eel.expose
def take_command():
  helper=sr.Recognizer()

  with sr.Microphone() as source:
    print("Listening...")
    eel.DisplayMessage("Listening...")
    helper.pause_threshold=1
    helper.adjust_for_ambient_noise(source)
    audio=helper.listen(source, 10, 6)

  try:
    print("Recognizing...")
    eel.DisplayMessage("Recognizing...")
    query=helper.recognize_google(audio, language='en-in')
    print(f"User said: {query}")
    eel.DisplayMessage(query)
    speak_bot(query)
    eel.ShowHome()
  except Exception as e:
    return ""
  
  return query.lower()