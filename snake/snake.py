import pygame
import random
import sys
import time

pygame.init()

score = 0
dead = False

screen_x = 600
screen_y = 500
screen_size = (screen_x, screen_y)

apple_size = 30
apple_x = random.randint(0, screen_x -apple_size)
apple_y = random.randint(0, screen_y -apple_size)

player_size = 30
player_x = random.randint(0, screen_x -player_size)
player_y = random.randint(0, screen_y -player_size)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("snake")

fps = 1000
clock = pygame.time.Clock()

text_font = pygame.font.SysFont("Arial", 30)

def text(text, font, text_color, text_x, text_y):
    img = font.render(text, True, text_color)
    screen.blit(img, (text_x, text_y))

move_player_x = 0
move_player_y = 0

is_running = True

while is_running:


    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
                is_running = False
        

            
        if event.type == pygame.KEYDOWN:
            if not dead:
                if event.key == pygame.K_d:
                    move_player_x = 3
                    move_player_y = 0  

                if event.key == pygame.K_a:
                    move_player_x = -3
                    move_player_y = 0  

                if event.key == pygame.K_w:
                    move_player_x = 0   
                    move_player_y = -3

                if event.key == pygame.K_s:
                    move_player_x = 0   
                    move_player_y = 3
                
            if event.key == pygame.K_q:
                is_running = False

    screen.fill((40, 40, 40))  
    if not dead:
        player_x += move_player_x
        player_y += move_player_y
 
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    apple_rect = pygame.Rect(apple_x, apple_y, apple_size, apple_size)
    if not dead:
        if  player_rect.colliderect(apple_rect):
            apple_x = random.randint(0, screen_x -apple_size)
            apple_y = random.randint(0, screen_y -apple_size)
            player_size += 10
            score += 1

    if player_rect.left < 0 or player_rect.right > screen_x or player_rect.top < 0 or player_rect.bottom > screen_y:
        score = 0
        dead = True

    pygame.draw.rect(screen, (5, 255, 5), player_rect)
    pygame.draw.rect(screen, (255, 5, 5), apple_rect)

    text("Score: " + str(score), text_font, (255, 255, 255), 1, 1)
    if dead == True:
        text("Game Over" , text_font, (255, 5, 5), 220, 220)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
