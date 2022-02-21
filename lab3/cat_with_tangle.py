import pygame
import pygame.draw as dr
from numpy import pi, sin

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))
# Фон
dr.rect(screen, (66, 64, 0), (0, 0, 400, 300))
dr.rect(screen, (125, 102, 6), (0, 300, 400, 300))
# Окно
dr.rect(screen, (240, 240, 255), (200, 20, 180, 270))
dr.rect(screen, (78, 195, 226), (210, 30, 75, 75))
dr.rect(screen, (78, 195, 226), (295, 30, 75, 75))
dr.rect(screen, (78, 195, 226), (210, 115, 75, 165))
dr.rect(screen, (78, 195, 226), (295, 115, 75, 165))

# Хвост
# dr.rect(screen, (182, 86, 35), [135, 260, 100, 30], 0, border_radius=400,
#           border_top_left_radius=0)
dr.arc(screen, (182, 86, 35), (200 - 150, 300 + 60, 400, 160), pi / 6, pi / 2, width=60)
dr.arc(screen, (182, 86, 35), (200 + 50, 300 - 15, 400, 160), pi / 6 + pi, pi + pi / 2, width=59)
dr.arc(screen, 'black', (200 - 150, 300 + 60, 400, 160), pi / 6, pi / 2, width=1)
dr.arc(screen, 'black', (200 + 50, 300 - 15, 400, 160), pi / 6 + pi, pi + pi / 2, width=1)

dr.ellipse(screen, (182, 86, 35), (50, 330, 266, 130), 0)
dr.ellipse(screen, (0, 0, 0), (50, 330, 266, 130), 1)

dr.circle(screen, (182, 86, 35), (265, 424), 45)
dr.circle(screen, (0, 0, 0), (265, 424), 45, 1)

dr.ellipse(screen, (182, 86, 35), (286, 437, 30, 75))
dr.ellipse(screen, (0, 0, 0), (286, 437, 30, 75), 1)

dr.ellipse(screen, (182, 86, 35), (50, 390, 35, 63))
dr.ellipse(screen, (0, 0, 0), (50, 390, 35, 63), 1)

# Голова
dr.ellipse(screen, (182, 86, 35), (30, 340, 107, 100))
dr.ellipse(screen, (0, 0, 0), (30, 340, 107, 100), 1)

# Левый глаз
b = -2
dr.ellipse(screen, (90, 135, 0), (50 + b, 377, 26, 32))
dr.ellipse(screen, (0, 0, 0), (50 + b, 377, 26, 32), 1)
dr.ellipse(screen, (0, 0, 0), (63 + b, 377, 5, 32))
dr.line(screen, ('white'), (53 + b, 385), (62 + b, 391), 5)

# Правый глаз
a = 45
dr.ellipse(screen, (90, 135, 0), (50 + a, 377, 26, 32))
dr.ellipse(screen, (0, 0, 0), (50 + a, 377, 26, 32), 1)
dr.ellipse(screen, (0, 0, 0), (63 + a, 377, 5, 32))
dr.line(screen, ('white'), (53 + a, 385), (62 + a, 391), 5)

# Носик
c = 7
d = 27
dr.polygon(screen, ('pink'), ((73 + c, 385 + d), (73 + c + 8, 385 + d), (73 + c + 4, 385 + d + 6)))
dr.polygon(screen, (0, 0, 0), ((73 + c - 1, 385 + d), (73 + c + 8 + 1, 385 + d), (73 + c + 4, 385 + d + 6)), width=1)
dr.ellipse(screen, (182, 86, 35), (87, 436, 73, 40))
dr.ellipse(screen, (0, 0, 0), (87, 436, 73, 40), 1)

# Мoрдочка
dr.line(screen, ('black'), (73 + c + 4, 385 + d + 6), (73 + c + 4, 385 + d + 6 + 8))
e = 12
dr.arc(screen, ('black'), (84 - e, 426 - e / 2, e, e), 7 * pi / 6, 0)
dr.arc(screen, ('black'), (84, 426 - e / 2, e, e), pi, 11 * pi / 6)

# Ушки
f = 70
g = 8
dr.polygon(screen, (182, 86, 35),
           ((30 + f - 2, 340 + g), (30 + f + 27 + 2, 340 + g - 16 - 2), (30 + f + 24, 340 + g + 15 + 2)))
dr.polygon(screen, (0, 0, 0),
           ((30 + f - 2, 340 + g), (30 + f + 27 + 2, 340 + g - 16 - 2), (30 + f + 24, 340 + g + 15 + 2)), 1)
dr.polygon(screen, ('pink'),
           ((30 + f + 3, 340 + g), (30 + f + 27 - 2, 340 + g - 16 + 3), (30 + f + 24 - 2 - 2, 340 + g + 15 - 3)))
dr.polygon(screen, (0, 0, 0), ((30 + f + 3 - 1, 340 + g), (30 + f + 27 - 2 + 1, 340 + g - 16 + 3 - 1),
                               (30 + f + 24 - 2 - 2 + 1, 340 + g + 15 - 3 + 1)), 1)

h = 30

dr.polygon(screen, (182, 86, 35),
           ((30 + f - 2 - h, 340 + g), (30 + f - 2 - 31 - h, 340 + g - 16 - 2), (30 + f - 28 - h, 340 + g + 15 + 2)))
dr.polygon(screen, (0, 0, 0),
           ((30 + f - 2 - h, 340 + g), (30 + f - 33 - h, 340 + g - 16 - 2), (30 + f - 28 - h, 340 + g + 15 + 2)), 1)
dr.polygon(screen, ('pink'), ((30 + f + 3 - 9 - h, 340 + g), (30 + f + 3 - 22 - 9 - h, 340 + g - 16 + 3),
                              (30 + f + 3 - 17 - 10 - h, 340 + g + 15 - 3)))
dr.polygon(screen, (0, 0, 0), ((30 + f + 3 - 1 - 8 - h, 340 + g), (30 + f + 2 - 24 - 8 - h, 340 + g - 16 + 3 - 1),
                               (30 + f + 2 - 19 - 8 - h, 340 + g + 15 - 3 + 1)), 1)

# Вибриссы
l = -160
m = 124
# Правая сторона
dr.arc(screen, ('black'), (200 + l, 300 + m, 120, 40), pi / 6, pi / 2)
dr.arc(screen, ('black'), (200 + l + 30, 300 + m - 5, 120, 40), pi / 6 + pi / 6, pi / 2 + pi / 6)
dr.arc(screen, ('black'), (200 + l + 51, 300 + m - 15, 120, 40), pi / 6 + 2 * pi / 6, pi / 2 + 2 * pi / 6)
# Левая сторона
n = 30
dr.arc(screen, ('black'), (200 + l - n, 300 + m, 120, 40), pi - pi / 2, pi - pi / 6)
dr.arc(screen, ('black'), (200 + l - n - 30, 300 + m - 5, 120, 40), pi - (pi / 2 + pi / 6), pi - (pi / 6 + pi / 6))
dr.arc(screen, ('black'), (200 + l - 51 - n, 300 + m - 15, 120, 40), pi - (pi / 2 + 2 * pi / 6),
       pi - (pi / 6 + 2 * pi / 6))

# Клубок
dr.circle(screen, ('grey'), (200, 530), 40)
dr.circle(screen, ('black'), (200, 530), 40, width=1)
dr.arc(screen, (0, 0, 0), (200, 530, 50, 50), pi / 2 + pi / 6, pi)
dr.arc(screen, (0, 0, 0), (190, 522, 60, 60), pi / 2 + pi / 6, pi)
dr.arc(screen, (0, 0, 0), (180, 515, 70, 70), pi / 2 + pi / 6, pi)
dr.arc(screen, (0, 0, 0), (153, 507, 70, 70), 0, pi / 2)
dr.arc(screen, (0, 0, 0), (150, 497, 80, 80), 0, pi / 2)

# Нитка
x = 180
y = 555
for i in range(0, 15, 1):
    dr.aaline(screen, 'gray', [x, y], [x - i, y + 3 * sin(i * pi / 5)])
    x -= i
    y += 3 * sin(i * pi / 5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
