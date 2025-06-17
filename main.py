import eel
from engine.features import *
from engine.command import *
from engine.auth.recognize import face_authentication
import time

def start():
  eel.init('frontend')
  assistant_sound()

  @eel.expose
  def start_bot():
    time.sleep(7)
    eel.hideLoader()

    speak_bot("Ready for face authentication...")
    flag=face_authentication()

    if flag==1:
      eel.hideFaceAuth()
      speak_bot("Face authentication successful...")
      eel.hideFaceAuthSuccess()
      speak_bot("Welcome Boss, I am here to help you...")
      eel.hideStart()
      assistant_sound()
    else:
      speak_bot("Face authentication failed...")

  # For chrome
  eel.start('index.html', mode='chrome', app_mode=True, host='localhost', block=True)

# For edge
# os.system('start msedge.exe --app="http://localhost:5500/frontend/index.html"')
# eel.start('index.html', mode=None, host='localhost', block=True)