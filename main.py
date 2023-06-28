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
                # Lógica para carregar os pontos
                arquivo = open("pontos.txt", "r")
                estrelas = []
                for linha in arquivo:
                    dados = linha.strip().split(",")
                    nome = dados[0]
                    posicao = (int(dados[1]), int(dados[2]))
                    estrelas.append((posicao, nome))
                arquivo.close()
                print("Pontos carregados")
            elif event.key == pygame.K_F12:
                # Lógica para deletar os pontos
                estrelas = []
                print("Pontos deletados")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            nome_estrela = simpledialog.askstring("Nome da estrela", "Digite o nome da estrela:")
            if nome_estrela: