import pyttsx3
import speech_recognition as sr
import eel
import time

def speak_bot(text):
  text=str(text)
  engine=pyttsx3.init('sapi5')
  voices=engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)
  engine.setProperty('rate', 174)
  eel.DisplayMessage(text)
  engine.say(text)
  eel.receiveText(text)
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
def all_commands(message=1):
  if message==1:
    query=take_command()
    eel.sendText(query)
  else:
    query=message
    eel.sendText(query)

  try:
    if "open" in query:
      from engine.features import open_command
      open_command(query)

    elif "on youtube" in query:
      from engine.features import play_youtube
      play_youtube(query)

    elif "send message" in query or "send a message" in query or "phone call" in query or "video call" in query:
      from engine.features import find_contact, whats_app, make_call, send_message
      contact_no, name=find_contact(query)

      if(contact_no!=0):
        speak_bot("Which mode you want to use? Whatsapp or Mobile")
        preference=take_command()

        if "mobile" in preference:
          if "phone call" in query:
            make_call(name, contact_no)
          elif "send message" in query or "send a message" in query or "send sms" in query or "send an sms" in query:
            speak_bot("What message to send?")
            inp_message=take_command()
            send_message(inp_message, contact_no, name)
          else:
            speak_bot("Please try again...")

        elif "whatsapp" in preference:
          flag=""
          if "send message" in query or "send a message" in query:
            flag="message"
            speak_bot("What message to send?")
            query=take_command()
          elif "phone call" in query:
            flag="call"
          else:
            flag="video call"
          whats_app(contact_no, query, flag, name)

    elif "take a note" in query:
      from engine.features import note_taking
      speak_bot("What is the subject?")
      heading=take_command()
      time.sleep(1)
      speak_bot("What is the note to be taken?")
      note=take_command()
      note_taking(heading, note)

    elif "take a selfie" in query:
      from engine.features import take_selfie
      take_selfie()
      
    elif "what" in query or "where" in query or "why" in query or "how" in query or "who" in query or "give" in query:
      from engine.features import chat_bot
      chat_bot(query)

    elif "capture a video":
      from engine.features import record_video
      record_video()
  except:
    print("Error in running the query...")

  eel.ShowHome()