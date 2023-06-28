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
fundo = pygame.image.load("bg.jpg")
pygame.mixer.music.load("space_machine.mp3")
pygame.mixer.music.play(-1)

estrelas = []  # Lista para armazenar as estrelas
linhas = []  # Lista para armazenar as linhas

instrucoes = [
    "Pressione F10 para Salvar os Pontos",
    "Pressione F11 para Carregar os Pontos",
    "Pressione F12 para Deletar os Pontos"
]
