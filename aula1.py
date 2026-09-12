import pygame
import time
import random

def sortear_posicao():
    x = random.randint(0, 750)
    y = random.randint(0, 550)
    return x, y

def sortear_cor():
    r = random.randint(0,200)
    g = random.randint(0,200)
    b = random.randint(0,200)
    return (r,g,b)

pygame.init()

#Clock - Define a taxa de atualização
clock = pygame.time.Clock()

#Define a tela e seu tamanho
tela = pygame.display.set_mode((1200,800))

#Define o título da janela
pygame.display.set_caption("Aula de Pygame muito legal e daora")

#Define a fonte do jogo
fonte = pygame.font.SysFont("arial", 28)

#Define a posição e cor iniciais do jogador
x = 200
y = 200
rgb = (255,0,0)
jogador = pygame.Rect(x, y, 50, 50)
pontos = 0 
# Define a posição e cor do alvo aleatoriamente
alvo_x, alvo_y = sortear_posicao()
alvo_rgb = sortear_cor()
alvo = pygame.Rect(alvo_x, alvo_y, 50, 50)

#Define a velocidade
velocidade = 5
dx = 0
dy = 0

rodando = True
while rodando:
    for evento in pygame.event.get():
        #Evento de fechar o jogo
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                dx = 0
                dy = -velocidade

            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                dx = 0
                dy = velocidade

            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                dx = -velocidade
                dy = 0

            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                dx = velocidade
                dy = 0

    jogador.x += dx
    jogador.y += dy
    # Define o fundo do jogo para branco
    tela.fill((255,255,255))


    # Verifica as bordas e impede o quadro de sair
    jogador.clamp_ip(tela.get_rect())

    # Verifica se o jogador encostou no alvo
    # Se verdadeiro, troca a cor do jogador
    # e sorteia uma nova posição/cor para o alvo 
    if jogador.colliderect(alvo):
        rgb = alvo_rgb
        alvo.topleft = sortear_posicao()
        alvo_rgb = sortear_cor()
        pontos += 1
        print(f"PONTOS = {pontos}")

    pygame.draw.rect(tela, rgb, jogador)
    pygame.draw.rect(tela, alvo_rgb, alvo)
    texto = fonte.render("Pontos: " + str(pontos), True, (0,0,0))
    tela.blit(texto, (10,10))
    pygame.display.flip()
    clock.tick(60)
    
    

pygame.quit()