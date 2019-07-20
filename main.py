import pygame
import random

pygame.init()

background = pygame.image.load("background_image.jpg")
background_size = background.get_rect().size # background_size[0] == x, background_size[1] == y
screen = pygame.display.set_mode(background_size)

BLUE = [0, 0, 255]
RED = [193, 0, 32]
GREEN = [42, 194, 0]

enemies = []
ENEMY_SIZE = (30, 20)

player_color = BLUE

x = int(background_size[0] / 2)
y = int(background_size[1] / 2)

speed_x = 0
speed_y = 0

enemy_speed = 0.5

score = 0


def init_enemies():
    for enemy in range(0, 10):
        new_enemy_pos_y = random.randint(5, background_size[1] - 5)
        new_enemy_pos_x = background_size[0] + (background_size[0] / 2 / 2)
        enemy_rect = pygame.Rect(new_enemy_pos_x, new_enemy_pos_y, ENEMY_SIZE[1], ENEMY_SIZE[0])
        new_enemy = [new_enemy_pos_y, new_enemy_pos_x, enemy_rect]
        enemies.append(new_enemy)


init_enemies()
attacking_enemy = enemies[0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_y = -1
            elif event.key == pygame.K_DOWN:
                speed_y = 1
            elif event.key == pygame.K_LEFT:
                speed_x = -1
            elif event.key == pygame.K_RIGHT:
                speed_x = 1
            elif event.key == pygame.K_LSHIFT:
                if speed_y < 0:
                    speed_y = -5
                elif speed_y > 0:
                    speed_y = 5
                elif speed_x < 0:
                    speed_x = -5
                elif speed_x > 0:
                    speed_x = 5
            elif event.key == pygame.K_RETURN:
                player_color = RED
                if player.colliderect(attacking_enemy[2]):
                    score += 100
                    print(f"KILL! Score: {score}")
                    enemies.remove(attacking_enemy)
                    del attacking_enemy
                    enemy_speed += 0.1
                    try:
                        attacking_enemy = enemies[0]
                    except IndexError:
                        init_enemies()
                        attacking_enemy = enemies[0]

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                speed_y = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                speed_x = 0
            elif event.key == pygame.K_RETURN:
                player_color = BLUE

    screen.blit(background, (0, 0))
    attacking_enemy[2] = pygame.draw.rect(screen, GREEN, (attacking_enemy[1], attacking_enemy[0], ENEMY_SIZE[0], ENEMY_SIZE[1]))
    attacking_enemy[1] -= enemy_speed
    if attacking_enemy[1] <= 0:
        del attacking_enemy
        del enemies
        del player
        print(f"You lose! You got: {score} points")
        break
    else:
        player = pygame.draw.circle(screen, player_color, (x, y), 10)
        if x >= background_size[0]:
            speed_x = -1
        if x <= 0:
            speed_x = 1
        if y >= background_size[1]:
            speed_y = -1
        if y <= 0:
            speed_y = 1
        x += speed_x
        y += speed_y
        pygame.display.update()
