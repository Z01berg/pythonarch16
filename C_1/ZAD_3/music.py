import pygame

pygame.init()

pygame.mixer.music.load("./ritual.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
