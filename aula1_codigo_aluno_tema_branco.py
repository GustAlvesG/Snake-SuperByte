import pygame

# --- CONFIGURAÇÕES ---
LINHAS = 20
COLUNAS = 10
TAM = 30

LARGURA = COLUNAS * TAM
ALTURA = LINHAS * TAM

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)   # ◀ TEMA BRANCO: cor nova, para o fundo
CINZA = (120, 120, 120)    # ◀ TEMA BRANCO: era (40, 40, 40) — a grade precisa aparecer no branco
VERDE = (0, 150, 0)        # ◀ TEMA BRANCO: era (0, 255, 0) — o verde claro some no branco
CIANO = (0, 255, 255)

def criar_tabuleiro():
    tabuleiro = []
    for linha in range(LINHAS):
        tabuleiro.append([0] * 10)
    return tabuleiro
def desenhar_tabuleiro(tela, tabuleiro):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x = coluna * TAM
            y = linha * TAM
            celula = pygame.Rect(x, y, TAM, TAM)

            if (linha + coluna) % 2 == 0:
                tabuleiro[linha][coluna] = 1
            
            if tabuleiro[linha][coluna] == 0:
                pygame.draw.rect(tela, CINZA, celula, 1)   # ◀ TEMA BRANCO: era VERDE — a borda das casas vazias vira grade cinza
            else:
                pygame.draw.rect(tela, VERDE, celula)


pygame.init()

#Clock - Define a taxa de atualização
clock = pygame.time.Clock()

#Define a tela e seu tamanho
tela = pygame.display.set_mode((LARGURA, ALTURA))

#Define o título da janela
pygame.display.set_caption("SuperTetris")

tabuleiro = criar_tabuleiro()

rodando = True
while rodando:
    #Ouvir o jogador
    for evento in pygame.event.get():
        #Evento de fechar o jogo
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(BRANCO)   # ◀ TEMA BRANCO: era PRETO

    desenhar_tabuleiro(tela, tabuleiro)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
