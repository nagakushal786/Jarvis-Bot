# To test the hot word detection

import struct
import pvporcupine
import pyaudio
import subprocess, time, pyautogui
from urllib.parse import quote

def hot_word():
    porcupine=None
    paud=None
    audio_stream=None

    try:
        porcupine=pvporcupine.create(keywords=['jarvis', 'alexa'])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,
                               channels=1,
                               format=pyaudio.paInt16,
                               input=True,
                               frames_per_buffer=porcupine.frame_length)
        
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length, keyword)

            keyword_idx=porcupine.process(keyword)

            if keyword_idx>=0:
                print("Hotword detected...")

                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()
        if paud is not None:
            paud.terminate()
        if audio_stream is not None:
            audio_stream.close()

def debug_tab_count(mobile_no, flag):
    # Open chat
    whatsapp_url = f'whatsapp://send?phone={mobile_no}'
    subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
    time.sleep(5)

    # Focus the window
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)

    # Try pressing TAB and read captions
    for i in range(1, 20):
        pyautogui.hotkey('tab')
        time.sleep(0.2)
        # Make sure system is reading UI focus
        # You'll need a tool like Windows Narrator, NVDA, or a screen reader
        print("Pressed TAB:", i)

debug_tab_count("+917780737761", "call")
