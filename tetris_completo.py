# import pygame
# import random

# # 1 - CABEÇA DA COBRA DE COR DIFERENTE;
# # 2 - PONTOS = TAMANHO DA COBRA;
# # 3 - CADA PEDAÇO DA COR DO ALVO;
# # 4 - VENENO - DOIS ALVOS, 1 É O VENENO, SE PEGAR O VENENO, PERDE UMA PARTE
# # 5 - BANQUETE - TRÊS ALVOS, O BANQUETE VALE 3 PONTOS
# # 6 - MAIS RÁPIDO - A cada 3 pontos, o jogo fica um pouco mais rápido
# # 7 - BARREIRAS - A cada 5 pontos, surgem obstáculos no mapa
# # 8 - RESTART - Ao perder, apertar R reinicia tudo

# LARGURA = 600
# ALTURA = 600

# TAM = 50 #Tamanho da cobra
# #TEMPO_TOTAL = tempo_restante = 5

 
# def sortear_posicao():
#     x = random.randint(0, LARGURA // TAM - 1)
#     y = random.randint(0, ALTURA // TAM - 1)
    
#     return x * TAM, y * TAM


# def sortear_cor():
#     r = random.randint(0,200)
#     g = random.randint(0,200)
#     b = random.randint(0,200)
#     return (r,g,b)


# def lugar_livre(objeto):
#     ocupados = cobra + barreiras + [alvo, veneno, banquete]
#     ocupados.remove(objeto)
#     return objeto.collidelist(ocupados) == -1

# def nascer(objeto):
#     objeto.topleft = sortear_posicao()
#     while not lugar_livre(objeto):
#         objeto.topleft = sortear_posicao()

# def nascer_alvos():
#     nascer(alvo)
#     nascer(veneno)
#     nascer(banquete)
    
# pygame.init()

# #Clock - Define a taxa de atualização
# clock = pygame.time.Clock()

# #Define a tela e seu tamanho
# tela = pygame.display.set_mode((LARGURA, ALTURA))

# #Define o título da janela
# pygame.display.set_caption("Aula de Pygame muito legal e daora")

# #Define a fonte do jogo
# fonte = pygame.font.SysFont("arial", 28)

# #Define a posição e cor iniciais do jogador
# #rgb = (255,0,0)
# cores = [(255,0,0)]
# cobra = [pygame.Rect(LARGURA / 2, ALTURA / 2, TAM, TAM)]



# #Define a velocidade
# velocidade = TAM
# dx = 0
# dy = 0

# # Define a posição e cor do alvo aleatoriamente
# alvo_rgb = sortear_cor()
# alvo = pygame.Rect(0, 0, TAM, TAM)

# # Define a posição e cor do veneno aleatoriamente
# veneno_rgb = alvo_rgb
# veneno = pygame.Rect(0, 0, TAM, TAM)

# # Define a posição e cor do banquete aleatoriamente
# banquete_rgb = alvo_rgb
# banquete = pygame.Rect(0, 0, TAM, TAM)

# # Define a posição e cor do barreira aleatoriamente
# barreira_rgb = (0,0,0)
# barreiras = []

# nascer_alvos()

# # DEFINIÇÕES - Tudo antes do while infinito
# # OUVIR O JOGADOR - Capturar evento
# # MUDAR O MUNDO - Atualizar o cenário
# # DESENHAR O MUNDO - Atualizar a tela

# direcao = ''
# rodando = jogando = True
# while rodando:
#     #Ouvir o jogador
#     for evento in pygame.event.get():
#         #Evento de fechar o jogo
#         if evento.type == pygame.QUIT:
#             rodando = False

#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_ESCAPE:
#                 rodando = False

#             if (evento.key == pygame.K_UP or evento.key == pygame.K_w) and direcao != 'baixo':
#                 dx = 0
#                 dy = -velocidade
#                 direcao = 'cima'

#             if (evento.key == pygame.K_DOWN or 
#                 evento.key == pygame.K_s) \
#                 and direcao != 'cima':
#                 dx = 0
#                 dy = velocidade
#                 direcao = 'baixo'

#             if (evento.key == pygame.K_LEFT or evento.key == pygame.K_a) and direcao != 'direita':
#                 dx = -velocidade
#                 dy = 0
#                 direcao = 'esquerda'

#             if (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d) and direcao != 'esquerda':
#                 dx = velocidade
#                 dy = 0
#                 direcao = 'direita'

#             if (evento.key == pygame.K_r and not jogando):
#                 cobra = [pygame.Rect(LARGURA / 2, ALTURA / 2, TAM, TAM)]
#                 cores = [(255,0,0)]
#                 barreiras = []
#                 dx = dy = 0
#                 direcao = ''
#                 nascer_alvos()
#                 jogando = True

#     # Mudar o mundo
#     #if tempo_restante <= 0:
#     #    jogando = False  

#     if jogando:
#         #jogador.x += dx
#         #jogador.y += dy

#         nova = cobra[0].move(dx, dy)
#         cobra.insert(0, nova)

#         #Verifica se bateu na parede
#         if not tela.get_rect().contains(cobra[0]):
#             jogando = False

        

#         # Verifica as bordas e impede o quadro de sair
#         #jogador.clamp_ip(tela.get_rect())

#         # Verifica se o jogador encostou no alvo
#         # Se verdadeiro, troca a cor do jogador
#         # e sorteia uma nova posição/cor para o alvo 
#         if nova.colliderect(alvo):
#             rgb = alvo_rgb
#             cores.append(alvo_rgb)
#             nascer_alvos()
#             alvo_rgb = sortear_cor()
#         elif nova.colliderect(banquete):
#             for i in range(2):
#                 cobra.append(cobra[-1].copy())

#             for i in range(3):
#                 cores.append(alvo_rgb)
#             nascer_alvos()
#         else:
#             cobra.pop()
     

#         if nova.colliderect(veneno):
#             if len(cobra) == 1:
#                 jogando = False
#             else:
#                 cobra.pop() # Perco uma parte
#                 #cobra.pop() # Remoção padrão
#                 nascer_alvos()
                

#         if cobra[0].collidelist(cobra[1:]) != -1:
#             jogando = False

#         if cobra[0].collidelist(barreiras) != -1:
#             jogando = False

#         while len(barreiras) < (len(cobra) -1) // 5:
#             largura = altura = TAM
#             posicao = random.randint(1,2)
#             if posicao == 1:
#                 largura = 2 *TAM
#             else:
#                 altura = 2 * TAM
#             barreira = pygame.Rect(0,0,largura, altura)
#             barreiras.append(barreira)
#             nascer(barreira)
            
#         #Atualizar o mundo
#         tela.fill((255,255,255))
        

#         for parte in range(1, len(cobra)):
#             pygame.draw.rect(tela, cores[parte], cobra[parte])

#         pygame.draw.rect(tela, (0,255,0), cobra[0])

#         #DESENHO DO ALVO
#         pygame.draw.rect(tela, (255, 0, 0), alvo)

#         #DESENHO do VENENO
#         pygame.draw.rect(tela, (0,255,0), veneno)
        
#         #DESENHO do BANQUETE
#         pygame.draw.rect(tela, (0,0,255), banquete)

#         for barreira in barreiras:
#             pygame.draw.rect(tela, (0,0,0), barreira)

#         texto = fonte.render(f"Pontos: {str(len(cobra) -1)}", True, (0,0,0))
#         tela.blit(texto, (10,10))
        

#     else:
#         tela.fill((255,255,255))
#         mensagem = fonte.render("FIM DE JOGO", True, (0,0,0))
#         texto = fonte.render(f"Pontos: {len(cobra) -1}", True, (0,0,0))

#         tela.blit(mensagem, (LARGURA /2, ALTURA / 2))
#         tela.blit(texto, (LARGURA /2, ALTURA / 2 + 35))

#     pygame.display.flip()
#     clock.tick(5 + ((len(cobra) -1) // 3))
    
# pygame.quit()


# Tetris — versão completa do projeto
#
# Controles:
#   Setas esquerda/direita: mover
#   Seta para cima: girar
#   Seta para baixo (segurando): descer mais rápido
#   Espaço: cair de vez
#   P: pausa
#   R: recomeçar (depois do fim de jogo)

import random
import pygame

# --- Configurações ---
LINHAS = 20
COLUNAS = 10
TAM = 30      # tamanho de cada célula, em pixels
PAINEL = 180  # largura do painel do lado direito

LARGURA = COLUNAS * TAM + PAINEL
ALTURA = LINHAS * TAM

PRETO = (0, 0, 0)
CINZA = (40, 40, 40)
CINZA_PAINEL = (22, 22, 28)
CINZA_CLARO = (150, 150, 150)
BRANCO = (255, 255, 255)

# Cada peça tem um número de 1 a 7. É esse número que vai para a matriz,
# e ele também é a posição da cor da peça na lista CORES (0 = vazio).
CORES = [
    PRETO,            # 0  vazio
    (0, 200, 220),    # 1  I  ciano
    (240, 200, 0),    # 2  O  amarelo
    (160, 60, 200),   # 3  T  roxo
    (240, 140, 0),    # 4  L  laranja
    (40, 90, 230),    # 5  J  azul
    (60, 190, 70),    # 6  S  verde
    (220, 50, 50),    # 7  Z  vermelho
]

# O formato de cada peça: suas 4 células como (linha, coluna),
# contadas a partir do centro da peça, que é o (0, 0).
# A peça gira em volta desse centro.
FORMAS = [
    [],                                    # 0  (vazio)
    [(0, -1), (0, 0), (0, 1), (0, 2)],     # 1  I
    [(-1, 0), (-1, 1), (0, 0), (0, 1)],    # 2  O
    [(0, -1), (0, 0), (0, 1), (-1, 0)],    # 3  T
    [(0, -1), (0, 0), (0, 1), (-1, 1)],    # 4  L
    [(0, -1), (0, 0), (0, 1), (-1, -1)],   # 5  J
    [(0, -1), (0, 0), (-1, 0), (-1, 1)],   # 6  S
    [(-1, -1), (-1, 0), (0, 0), (0, 1)],   # 7  Z
]
PECA_O = 2  # o quadrado não gira

# Pontos por limpar 0, 1, 2, 3 ou 4 linhas de uma vez (multiplicados pelo nível)
PONTOS_POR_LINHAS = [0, 100, 300, 500, 800]


# --- A matriz ---

def criar_tabuleiro():
    tabuleiro = []
    for linha in range(LINHAS):
        tabuleiro.append([0] * COLUNAS)
    return tabuleiro


def cabe(tabuleiro, celulas, linha, coluna):
    # A peça cabe nessa posição? Toda célula precisa estar dentro do
    # tabuleiro e em cima de um 0.
    # dl, dc: quanto a célula está deslocada do centro da peça
    for dl, dc in celulas:
        l = linha + dl
        c = coluna + dc
        if l < 0 or l >= LINHAS:
            return False
        if c < 0 or c >= COLUNAS:
            return False
        if tabuleiro[l][c] != 0:
            return False
    return True


def girar(celulas):
    # (linha, coluna) vira (coluna, -linha): 90 graus no sentido horário
    giradas = []
    for dl, dc in celulas:
        giradas.append((dc, -dl))
    return giradas


def fixar_peca(tabuleiro, celulas, linha, coluna, tipo):
    # A peça pousou: suas células viram parte da matriz
    for dl, dc in celulas:
        tabuleiro[linha + dl][coluna + dc] = tipo


def limpar_linhas(tabuleiro):
    # Tira as linhas cheias e coloca linhas vazias no topo.
    # Devolve quantas linhas foram limpas.
    removidas = 0
    for linha in range(LINHAS):
        if 0 not in tabuleiro[linha]:
            tabuleiro.pop(linha)
            tabuleiro.insert(0, [0] * COLUNAS)
            removidas += 1
    return removidas


# --- Desenho ---

def desenhar_bloco(tela, x, y, cor):
    bloco = pygame.Rect(x, y, TAM, TAM)
    pygame.draw.rect(tela, cor, bloco)
    pygame.draw.rect(tela, PRETO, bloco, 1)


def desenhar_tabuleiro(tela, tabuleiro):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x = coluna * TAM
            y = linha * TAM
            valor = tabuleiro[linha][coluna]
            if valor == 0:
                celula = pygame.Rect(x, y, TAM, TAM)
                pygame.draw.rect(tela, CINZA, celula, 1)
            else:
                desenhar_bloco(tela, x, y, CORES[valor])


def desenhar_peca(tela, celulas, linha, coluna, tipo):
    for dl, dc in celulas:
        x = (coluna + dc) * TAM
        y = (linha + dl) * TAM
        desenhar_bloco(tela, x, y, CORES[tipo])


def escrever(tela, fonte, texto, x, y, cor):
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))


def desenhar_painel(tela, fonte, fonte_pequena, proximo, pontos, linhas_feitas, nivel):
    x0 = COLUNAS * TAM
    pygame.draw.rect(tela, CINZA_PAINEL, pygame.Rect(x0, 0, PAINEL, ALTURA))
    x = x0 + 20

    escrever(tela, fonte_pequena, "PRÓXIMA", x, 20, CINZA_CLARO)
    for dl, dc in FORMAS[proximo]:
        bx = x + 10 + (dc + 1) * TAM
        by = 50 + (dl + 1) * TAM
        desenhar_bloco(tela, bx, by, CORES[proximo])

    escrever(tela, fonte_pequena, "PONTOS", x, 150, CINZA_CLARO)
    escrever(tela, fonte, str(pontos), x, 170, BRANCO)
    escrever(tela, fonte_pequena, "LINHAS", x, 225, CINZA_CLARO)
    escrever(tela, fonte, str(linhas_feitas), x, 245, BRANCO)
    escrever(tela, fonte_pequena, "NÍVEL", x, 300, CINZA_CLARO)
    escrever(tela, fonte, str(nivel), x, 320, BRANCO)

    controles = ["Setas: mover", "Cima: girar", "Baixo: descer", "Espaço: cair", "P: pausa"]
    y = 440
    for texto in controles:
        escrever(tela, fonte_pequena, texto, x, y, CINZA_CLARO)
        y += 26


def mensagem(tela, fonte_grande, fonte, titulo, subtitulo):
    faixa = pygame.Rect(0, ALTURA // 2 - 60, COLUNAS * TAM, 120)
    pygame.draw.rect(tela, PRETO, faixa)
    pygame.draw.rect(tela, BRANCO, faixa, 2)
    imagem = fonte_grande.render(titulo, True, BRANCO)
    tela.blit(imagem, imagem.get_rect(center=(faixa.centerx, faixa.centery - 18)))
    imagem = fonte.render(subtitulo, True, CINZA_CLARO)
    tela.blit(imagem, imagem.get_rect(center=(faixa.centerx, faixa.centery + 25)))


# --- Programa principal ---

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetris")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)
fonte_pequena = pygame.font.Font(None, 24)
fonte_grande = pygame.font.Font(None, 52)

reiniciar = True
rodando = True
while rodando:
    # --- Começo de um jogo novo ---
    if reiniciar:
        tabuleiro = criar_tabuleiro()
        pontos = 0
        linhas_feitas = 0
        proximo = random.randint(1, 7)
        nova_peca = True
        travar = False
        pausado = False
        fim_de_jogo = False
        reiniciar = False

    # --- Uma peça nova nasce no topo ---
    if nova_peca:
        tipo = proximo
        proximo = random.randint(1, 7)
        celulas = FORMAS[tipo]
        peca_linha = 1
        peca_coluna = COLUNAS // 2 - 1
        ultima_queda = pygame.time.get_ticks()
        nova_peca = False
        if not cabe(tabuleiro, celulas, peca_linha, peca_coluna):
            fim_de_jogo = True

    nivel = linhas_feitas // 10 + 1
    intervalo = max(100, 500 - (nivel - 1) * 40)  # milissegundos entre uma queda e outra

    # --- Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.KEYDOWN:
            if fim_de_jogo:
                if evento.key == pygame.K_r:
                    reiniciar = True

            elif evento.key == pygame.K_p:
                pausado = not pausado

            elif not pausado:
                if evento.key == pygame.K_LEFT:
                    if cabe(tabuleiro, celulas, peca_linha, peca_coluna - 1):
                        peca_coluna -= 1
                elif evento.key == pygame.K_RIGHT:
                    if cabe(tabuleiro, celulas, peca_linha, peca_coluna + 1):
                        peca_coluna += 1
                elif evento.key == pygame.K_UP and tipo != PECA_O:
                    giradas = girar(celulas)
                    if cabe(tabuleiro, giradas, peca_linha, peca_coluna):
                        celulas = giradas
                elif evento.key == pygame.K_SPACE:
                    while cabe(tabuleiro, celulas, peca_linha + 1, peca_coluna):
                        peca_linha += 1
                    travar = True

    # --- Gravidade ---
    if not pausado and not fim_de_jogo and not travar:
        espera = intervalo
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            espera = 40
        agora = pygame.time.get_ticks()
        if agora - ultima_queda > espera:
            ultima_queda = agora
            if cabe(tabuleiro, celulas, peca_linha + 1, peca_coluna):
                peca_linha += 1
            else:
                travar = True

    # --- A peça pousou ---
    if travar:
        fixar_peca(tabuleiro, celulas, peca_linha, peca_coluna, tipo)
        removidas = limpar_linhas(tabuleiro)
        linhas_feitas += removidas
        pontos += PONTOS_POR_LINHAS[removidas] * nivel
        nova_peca = True
        travar = False

    # --- Desenho ---
    tela.fill(PRETO)
    desenhar_tabuleiro(tela, tabuleiro)
    if not fim_de_jogo and not nova_peca:  # se acabou de pousar, ela já está na matriz
        desenhar_peca(tela, celulas, peca_linha, peca_coluna, tipo)
    desenhar_painel(tela, fonte, fonte_pequena, proximo, pontos, linhas_feitas, nivel)
    if pausado:
        mensagem(tela, fonte_grande, fonte, "PAUSA", "P para continuar")
    if fim_de_jogo:
        mensagem(tela, fonte_grande, fonte, "FIM DE JOGO", "R para recomeçar")
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()