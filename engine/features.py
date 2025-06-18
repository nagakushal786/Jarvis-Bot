import pygame
import eel
from engine.config import ASSISTANT_NAME, ADB_PATH
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
                speak_bot(f'Opening{query}...')
                os.startfile(results[0][0])

            elif len(results)==0:
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                results=cursor.fetchall()

                if len(results)!=0:
                    speak_bot(f'Opening{query}...')
                    webbrowser.open(results[0][0])

                else:
                    speak_bot(f'Opening{query}...')
                    try:
                        os.system(query)
                    except:
                        speak_bot("Application not found...")

        except:
            speak_bot("Something went wrong...")

def play_youtube(query):
    search_term=extract_yt_term(query)
    speak_bot(f"Playing {search_term} on Youtube...")
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
        jarvis_message="Message successfully sent to "+name+"..."
    elif flag=='call':
        target_tab=14
        message=""
        jarvis_message="Calling "+name+"..."
    elif flag=='video call':
        target_tab=13
        message=""
        jarvis_message="Starting video call with "+name+"..."

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

def make_call(name, mobile_no):
    mobile_no=mobile_no.replace(" ", "")
    speak_bot(f"Calling {name}...")
    command=ADB_PATH+" shell am start -a android.intent.action.CALL -d tel:"+mobile_no
    os.system(command)

def send_message(message, mobile_no, name):
    from engine.helper import key_event, tap_event, adb_input, go_complete_back, replace_spaces_with_percent_s
    message=replace_spaces_with_percent_s(message)
    mobile_no=replace_spaces_with_percent_s(mobile_no)
    speak_bot(f"Sending message to {name}...")

    go_complete_back(4)
    time.sleep(1)
    # Home screen
    key_event(3)

    tap_event(411, 2117)
    tap_event(931, 2081)
    adb_input(mobile_no)
    tap_event(508, 558)
    tap_event(301, 2113)
    adb_input(message)
    tap_event(966, 1389)

    speak_bot(f"Message sent successfully to {name}...")

def note_taking(heading, note):
    from engine.helper import key_event, tap_event, adb_input, go_complete_back, replace_spaces_with_percent_s
    heading=replace_spaces_with_percent_s(heading)
    note=replace_spaces_with_percent_s(note)
    speak_bot(f"Taking a note...")

    go_complete_back(4)
    time.sleep(1)
    # Home screen
    key_event(3)

    tap_event(794, 667)
    tap_event(849, 751)
    tap_event(940, 1916)
    tap_event(132, 502)
    adb_input(heading)
    tap_event(576, 2171)
    tap_event(89, 2158)
    tap_event(599, 1875)
    tap_event(576, 2171)
    adb_input(note)
    tap_event(986, 226)
    tap_event(79, 212)

    speak_bot("Note successfully taken...")

def take_selfie():
    from engine.helper import key_event, tap_event, adb_input, go_complete_back

    go_complete_back(4)
    time.sleep(1)
    # Home screen
    key_event(3)

    speak_bot("Ready to take a selfie...")

    tap_event(921, 2107)
    tap_event(912, 2049)
    speak_bot("Say cheese...")
    tap_event(537, 2054)

    speak_bot("Selfie taken successfully...")

def record_video():
    from engine.helper import key_event, tap_event, adb_input, go_complete_back

    go_complete_back(4)
    time.sleep(1)
    # Home screen
    key_event(3)

    speak_bot("Capturing a video...")

    tap_event(921, 2107)
    tap_event(297, 1836)
    tap_event(537, 2054)
    time.sleep(4)
    tap_event(541, 2058)
    
    speak_bot("Video captured successfully...")