import pyttsx3
import speech_recognition as sr
import eel
import time

def speak_bot(text):
  engine=pyttsx3.init('sapi5')
  voices=engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)
  engine.setProperty('rate', 174)
  eel.DisplayMessage(text)
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
    audio=helper.listen(source, 10, 7)

  try:
    print("Recognizing...")
    eel.DisplayMessage("Recognizing...")
    query=helper.recognize_google(audio, language='en-in')
    print(f"User said: {query}")
    eel.DisplayMessage(query)
    time.sleep(2)
  except Exception as e:
    return ""
  
  return query.lower()

@eel.expose
def all_commands():
  try:
    query=take_command()

    if "open" in query:
      from engine.features import open_command
      open_command(query)
    elif "on youtube" in query:
      from engine.features import play_youtube
      play_youtube(query)
    elif "send message" in query or "phone call" in query or "video call" in query:
      from engine.features import find_contact, whats_app
      flag=""
      contact_no, name=find_contact(query)

      if(contact_no!=0):
        if "send message" in query:
          flag="message"
          speak_bot("What message to send?")
          query=take_command()
        elif "phone call" in query:
          flag="call"
        else:
          flag="video call"

        whats_app(contact_no, query, flag, name)
    else:
      print("Not a command to run...")
  except:
    print("Error in running the query...")

  eel.ShowHome()