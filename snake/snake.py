import pygame
import random
import sys
import time

pygame.init()
cell_size = 30

screen_x = 600
screen_y = 510

snake_size = cell_size
apple_size = cell_size

apple_x = random.randrange(0, screen_x, cell_size)
apple_y = random.randrange(0, screen_y, cell_size)

snake_x = random.randrange(0, screen_x, cell_size)
snake_y = random.randrange(0, screen_y, cell_size)


score = 0
dead = False

screen_size = (screen_x, screen_y)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("snake")

fps = 8
clock = pygame.time.Clock()

text_font = pygame.font.SysFont("Arial", 30)

def text(text, font, text_color, text_x, text_y):
    img = font.render(text, True, text_color)
    screen.blit(img, (text_x, text_y))

move_snake_x = 0
move_snake_y = 0

is_running = True



while is_running:


    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
                is_running = False
        

            
        if event.type == pygame.KEYDOWN:
            if not dead:
                if event.key == pygame.K_d:
                    move_snake_x = cell_size
                    move_snake_y = 0  

                if event.key == pygame.K_a:
                    move_snake_x = -cell_size
                    move_snake_y = 0  

                if event.key == pygame.K_w:
                    move_snake_x = 0   
                    move_snake_y = -cell_size

                if event.key == pygame.K_s:
                    move_snake_x = 0   
                    move_snake_y = cell_size
                
            if event.key == pygame.K_q:
                is_running = False

    screen.fill((40, 40, 40))  
    if not dead:
        snake_x += move_snake_x
        snake_y += move_snake_y
 
    snake_rect = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
    apple_rect = pygame.Rect(apple_x, apple_y, apple_size, apple_size)
    if not dead:
        if  snake_rect.colliderect(apple_rect):
            apple_x = random.randrange(0, screen_x, cell_size)
            apple_y = random.randrange(0, screen_y, cell_size)
            score += 1

    if snake_rect.left < 0 or snake_rect.right > screen_x or snake_rect.top < 0 or snake_rect.bottom > screen_y:
        score = 0
        dead = True

    pygame.draw.rect(screen, (5, 255, 5), snake_rect)
    pygame.draw.rect(screen, (255, 5, 5), apple_rect)

    text("Score: " + str(score), text_font, (255, 255, 255), 1, 1)
    if dead == True:
        text("Game Over" , text_font, (255, 5, 5), 220, 220)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
