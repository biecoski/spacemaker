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
# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F10:
                # Lógica para salvar os pontos
                arquivo = open("pontos.txt", "w")
                for posicao, nome in estrelas:
                    arquivo.write(f"{nome},{posicao[0]},{posicao[1]}\n")
                arquivo.close()
                print("Pontos salvos")
            elif event.key == pygame.K_F11: