import pygame
import sys
import random
from gameplay import *
from page import *

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
pygame.display.set_caption("Minesweeper")

clock = pygame.time.Clock()

bombImg = pygame.image.load("img/bomb.png")
expoImg = pygame.image.load("img/explosion.png")
flagImg = pygame.image.load("img/flag.png")
# image = pygame.transform.scale(image, (rect.width, rect.height))

def draw_board(game):
    global bombImg, expoImg, flagImg

    for y in range(game.ROWS):
        for x in range(game.COLS):

            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            color = REVEALED if game.VISITED[y][x] else HIDDEN
            if(game.FLAGGED[y][x]): color = MARKED

            dark_color = OUTLINE if game.VISITED[y][x] else OUTLINE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, dark_color, rect, 2)

            if game.VISITED[y][x]:
                text_surface = font.render(game.BOARD[y][x], True, FONT_COLOR)
                text_rect = text_surface.get_rect(center=(rect.centerx, rect.centery))
                screen.blit(text_surface, text_rect)
            
            if(game.FLAGGED[y][x]):
                flagImg= pygame.transform.scale(flagImg, (rect.width, rect.height))
                screen.blit(flagImg, rect)
            if(game.BOARD[y][x]=='@' and GAMEOVER):
                if(game.VISITED[y][x]):
                    expoImg= pygame.transform.scale(expoImg, (rect.width, rect.height))
                    screen.blit(expoImg, rect)
                else:
                    bombImg= pygame.transform.scale(bombImg, (rect.width, rect.height))
                    screen.blit(bombImg, rect)




def event_manager(game):
    global GAMEOVER, RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            GAMEOVER = True

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()
            cell_pos = game.get_cell_from_mouse(mouse_pos)
            row, col = cell_pos
            if(row>=game.ROWS or row<0 or col>=game.COLS or col<0):
                print("IN")
                continue

            if GAMEOVER: continue

            if event.button == 1:
                
                if(not game.FLAGGED[row][col]):
                    if not game.VISITED[row][col]:
                        game.CELL_LEFT -=1
                        game.VISITED[row][col] = True
                    if(game.BOARD[row][col]=='0'):
                        if not game.VISITED[row][col]:
                            game.CELL_LEFT -=1
                        game.dfs(row, col)

                    if(game.BOARD[row][col]=='@'):
                        GAMEOVER = True

                    print(game.CELL_LEFT)

            if event.button == 3: 
                if(not game.VISITED[row][col]):
                    game.FLAGGED[row][col] = not game.FLAGGED[row][col]


GAMEOVER= False
RUNNING = True
HSCORE = [None, None, None]
HARDNESS = [(9,9), (15,15), (16, 20)]
while RUNNING:
    GAMEOVER= False

    level = homePage(screen, HSCORE)
    if(level==0): break
    else : print(level)
    p ,q = HARDNESS[level-1]
    
    # p,q = [int(x) for x in input().split()]
    game = GamePlay(p,q, level)
    game.placeBombs()
    game.CountBombs()
    event_manager(game)
    print(game.CELL_LEFT)

    # print("OVER")
    WIN = False 
    start_time = pygame.time.get_ticks()
    while not GAMEOVER:
        if game.CELL_LEFT ==game.TOTAL_BOMBS:
            WIN = True
            print("you win")
            break

        event_manager(game)
        screen.fill((255, 255, 255))
        draw_board(game)

        current_time = pygame.time.get_ticks()

    # Calculate elapsed time in seconds
        elapsed_time = (current_time - start_time) // 1000

        # Draw the elapsed time on the screen
        display_text('black', screen, "TIME: "+str(elapsed_time), (game.COLS*CELL_SIZE+50, 50))

        pygame.display.flip()
        clock.tick(60)

    if(WIN) : 
        display_text('blue', screen, str(f"you win, your time: {elapsed_time}"),(game.COLS*CELL_SIZE+50, 100))

        HSCORE[level-1] = elapsed_time if HSCORE[level-1]== None else min(HSCORE, int(elapsed_time)) 
    if(GAMEOVER):
        display_text('red', screen, str(f"GAME OVER!!!! "),(game.COLS*CELL_SIZE+50, 100))
    pygame.display.flip()
    if RUNNING: pygame.time.delay(5000)

    


pygame.quit()
sys.exit()
