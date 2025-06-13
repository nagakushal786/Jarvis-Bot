import re

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    matching=re.search(pattern, command, re.IGNORECASE)
    return matching.group(1) if matching else None

def remove_words(input_str, words_to_remove):
    words=input_str.split()
    filtered_words=[word for word in words if word.lower() not in words_to_remove]
    result_str=' '.join(filtered_words)
    return result_str