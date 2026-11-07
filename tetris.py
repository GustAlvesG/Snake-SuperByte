import pygame

# --- CONFIGURAÇÕES ---
LINHAS = 20
COLUNAS = 10
TAM = 30

LARGURA = COLUNAS * TAM
ALTURA = LINHAS * TAM

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (120, 120, 120)
VERDE = (0, 150, 0)
CIANO = (0, 255, 255)
ROXO = (130, 40, 190)

INTERVALO = 500  # milissegundos entre uma queda e outra

#As 7 peças. Cada célula é (linha, coluna) a partir do centro (0, 0)
FORMAS = [
    [(0, -1), (0, 0), (0, 1), (0, 2)],    # 0: I
    [(-1, 0), (-1, 1), (0, 0), (0, 1)],   # 1: O
    [(0, -1), (0, 0), (0, 1), (-1, 0)],   # 2: T
    [(0, -1), (0, 0), (0, 1), (-1, 1)],   # 3: L
    [(0, -1), (0, 0), (0, 1), (-1, -1)],  # 4: J
    [(0, -1), (0, 0), (-1, 0), (-1, 1)],  # 5: S
    [(-1, -1), (-1, 0), (0, 0), (0, 1)],  # 6: Z
]

def criar_tabuleiro():
    tabuleiro = []
    for linha in range(LINHAS):
        tabuleiro.append([0] * COLUNAS)
    return tabuleiro

def desenhar_tabuleiro(tela, tabuleiro):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x = coluna * TAM
            y = linha * TAM
            celula = pygame.Rect(x, y, TAM, TAM)

            if tabuleiro[linha][coluna] == 0:
                pygame.draw.rect(tela, CINZA, celula, 1)
            else:
                pygame.draw.rect(tela, VERDE, celula)

def desenhar_peca(tela, celulas, linha, coluna):
    for dl, dc in celulas:
        x = (coluna + dc) * TAM
        y = (linha + dl) * TAM
        bloco = pygame.Rect(x, y, TAM, TAM)
        pygame.draw.rect(tela, ROXO, bloco)
        pygame.draw.rect(tela, PRETO, bloco, 1)
        
def cabe(celulas, linha, coluna):
    #A peça cabe aqui? Toda célula precisa estar dentro do tabuleiro
    for dl, dc in celulas:
        l = linha + dl
        c = coluna + dc
        if l < 0 or l >= LINHAS:
            return False
        if c < 0 or c >= COLUNAS:
            return False
    return True


pygame.init()

#Segurar uma tecla repete o KEYDOWN: espera 170 ms, depois repete a cada 50 ms
pygame.key.set_repeat(170, 50)

#Clock - Define a taxa de atualização
clock = pygame.time.Clock()

#Define a tela e seu tamanho
tela = pygame.display.set_mode((LARGURA, ALTURA))

#Define o título da janela
pygame.display.set_caption("SuperTetris")

tabuleiro = criar_tabuleiro()
tabuleiro[19][0] = 1
tabuleiro[19][1] = 1
tabuleiro[18][0] = 1

#A peça que cai: começa com o T (posição 2 de FORMAS)
indice = 2
celulas = FORMAS[indice]
peca_linha = 1
peca_coluna = 4
ultima_queda = pygame.time.get_ticks()

rodando = True
while rodando:
    #Ouvir o jogador
    for evento in pygame.event.get():
        #Evento de fechar o jogo
        if evento.type == pygame.QUIT:
            rodando = False
        #Setas: mover a peça
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                if cabe(celulas, peca_linha, peca_coluna - 1):
                    peca_coluna -= 1
            elif evento.key == pygame.K_RIGHT:
                if cabe(celulas, peca_linha, peca_coluna + 1):
                    peca_coluna += 1
            elif evento.key == pygame.K_DOWN:
                if cabe(celulas, peca_linha + 1, peca_coluna):
                    peca_linha += 1
            elif evento.key == pygame.K_a:
                while cabe(celulas, peca_linha, peca_coluna - 1):
                    peca_coluna -= 1
            elif evento.key == pygame.K_d:
                while cabe(celulas, peca_linha, peca_coluna + 1):
                    peca_coluna += 1
            elif evento.key == pygame.K_SPACE:
                while cabe(celulas, peca_linha + 1, peca_coluna):
                    peca_linha += 1
            elif evento.key == pygame.K_UP:
                proxima = (indice + 1) % len(FORMAS)
                if cabe(FORMAS[proxima], peca_linha, peca_coluna):
                    indice = proxima
                    celulas = FORMAS[indice]

    #Gravidade: a peça desce uma linha a cada INTERVALO, se couber
    agora = pygame.time.get_ticks()
    if agora - ultima_queda > INTERVALO:
        ultima_queda = agora
        if cabe(celulas, peca_linha + 1, peca_coluna):
            peca_linha += 1

    tela.fill(BRANCO)

    desenhar_tabuleiro(tela, tabuleiro)
    desenhar_peca(tela, celulas, peca_linha, peca_coluna)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()