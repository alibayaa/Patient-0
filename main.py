import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Patient 0')
clock = pygame.time.Clock()
game_active = True

background_surface = pygame.image.load('graphics/background.png').convert()
ground_surface = pygame.image.load('graphics/floor.png').convert()

scaled_bg = pygame.transform.scale(background_surface, (1000, 600))
scaled_floor = pygame.transform.scale(ground_surface, (1000, 100))

text_font = pygame.font.Font('graphics/Pixeltype.ttf', 40)
score_surface = text_font.render('Score:', False, 'darkslategray4')
score_rect = score_surface.get_rect(center = (500, 50))

slime1_surface = pygame.image.load('graphics/slime/slime1.png').convert_alpha()
scaled_slime1 = pygame.transform.scale(slime1_surface, (175, 50))
slime_rect = scaled_slime1.get_rect(midbottom = (1000, 500))
slime_rect.size = (50, 50)

player_surface = pygame.image.load('graphics/player/playeridle.png').convert_alpha()
scaled_playeridle = pygame.transform.scale(player_surface, (250, 125))
player_rect = scaled_playeridle.get_rect(midbottom = (100, 500))
player_rect.size = (73, 125)
player_gravity = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 500:
                        player_gravity = -20
    
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
            
    
    if game_active:
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_floor, (0, 500))
    
        # Score

        pygame.draw.rect(screen, "darkslategray3", score_rect)
        pygame.draw.rect(screen, 'darkslategrey', score_rect, 2)
        screen.blit(score_surface, (score_rect))
    
        # Slime

        screen.blit(scaled_slime1, slime_rect)
        slime_rect.x -= 5
        if slime_rect.right <= 0: slime_rect.left = 1000
    
        # Player

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 500: player_rect.bottom = 500
        screen.blit(scaled_playeridle, player_rect)

        # Collisions
    
        if slime_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')

        pygame.display.update()
        clock.tick(60)