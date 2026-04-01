import pygame
import sys

# ------------------------------------------------------------------ #
# COSTANTI                                                             #
# ------------------------------------------------------------------ #

SCREEN_W = 800
SCREEN_H = 600
FPS      = 60

BALL_RADIUS = 30
BALL_SPEED  = 4          # pixel per frame (tastiera)

BG_COLOR   = ( 30,  30,  30)
TEXT_COLOR = (200, 200, 200)

# Colori disponibili per il cambio al clic
COLORS = [
    (220,  80,  80),   # rosso
    ( 80, 180, 220),   # azzurro
    ( 80, 220, 120),   # verde
    (220, 200,  80),   # giallo
    (180,  80, 220),   # viola
]

# ------------------------------------------------------------------ #
# INIZIALIZZAZIONE                                                     #
# ------------------------------------------------------------------ #

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Pallina interattiva")
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("Arial", 22)

# ------------------------------------------------------------------ #
# STATO                                                                #
# ------------------------------------------------------------------ #

ball_x      = SCREEN_W // 2
ball_y      = SCREEN_H // 2
color_index = 0                      # indice corrente in COLORS
ball_color  = COLORS[color_index]

# ------------------------------------------------------------------ #
# FUNZIONI DI SUPPORTO                                                 #
# ------------------------------------------------------------------ #

def clamp(value: int, min_val: int, max_val: int) -> int:
    """
    Restituisce value se è compreso tra min_val e max_val,
    altrimenti restituisce il limite più vicino.
    """
    return max(min_val, min(value, max_val))


def point_in_circle(px: int, py: int,
                    cx: int, cy: int, radius: int) -> bool:
    """
    Restituisce True se il punto (px, py) si trova
    all'interno del cerchio con centro (cx, cy) e raggio radius.
    """
    # Evitiamo la radice quadrata confrontando il quadrato della distanza 
    # con il quadrato del raggio per una maggiore efficienza.
    distanza_quadrata = (px - cx)**2 + (py - cy)**2
    return distanza_quadrata <= radius**2


def next_color(current_index: int) -> tuple:
    """
    Restituisce la tupla (nuovo_indice, nuovo_colore)
    passando al colore successivo nella lista COLORS.
    """
    nuovo_indice = (current_index + 1) % len(COLORS)
    return nuovo_indice, COLORS[nuovo_indice]

# ------------------------------------------------------------------ #
# LOOP PRINCIPALE                                                      #
# ------------------------------------------------------------------ #

running = True

while running:

    # ---- 1. EVENTI ------------------------------------------------ #

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # -- Clic del mouse --
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 corrisponde al clic sinistro
                mouse_x, mouse_y = event.pos
                if point_in_circle(mouse_x, mouse_y, ball_x, ball_y, BALL_RADIUS):
                    color_index, ball_color = next_color(color_index)


    # ---- 2. AGGIORNA ---------------------------------------------- #

    keys = pygame.key.get_pressed()

    # -- Tastiera --
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ball_x -= BALL_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ball_x += BALL_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        ball_y -= BALL_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        ball_y += BALL_SPEED

    # Manteniamo la pallina all'interno dello schermo
    # Sottraiamo/aggiungiamo il raggio per far sì che rimbalzi sul bordo, 
    # non quando il suo centro esce dallo schermo.
    ball_x = clamp(ball_x, BALL_RADIUS, SCREEN_W - BALL_RADIUS)
    ball_y = clamp(ball_y, BALL_RADIUS, SCREEN_H - BALL_RADIUS)


    # ---- 3. DISEGNA ----------------------------------------------- #

    screen.fill(BG_COLOR)

    # Disegna la pallina
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), BALL_RADIUS)


    # HUD: istruzioni a schermo
    hints = [
        "Frecce / WASD: muovi la pallina",
        "Clic sinistro sulla pallina: cambia colore",
    ]
    for i, line in enumerate(hints):
        surf = font.render(line, True, TEXT_COLOR)
        screen.blit(surf, (10, 10 + i * 28))

    pygame.display.flip()
    clock.tick(FPS)

# ------------------------------------------------------------------ #
# USCITA                                                               #
# ------------------------------------------------------------------ #

pygame.quit()
sys.exit()