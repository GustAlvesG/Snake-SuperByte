import pygame
import random


LARGURA = 500
ALTURA = 800
TAM = 50 #Tamanho da cobra
#TEMPO_TOTAL = tempo_restante = 5

def sortear_posicao():
    x = random.randint(0, LARGURA // TAM - 1)
    y = random.randint(0, ALTURA // TAM - 1)
    
    return x * TAM, y * TAM


def sortear_cor():
    r = random.randint(0,200)
    g = random.randint(0,200)
    b = random.randint(0,200)
    return (r,g,b)

def nascer_alvo():
    alvo.topleft = sortear_posicao()
    while alvo.colliderect(jogador):
        alvo.topleft = sortear_posicao()
    
pygame.init()

#Clock - Define a taxa de atualização
clock = pygame.time.Clock()

#Define a tela e seu tamanho
tela = pygame.display.set_mode((LARGURA, ALTURA))

#Define o título da janela
pygame.display.set_caption("Aula de Pygame muito legal e daora")

#Define a fonte do jogo
fonte = pygame.font.SysFont("arial", 28)

#Define a posição e cor iniciais do jogador
rgb = (255,0,0)
jogador = pygame.Rect(LARGURA / 2, ALTURA / 2, TAM, TAM)
pontos = 0 

# Define a posição e cor do alvo aleatoriamente
alvo_x, alvo_y = sortear_posicao()
alvo_rgb = sortear_cor()
alvo = pygame.Rect(alvo_x, alvo_y, TAM, TAM)

#Define a velocidade
velocidade = TAM
dx = 0
dy = 0


# DEFINIÇÕES - Tudo antes do while infinito
# OUVIR O JOGADOR - Capturar evento
# MUDAR O MUNDO - Atualizar o cenário
# DESENHAR O MUNDO - Atualizar a tela


rodando = jogando = True
while rodando:
    #Ouvir o jogador
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

    # Mudar o mundo
    #if tempo_restante <= 0:
    #    jogando = False  

    #Atualizar o mundo
    if jogando:
        jogador.x += dx
        jogador.y += dy

        #Verifica se bateu na parede
        if not tela.get_rect().contains(jogador):
            jogando = False

        # Verifica as bordas e impede o quadro de sair
        #jogador.clamp_ip(tela.get_rect())

        # Verifica se o jogador encostou no alvo
        # Se verdadeiro, troca a cor do jogador
        # e sorteia uma nova posição/cor para o alvo 
        if jogador.colliderect(alvo):
            rgb = alvo_rgb
            nascer_alvo()
            alvo_rgb = sortear_cor()
            pontos += 1

        tela.fill((255,255,255))
        pygame.draw.rect(tela, rgb, jogador)
        pygame.draw.rect(tela, alvo_rgb, alvo)
        #tempo_restante = TEMPO_TOTAL - pygame.time.get_ticks() // 1000 
        texto = fonte.render(f"Pontos: {str(pontos)}", True, (0,0,0))
        #tempo = fonte.render(f"Tempo: {str(tempo_restante)}", True, (0,0,0))
        tela.blit(texto, (10,10))
        #tela.blit(tempo, (10,45))

    else:
        tela.fill((255,255,255))
        mensagem = fonte.render("FIM DE JOGO", True, (0,0,0))
        texto = fonte.render(f"Pontos: {str(pontos)}", True, (0,0,0))

        tela.blit(mensagem, (LARGURA /2, ALTURA / 2))
        tela.blit(texto, (LARGURA /2, ALTURA / 2 + 35))

    pygame.display.flip()
    clock.tick(3)
pygame.quit()