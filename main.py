import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/GAME.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счетчик попаданий
score = 0
font = pygame.font.Font(None, 36)

# Таймер
start_time = pygame.time.get_ticks()
time_limit = 30000  # 30 секунд

# Звук при попадании
pygame.mixer.init()
sound_hit = pygame.mixer.Sound("img/hit.wav")

running = True
while running:
    screen.fill(color)
    
    # Таймер
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time > time_limit:
        running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_width = max(20, target_width - 5)  # Уменьшаем мишень
                target_height = max(20, target_height - 5)
                score += 1
                sound_hit.play()
    
    screen.blit(pygame.transform.scale(target_img, (target_width, target_height)), (target_x, target_y))
    
    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

pygame.quit()