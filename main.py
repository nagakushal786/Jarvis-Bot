import os
import eel
from engine.features import *

eel.init('frontend')
assistant_sound()

os.system('start msedge.exe --app="http://localhost:5500/frontend/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)