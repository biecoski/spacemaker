from tkinter import simpledialog
import math
import pygame

pygame.init()

tamanho = (850, 560)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")

# Definir o ícone da janela
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

