import re

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    matching=re.search(pattern, command, re.IGNORECASE)
    return matching.group(1) if matching else None