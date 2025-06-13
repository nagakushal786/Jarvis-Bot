import pygame
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speak_bot
import os
import pywhatkit as kit
import sqlite3
import webbrowser
from engine.helper import extract_yt_term
import pvporcupine
import pyaudio
import struct
import time

connection=sqlite3.connect('jarvis.db')
cursor=connection.cursor()

@eel.expose
def assistant_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("frontend/assets/audio/start_sound.mp3")
    pygame.mixer.music.play()

def open_command(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open", "")
    query.lower()

    app_name=query.strip().lower()

    if app_name!="":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results=cursor.fetchall()

            if len(results)!=0:
                speak_bot(f'Opening {query}')
                os.startfile(results[0][0])

            elif len(results)==0:
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                results=cursor.fetchall()

                if len(results)!=0:
                    speak_bot(f'Opening {query}')
                    webbrowser.open(results[0][0])

                else:
                    speak_bot(f'Opening {query}')
                    try:
                        os.system(query)
                    except:
                        speak_bot("Application not found...")

        except:
            speak_bot("Something went wrong...")

def play_youtube(query):
    search_term=extract_yt_term(query)
    speak_bot(f"Playing {search_term} on Youtube")
    kit.playonyt(search_term)

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