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
                # Marcar a estrela na tela
                pygame.draw.circle(tela, (255, 0, 0), mouse_pos, 5)
                fonte = pygame.font.Font(None, 20)
                texto = fonte.render(nome_estrela, True, (255, 255, 255))
                tela.blit(texto, (mouse_pos[0] + 10, mouse_pos[1]))
                estrelas.append((mouse_pos, nome_estrela))
            else:
                print("Nenhum nome fornecido")

    # Atualizar tela
    tela.blit(fundo, (0, 0))

    # Desenhar nomes das estrelas na tela
    for posicao, nome in estrelas:
        fonte = pygame.font.Font(None, 33)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (posicao[0] + 10, posicao[1]))

    # Desenhar linhas entre as estrelas e exibir distâncias
    for i in range(len(estrelas)):
        for j in range(i + 1, len(estrelas)):
            posicao_estrela1, nome_estrela1 = estrelas[i]
            posicao_estrela2, nome_estrela2 = estrelas[j]

            # Desenhar linha entre as estrelas
            pygame.draw.line(tela, (255, 0, 255), posicao_estrela1, posicao_estrela2)

            # Calcular a distância entre as estrelas
            distancia = math.sqrt(
                (posicao_estrela2[0] - posicao_estrela1[0]) * 2 + (posicao_estrela2[1] - posicao_estrela1[1]) * 2
            )
            distancia_texto = f"{distancia:.2f}"
            fonte_distancia = pygame.font.Font(None, 20)
            texto_distancia = fonte_distancia.render(distancia_texto, True, (255, 255, 255))

            # Posicionar o texto da distância no meio da linha
            texto_posicao_x = (posicao_estrela1[0] + posicao_estrela2[0]) // 2
            texto_posicao_y = (posicao_estrela1[1] + posicao_estrela2[1]) // 2
            tela.blit(texto_distancia, (texto_posicao_x, texto_posicao_y))

    # Exibir instruções na tela
    for i, instrucao in enumerate(instrucoes):
        fonte_instrucao = pygame.font.Font(None, 25)
        texto_instrucao = fonte_instrucao.render(instrucao, True, (255, 255, 255))
        tela.blit(texto_instrucao, (10, 10 + i * 30))
    
    # Exibir informações do autor
    fonte_autor = pygame.font.Font(None, 20)
    texto_autor1 = fonte_autor.render("Emily Biecoski 1134316", True, (255, 255, 255))
    tela.blit(texto_autor1, (10, tamanho[1] - 20))

    texto_autor2 = fonte_autor.render("Carlos Henrique Ferrão 1135230", True, (255, 255, 255))
    tela.blit(texto_autor2, (10, tamanho[1] - 40))

    pygame.display.flip()

# Encerrar o pygame
pygame.quit()