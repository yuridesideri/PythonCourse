import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("c:/Users/yurid/Desktop/Python Programs/Exerc/Curso/turndown.mp3")
pygame.mixer.music.play(-1)
input('Ta tocando o Turn?')
