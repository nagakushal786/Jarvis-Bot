# To test the hot word detection

import struct
import time
import pvporcupine
import pyaudio

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

hot_word()