import pygame
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Patient 0')
clock = pygame.time.Clock()
game_active = False

# Floor

ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
scaled_floor = pygame.transform.scale(ground_surface, (1000, 100)).convert_alpha()

# Background

background_surface = pygame.image.load('graphics/background.png').convert_alpha()
scaled_bg = pygame.transform.scale(background_surface, (1000, 600)).convert_alpha()

# Text

text_font = pygame.font.Font('graphics/Pixeltype.ttf', 40)
score_surface = text_font.render('Score:  ', False, 'darkslategray4')
score_rect = score_surface.get_rect(center = (500, 50))

start_time = 0
score = 0

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f'{current_time}', False, 'darkslategray4')
    score_rect = score_surf.get_rect(center = (575, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# Obstacles

slime1_surface = pygame.image.load('graphics/slime/slime1.png').convert_alpha()
scaled_slime1 = pygame.transform.scale(slime1_surface, (175, 50))
slime_rect = scaled_slime1.get_rect(midbottom = (1000, 500))
slime_rect.size = (50, 50)

obstacle_rect_list = []

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(scaled_slime1, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

# Player

player_surface = pygame.image.load('graphics/player/playeridle.png').convert_alpha()
scaled_playeridle = pygame.transform.scale(player_surface, (250, 125)).convert_alpha()
player_rect = scaled_playeridle.get_rect(midbottom = (100, 500))
player_rect.size = (73, 125)
player_gravity = 0

# Intro Screen

player_stand = pygame.image.load('graphics/player/playerstanding.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (500, 600))

game_name = text_font.render('Patient-0', False, 'darkslategrey')
game_name_rect = game_name.get_rect(center = (500, 80))
game_message = text_font.render('Press space to run', False, 'darkslategrey')
game_message_rect = game_message.get_rect(center = (500, 175))

# Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

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
                    start_time = int(pygame.time.get_ticks() / 1000)
    
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(scaled_slime1.get_rect(midbottom = (randint(900, 1100), 500)))

    if game_active:
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_floor, (0, 500))
    
        # Score

        pygame.draw.rect(screen, "darkslategray3", score_rect)
        pygame.draw.rect(screen, 'darkslategrey', score_rect, 2)
        screen.blit(score_surface, (score_rect))
        score = display_score()
    
        # Player

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 500: player_rect.bottom = 500
        screen.blit(scaled_playeridle, player_rect)

        # Obstacle movement

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collisions
    
        if slime_rect.colliderect(player_rect):
            game_active = False
    else:    
        screen.fill('black')
        screen.blit(player_stand, player_stand_rect)
        
        score_message = text_font.render(f'Your score: {score}', False, 'darkslategrey')
        score_message_rect = score_message.get_rect(center = (500, 175))
        screen.blit(game_name, game_name_rect)
        
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        
        
        
    pygame.display.update()
    clock.tick(60)