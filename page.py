import pygame
from gameplay import *

pygame.init()
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)


# Function to display text on the screen
def display_text(color, screen,text, position):
    global hscore
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def homePage(screen, hscore):
    screen.fill((255, 255, 255))
    display_text('red', screen, "PRESS : 1/2/3 (easy/medium/hard) to choose level", (100, HEIGHT // 2-100))
    display_text('black', screen, "FASTEST TIMES:", (100, HEIGHT // 2))
    display_text('black', screen, f"    EASY: {hscore[0]}", (100, HEIGHT // 2+30))
    display_text('black', screen, f"    MEDIUM: {hscore[1]}", (100, HEIGHT // 2+60))
    display_text('black', screen, f"    HARD: {hscore[2]}", (100, HEIGHT // 2+90))
    pygame.display.flip()

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait=False
                return 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    wait=False
                    return 1
                elif event.key == pygame.K_2:
                    wait=False
                    return 2
                
                elif event.key==pygame.K_3:
                    wait=False
                    return 3
        
