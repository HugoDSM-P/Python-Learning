import pygame
import random
import math
from pygame import mixer

pygame.init()

# Score

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

game_active = True

# Game over text

gover = pygame.font.Font("freesansbold.ttf", 40)

def game_over():
    my_gover = gover.render("GAME OVER", True, (255, 255, 255))
    screen.blit(my_gover, (270, 200))


# Show score function

def show_score(x, y):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))

# Background music
mixer.music.load("bg_music.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Screen display

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("bg.png")

exe = True

# Title and icon

pygame.display.set_caption("Space Invaders")
game_icon = pygame.image.load("space.png")
pygame.display.set_icon(game_icon)

# Player model and position

img_player = pygame.image.load("rocket.png")
player_x = 368
player_y = 500
player_x_move = 0

# Enemy model and position

img_enemy = pygame.image.load("enemy.png")

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)
        self.x_move = random.choice([-0.5, 0.5])
        self.y_move = 30

    def update(self):
        global game_active

        if not game_active:
            return

        self.x += self.x_move

        if self.x <= 0:
            self.x_move = 0.4
            self.y += self.y_move
        elif self.x >= 736:
            self.x_move = -0.4
            self.y += self.y_move

        if self.y > 500:
            game_active = False

    def draw(self):
        if game_active:
            screen.blit(img_enemy, (self.x, self.y))

    def reset(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)

enemies = [Enemy() for _ in range(5)]

# Bullet model and position

img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_y_move = 3
bullet_visible = False


# Player

def player(x, y):
    screen.blit(img_player, (x, y))

# Shoot

def shoot(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(img_bullet, (x + 16, y + 10))

# Collision calc

def coll(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_1 - y_2, 2))
    if distance < 17:
        return True
    else:
        return False

while exe:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False

        if event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_LEFT:
                player_x_move = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_move = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_visible == False:
                    bullet_x = player_x
                    shoot(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_move = 0

    if game_active:

        # Player movement limit

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        # Bullet movement
        if bullet_y <= -16:
            bullet_y = 500
            bullet_visible = False
            
        if bullet_visible:
            shoot(bullet_x, bullet_y)
            bullet_y -= bullet_y_move

        # Enemy update and collision
        for enemy in enemies:
            enemy.update()
            enemy.draw()

            collision = coll(enemy.x, enemy.y, bullet_x, bullet_y)
            if collision:
                bullet_y = 500
                bullet_visible = False
                score += 1
                enemy.reset()

        # Move player

        player_x += player_x_move
        player(player_x, player_y)

    else:
        enemies.clear()
        game_over()

    show_score(text_x, text_y)
    
    pygame.display.update()