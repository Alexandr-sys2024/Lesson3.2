import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/GAME.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
initial_target_size = 80  # Начальный размер цели
target_width = initial_target_size
target_height = initial_target_size

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменная для хранения очков
score = 0

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Время игры (например, 30 секунд)
game_duration = 30
start_time = time.time()

running = True
while running:
    # Заполнение экрана цветом
    screen.fill(color)

    # Отображаем количество очков
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Таймер обратного отсчета
    elapsed_time = int(time.time() - start_time)
    time_left = game_duration - elapsed_time
    time_text = font.render(f"Время: {time_left}", True, (255, 255, 255))
    screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

    if time_left <= 0:
        # Время истекло, выводим результат и завершаем игру
        game_over_text = font.render(f"Игра окончена! Ваши очки: {score}", True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(5000)  # Показываем результат 5 секунд
        running = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем очки за попадание
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                # Уменьшаем размер цели, но не меньше 30 пикселей
                target_width = max(30, target_width - 5)
                target_height = max(30, target_height - 5)

    # Отображаем цель
    screen.blit(pygame.transform.scale(target_img, (target_width, target_height)), (target_x, target_y))
    pygame.display.update()

pygame.quit()



