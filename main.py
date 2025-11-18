import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Patient 0')
clock = pygame.time.Clock()


background_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/floor.png').convert()

scaled_bg = pygame.transform.scale(background_surface, (1000, 600))
scaled_floor = pygame.transform.scale(ground_surface, (1000, 100))

text_font = pygame.font.Font('graphics/Pixeltype.ttf', 40)
text_surface = text_font.render('My game', False, 'darkslategray4')

slime1_surface = pygame.image.load('graphics/slime/slime1.png').convert_alpha()
scaled_slime1 = pygame.transform.scale(slime1_surface, (175, 50))
slime_rect = scaled_slime1.get_rect(bottomright = (1000, 500))

player_surface = pygame.image.load('graphics/player/playeridle.png').convert_alpha()
scaled_playeridle = pygame.transform.scale(player_surface, (250, 125))
player_rect = scaled_playeridle.get_rect(midbottom = (100, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(scaled_bg, (0, 0))
    screen.blit(scaled_floor, (0, 500))
    screen.blit(text_surface, (0, 0))
    
    screen.blit(scaled_slime1, slime_rect)
    slime_rect.x -= 4

    player_rect.left += 1
    screen.blit(scaled_playeridle, player_rect)


    pygame.display.update()
    clock.tick(60)