import re
from engine.config import ADB_PATH
import os
import time

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    matching=re.search(pattern, command, re.IGNORECASE)
    return matching.group(1) if matching else None

def remove_words(input_str, words_to_remove):
    words=input_str.split()
    filtered_words=[word for word in words if word.lower() not in words_to_remove]
    result_str=' '.join(filtered_words)
    return result_str

def key_event(key_code):
    command=f"{ADB_PATH} shell input keyevent {key_code}"
    os.system(command)
    time.sleep(1)

def tap_event(x, y):
    command=f"{ADB_PATH} shell input tap {x} {y}"
    os.system(command)
    time.sleep(1)

def adb_input(message):
    command=f'{ADB_PATH} shell input text "{message}"'
    os.system(command)
    time.sleep(1)

def go_complete_back(key_code):
    for i in range(6):
        key_event(key_code)

def replace_spaces_with_percent_s(inp_str):
    return inp_str.replace(" ", "%s")