import pygame
import sys
import random

# Inicializa todos os módulos do pygame
pygame.init()

# Definição do tamanho da janela do jogo
WIDTH, HEIGHT = 800, 500

# Cria a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o título da janela
pygame.display.set_caption("Arcade DevOps Game")

# Definição de cores (RGB)
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
YELLOW = (255, 200, 0)
BLACK = (0,0,0)

# CONFIGURAÇÕES DO JOGADOR

# Tamanho do jogador
player_size = 40

# Posição inicial do jogador (centro da tela)
player_x = WIDTH // 2
player_y = HEIGHT // 2

# Velocidade de movimentação
speed = 5

# CONFIGURAÇÕES DA MOEDA

# Raio da moeda
coin_radius = 10

# Posição aleatória inicial da moeda
coin_x = random.randint(50, WIDTH-50)
coin_y = random.randint(50, HEIGHT-50)

# SISTEMA DE PONTUAÇÃO

# Pontuação inicial
score = 0

# Fonte usada para exibir o score
font = pygame.font.SysFont(None, 30)

# Controla o FPS do jogo
clock = pygame.time.Clock()

# LOOP PRINCIPAL DO JOGO

while True:

    # Limita o jogo a 60 quadros por segundo
    clock.tick(60)

    # Verifica eventos do jogo (fechar janela, teclado etc)
    for event in pygame.event.get():

        # Se o usuário fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimentação do jogador com as setas
    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    if keys[pygame.K_UP]:
        player_y -= speed

    if keys[pygame.K_DOWN]:
        player_y += speed

    # Cria um retângulo para representar o jogador
    # Isso facilita detectar colisões
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # Cria um retângulo invisível em volta da moeda
    # usado para detectar colisão com o jogador
    coin_rect = pygame.Rect(
        coin_x-coin_radius,
        coin_y-coin_radius,
        coin_radius*2,
        coin_radius*2
    )

    # DETECÇÃO DE COLISÃO

    # Se o jogador encostar na moeda
    if player_rect.colliderect(coin_rect):

        # aumenta a pontuação
        score += 1

        # gera nova posição aleatória para a moeda
        coin_x = random.randint(50, WIDTH-50)
        coin_y = random.randint(50, HEIGHT-50)


    screen.fill(WHITE)

    # desenha o jogador
    pygame.draw.rect(screen, BLUE, player_rect)

    # desenha a moeda
    pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), coin_radius)

    # cria o texto do score
    score_text = font.render(f"Score: {score}", True, BLACK)

    # desenha o score na tela
    screen.blit(score_text, (10,10))

    # atualiza a tela
    pygame.display.update()