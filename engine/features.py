import pygame
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speak_bot
import os
import pywhatkit as kit
import re
import sqlite3
import webbrowser

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

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    matching=re.search(pattern, command, re.IGNORECASE)
    return matching.group(1) if matching else None

def play_youtube(query):
    search_term=extract_yt_term(query)
    speak_bot(f"Playing {search_term} on Youtube")
    kit.playonyt(search_term)