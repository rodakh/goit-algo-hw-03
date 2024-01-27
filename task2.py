import pygame
import math


# Функція для малювання кривої Коха
def koch_curve(start, end, depth):
    if depth == 0:
        pygame.draw.line(screen, (255, 255, 255), start, end)
    else:
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        dist = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) / 3

        p1 = (start[0] + dist * math.cos(angle), start[1] + dist * math.sin(angle))
        p2 = (start[0] + 2 * dist * math.cos(angle), start[1] + 2 * dist * math.sin(angle))

        angle += math.pi / 3
        p3 = (p1[0] + dist * math.cos(angle), p1[1] + dist * math.sin(angle))

        koch_curve(start, p1, depth - 1)
        koch_curve(p1, p3, depth - 1)
        koch_curve(p3, p2, depth - 1)
        koch_curve(p2, end, depth - 1)

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Сніжинка Коха')

background_color = (0, 0, 0)

# Налаштування сніжинки Коха
depth = 4  # Рівень рекурсії
size = 300
start_point = (width // 2 - size // 2, height // 2 + size // 3)
end_point = (width // 2 + size // 2, height // 2 + size // 3)

# Головний цикл програми
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    # Малювання сніжинки
    koch_curve(start_point, end_point, depth)
    koch_curve(end_point, (
    start_point[0] + (end_point[0] - start_point[0]) / 2, start_point[1] - size * math.sin(math.radians(60))), depth)
    koch_curve(
        (start_point[0] + (end_point[0] - start_point[0]) / 2, start_point[1] - size * math.sin(math.radians(60))),
        start_point, depth)

    pygame.display.flip()

# Завершення Pygame
pygame.quit()
