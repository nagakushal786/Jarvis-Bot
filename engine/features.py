import pygame
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speak_bot
import os
import pywhatkit as kit
import sqlite3
import webbrowser
from engine.helper import extract_yt_term, remove_words
import pvporcupine
import pyaudio
import struct
import time
from pipes import quote
import subprocess
import pyautogui
from hugchat import hugchat

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

def find_contact(query):
    words_to_remove=[ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'video', 'send', 'message', 'whatsapp']
    query=remove_words(query, words_to_remove)

    try:
        query=query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%'+query+'%', query+'%'))
        results=cursor.fetchall()
        mobile_num_str=str(results[0][0])
        if not mobile_num_str.startswith('+91'):
            mobile_num_str='+91'+mobile_num_str

        return mobile_num_str, query
    except:
        speak_bot("No contact found")
        return 0, 0
    
def whats_app(mobile_no, message, flag, name):
    if flag=='message':
        target_tab=20
        jarvis_message="Message successfully sent to "+name
    elif flag=='call':
        target_tab=14
        message=""
        jarvis_message="Calling "+name
    elif flag=='video call':
        target_tab=13
        message=""
        jarvis_message="Starting video call with "+name

    # Encoding message for url
    encoded_message=quote(message)

    # Construction of shell based whatsapp url
    whatsapp_url=f'whatsapp://send?phone={mobile_no}&text={encoded_message}'

    # Start command of whatsapp
    full_command=f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl', 'f')
    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak_bot(jarvis_message)

def chat_bot(query):
    user_input=query.lower()
    chatbot=hugchat.ChatBot(cookie_path="engine/cookies.json")
    id=chatbot.new_conversation()
    chatbot.change_conversation(id)
    response=chatbot.chat(user_input)
    speak_bot(response)
    return response