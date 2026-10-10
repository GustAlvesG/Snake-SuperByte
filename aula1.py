import pygame
import random

# 1 - CABEÇA DA COBRA DE COR DIFERENTE;
# 2 - PONTOS = TAMANHO DA COBRA;
# 3 - CADA PEDAÇO DA COR DO ALVO;
# 4 - VENENO - DOIS ALVOS, 1 É O VENENO, SE PEGAR O VENENO, PERDE UMA PARTE
# 5 - BANQUETE - TRÊS ALVOS, O BANQUETE VALE 3 PONTOS
# 6 - MAIS RÁPIDO - A cada 3 pontos, o jogo fica um pouco mais rápido
# 7 - BARREIRAS - A cada 5 pontos, surgem obstáculos no mapa
# 8 - RESTART - Ao perder, apertar R reinicia tudo

LARGURA = 600
ALTURA = 600

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


def lugar_livre(objeto):
    ocupados = cobra + barreiras + [alvo, veneno, banquete]
    ocupados.remove(objeto)
    return objeto.collidelist(ocupados) == -1

def nascer(objeto):
    objeto.topleft = sortear_posicao()
    while not lugar_livre(objeto):
        objeto.topleft = sortear_posicao()

def nascer_alvos():
    nascer(alvo)
    nascer(veneno)
    nascer(banquete)
    
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
cores = [rgb]
cobra = [pygame.Rect(LARGURA / 2, ALTURA / 2, TAM, TAM)]



#Define a velocidade
velocidade = TAM
dx = 0
dy = 0

# Define a posição e cor do alvo aleatoriamente
alvo_rgb = sortear_cor()
alvo = pygame.Rect(0, 0, TAM, TAM)

# Define a posição e cor do veneno aleatoriamente
veneno_rgb = alvo_rgb
veneno = pygame.Rect(0, 0, TAM, TAM)

# Define a posição e cor do banquete aleatoriamente
banquete_rgb = alvo_rgb
banquete = pygame.Rect(0, 0, TAM, TAM)

# Define a posição e cor do barreira aleatoriamente
barreira_rgb = (0,0,0)
barreiras = []

nascer_alvos()

# DEFINIÇÕES - Tudo antes do while infinito
# OUVIR O JOGADOR - Capturar evento
# MUDAR O MUNDO - Atualizar o cenário
# DESENHAR O MUNDO - Atualizar a tela

direcao = ''
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

            if (evento.key == pygame.K_UP or evento.key == pygame.K_w) and direcao != 'baixo':
                dx = 0
                dy = -velocidade
                direcao = 'cima'

            if (evento.key == pygame.K_DOWN or 
                evento.key == pygame.K_s) \
                and direcao != 'cima':
                dx = 0
                dy = velocidade
                direcao = 'baixo'

            if (evento.key == pygame.K_LEFT or evento.key == pygame.K_a) and direcao != 'direita':
                dx = -velocidade
                dy = 0
                direcao = 'esquerda'

            if (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d) and direcao != 'esquerda':
                dx = velocidade
                dy = 0
                direcao = 'direita'

    # Mudar o mundo
    #if tempo_restante <= 0:
    #    jogando = False  

    if jogando:
        #jogador.x += dx
        #jogador.y += dy

        nova = cobra[0].move(dx, dy)
        cobra.insert(0, nova)

        #Verifica se bateu na parede
        if not tela.get_rect().contains(cobra[0]):
            jogando = False

        

        # Verifica as bordas e impede o quadro de sair
        #jogador.clamp_ip(tela.get_rect())

        # Verifica se o jogador encostou no alvo
        # Se verdadeiro, troca a cor do jogador
        # e sorteia uma nova posição/cor para o alvo 
        if nova.colliderect(alvo):
            rgb = alvo_rgb
            cores.append(alvo_rgb)
            nascer_alvos()
            alvo_rgb = sortear_cor()
        elif nova.colliderect(banquete):
            for i in range(2):
                cobra.append(cobra[-1].copy())

            for i in range(3):
                cores.append(alvo_rgb)
            nascer_alvos()
        else:
            cobra.pop()
     

        if nova.colliderect(veneno):
            if len(cobra) == 1:
                jogando = False
            else:
                cobra.pop() # Perco uma parte
                cobra.pop() # Remoção padrão
                nascer_alvos()
                if not len(cobra) >= 1:
                    jogando = False
                    continue

        if cobra[0].collidelist(cobra[1:]) != -1:
            jogando = False

        if cobra[0].collidelist(barreiras) != -1:
            jogando = False

        while len(barreiras) < (len(cobra) -1) // 5:
            largura = altura = TAM
            posicao = random.randint(1,2)
            if posicao == 1:
                largura = 2 *TAM
            else:
                altura = 2 * TAM
            barreira = pygame.Rect(0,0,largura, altura)
            barreiras.append(barreira)
            nascer(barreira)
            
        #Atualizar o mundo
        tela.fill((255,255,255))
        

        for parte in range(1, len(cobra)):
            pygame.draw.rect(tela, cores[parte], cobra[parte])

        pygame.draw.rect(tela, (0,255,0), cobra[0])

        #DESENHO DO ALVO
        pygame.draw.rect(tela, (255, 0, 0), alvo)

        #DESENHO do VENENO
        pygame.draw.rect(tela, (0,255,0), veneno)
        
        #DESENHO do BANQUETE
        pygame.draw.rect(tela, (0,0,255), banquete)

        for barreira in barreiras:
            pygame.draw.rect(tela, (0,0,0), barreira)

        texto = fonte.render(f"Pontos: {str(len(cobra) -1)}", True, (0,0,0))
        tela.blit(texto, (10,10))
        

    else:
        tela.fill((255,255,255))
        mensagem = fonte.render("FIM DE JOGO", True, (0,0,0))
        texto = fonte.render(f"Pontos: {len(cobra) -1}", True, (0,0,0))

        tela.blit(mensagem, (LARGURA /2, ALTURA / 2))
        tela.blit(texto, (LARGURA /2, ALTURA / 2 + 35))

    pygame.display.flip()
    clock.tick(5 + (len(cobra) // 3))
    
pygame.quit()