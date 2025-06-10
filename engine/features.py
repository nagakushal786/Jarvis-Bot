import pygame
import eel

@eel.expose
def assistant_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("frontend/assets/audio/start_sound.mp3")
    pygame.mixer.music.play()