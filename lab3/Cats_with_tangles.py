import pygame
import pygame.draw as dr
from numpy import pi, sin

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

# Фон
dr.rect(screen, (66, 64, 0), (0, 0, 400, 300))
dr.rect(screen, (125, 102, 6), (0, 300, 400, 300))


def draw_window(x0, y0, n):
    # Окно
    dr.rect(screen, (240, 240, 255), (x0, y0, 180 / n, 270 / n))
    dr.rect(screen, (78, 195, 226), (x0 + 10 / n, y0 + 10 / n, 75 / n, 75 / n))
    dr.rect(screen, (78, 195, 226), (x0 + 95 / n, y0 + 10 / n, 75 / n, 75 / n))
    dr.rect(screen, (78, 195, 226), (x0 + 10 / n, y0 + 95 / n, 75 / n, 165 / n))
    dr.rect(screen, (78, 195, 226), (x0 + 95 / n, y0 + 95 / n, 75 / n, 165 / n))


def draw_cat(x0, y0, n, coat_color, eye_color, mirror):
    if not mirror:
        # Хвост - Tail
        x_up_tail = 0
        y_up_tail = 30
        dr.arc(screen, coat_color, (x0 + x_up_tail / n, y0 + y_up_tail / n, 400 / n, 160 / n), 0, pi / 2,
               width=int(50 / n))
        dr.arc(screen, coat_color, (x0 + x_up_tail / n, y0 + y_up_tail / n + 1, 400 / n, 160 / n), 0, pi / 2,
               width=int(62 / n))
        x_down_tail = 200
        y_down_tail = -45
        dr.arc(screen, coat_color, (x0 + x_down_tail / n, y0 + y_down_tail / n, 400 / n, 160 / n), pi / 6 + pi,
               pi + pi / 2, width=int(16 / n))
        dr.arc(screen, coat_color, (x0 + x_down_tail / n, y0 + y_down_tail / n - 1, 400 / n, 160 / n), pi / 6 + pi,
               pi + pi / 2, width=int(16 / n))
        dr.arc(screen, 'black', (x0 + x_up_tail / n, y0 + y_up_tail / n, 400 / n, 160 / n), - pi / 42, pi / 2, width=1)
        dr.arc(screen, 'black', (x0 + x_down_tail / n, y0 + y_down_tail / n, 400 / n, 160 / n), pi / 6 + pi,
               pi + pi / 2, width=1)

        # Тело
        dr.ellipse(screen, coat_color, (x0, y0, 266 / n, 130 / n), 0)
        dr.ellipse(screen, (0, 0, 0), (x0, y0, 266 / n, 130 / n), 1)

        # Координаты частей кота даются в координатах относительно x0 и y0
        # Бедро - Hip
        x_hip = 215
        y_hip = 94
        dr.circle(screen, coat_color, (x0 + x_hip / n, y0 + y_hip / n), 45 / n)
        dr.circle(screen, (0, 0, 0), (x0 + x_hip / n, y0 + y_hip / n), 45 / n, 1)

        # Задняя лапка - BackFoot
        x_back_foot = 236
        y_back_foot = 107
        dr.ellipse(screen, coat_color, (x0 + x_back_foot / n, y0 + y_back_foot / n, 30 / n, 75 / n))
        dr.ellipse(screen, (0, 0, 0), (x0 + x_back_foot / n, y0 + y_back_foot / n, 30 / n, 75 / n), 1)

        # Передние лапки - FrontFoot
        x_right_front_foot = 0
        y_right_front_foot = 60
        dr.ellipse(screen, coat_color, (x0 + x_right_front_foot / n, y0 + y_right_front_foot / n, 35 / n, 63 / n))
        dr.ellipse(screen, (0, 0, 0), (x0 + x_right_front_foot / n, y0 + y_right_front_foot / n, 35 / n, 63 / n), 1)
        x_left_front_foot = 37
        y_left_front_foot = 106
        dr.ellipse(screen, coat_color, (x0 + x_left_front_foot / n, y0 + y_left_front_foot / n, 73 / n, 40 / n))
        dr.ellipse(screen, (0, 0, 0), (x0 + x_left_front_foot / n, y0 + y_left_front_foot / n, 73 / n, 40 / n), 1)
    else:
        # Третья точка носа - относительно неё будет произведено отражнение кота
        x = x0 + 34
        # Хвост - Tail
        x_up_tail = 0
        y_up_tail = 30
        dr.arc(screen, coat_color, (2 * x - (x0 + x_up_tail / n) - 400 / n, y0 + y_up_tail / n, 400 / n, 160 / n),
               pi / 2, pi,
               width=int(50 / n))
        dr.arc(screen, coat_color, (2 * x - (x0 + x_up_tail / n) - 400 / n, y0 + y_up_tail / n + 1, 400 / n, 160 / n),
               pi / 2, pi,
               width=int(62 / n))
        x_down_tail = 200
        y_down_tail = -45
        dr.arc(screen, coat_color, (2 * x - (x0 + x_down_tail / n) - 400 / n, y0 + y_down_tail / n, 400 / n, 160 / n),
               pi + pi / 2,
               2 * pi - pi / 6, width=int(16 / n))
        dr.arc(screen, coat_color,
               (2 * x - (x0 + x_down_tail / n) - 400 / n, y0 + y_down_tail / n - 1, 400 / n, 160 / n), pi + pi / 2,
               2 * pi - pi / 6, width=int(17 / n))
        dr.arc(screen, 'black', (2 * x - (x0 + x_up_tail / n) - 400 / n - 2, y0 + y_up_tail / n, 400 / n, 160 / n),
               pi / 2,
               pi + pi / 42, width=1)
        dr.arc(screen, 'black', (2 * x - (x0 + x_down_tail / n) - 400 / n, y0 + y_down_tail / n, 400 / n, 160 / n),
               pi + pi / 2,
               2 * pi - pi / 6, width=1)

        # Тело
        dr.ellipse(screen, coat_color, (2 * x - x0 - 266 / n, y0, 266 / n, 130 / n), 0)
        dr.ellipse(screen, (0, 0, 0), (2 * x - x0 - 266 / n, y0, 266 / n, 130 / n), 1)

        # Координаты частей кота даются в координатах относительно x0 и y0
        # Бедро - Hip
        x_hip = 215
        y_hip = 94
        dr.circle(screen, coat_color, (2 * x - (x0 + x_hip / n), y0 + y_hip / n), 45 / n)
        dr.circle(screen, (0, 0, 0), (2 * x - (x0 + x_hip / n), y0 + y_hip / n), 45 / n, 1)

        # Задняя лапка - BackFoot
        x_back_foot = 236
        y_back_foot = 107
        dr.ellipse(screen, coat_color, (2 * x - (x0 + x_back_foot / n) - 30 / n, y0 + y_back_foot / n, 30 / n, 75 / n))
        dr.ellipse(screen, (0, 0, 0), (2 * x - (x0 + x_back_foot / n) - 30 / n, y0 + y_back_foot / n, 30 / n, 75 / n),
                   1)

        # Передние лапки - FrontFoot
        x_right_front_foot = 0
        y_right_front_foot = 60
        dr.ellipse(screen, coat_color,
                   (2 * x - (x0 + x_right_front_foot / n) - 35 / n, y0 + y_right_front_foot / n, 35 / n, 63 / n))
        dr.ellipse(screen, (0, 0, 0),
                   (2 * x - (x0 + x_right_front_foot / n) - 35 / n, y0 + y_right_front_foot / n, 35 / n, 63 / n), 1)
        x_left_front_foot = 37
        y_left_front_foot = 106
        dr.ellipse(screen, coat_color,
                   (2 * x - (x0 + x_left_front_foot / n) - 73 / n, y0 + y_left_front_foot / n, 73 / n, 40 / n))
        dr.ellipse(screen, (0, 0, 0),
                   (2 * x - (x0 + x_left_front_foot / n) - 73 / n, y0 + y_left_front_foot / n, 73 / n, 40 / n), 1)
        x0 += 34 * (2  - 2/n)

    # Голова - Head
    x_head = -20
    y_head = 10
    dr.ellipse(screen, coat_color, (x0 + x_head / n, y0 + y_head / n, 107 / n, 100 / n))
    dr.ellipse(screen, (0, 0, 0), (x0 + x_head / n, y0 + y_head / n, 107 / n, 100 / n), 1)

    # Левый глаз - LeftEye
    x_left_eye = -2
    y_left_eye = 47
    dr.ellipse(screen, eye_color, (x0 + x_left_eye / n, y0 + y_left_eye / n, 26 / n, 32 / n))
    dr.ellipse(screen, (0, 0, 0), (x0 + x_left_eye / n, y0 + y_left_eye / n, 26 / n, 32 / n), 1)
    x_left_pupil = 11
    y_left_pupil = 47
    dr.ellipse(screen, (0, 0, 0), (x0 + x_left_pupil / n, y0 + y_left_pupil / n, 5 / n, 32 / n))
    x_left_glimmer = 10
    y_left_glimmer = 61
    dr.line(screen, 'white', (x0 + (x_left_glimmer - 9) / n, y0 + (y_left_glimmer - 6) / n),
            (x0 + x_left_glimmer / n, y0 + y_left_glimmer / n), int(5 / n))

    # Правый глаз - RightEye
    a = 45
    x_left_eye = -2
    y_left_eye = 47
    dr.ellipse(screen, eye_color, (x0 + (x_left_eye + a) / n, y0 + y_left_eye / n, 26 / n, 32 / n))
    dr.ellipse(screen, (0, 0, 0), (x0 + (x_left_eye + a) / n, y0 + y_left_eye / n, 26 / n, 32 / n), 1)
    x_left_pupil = 11
    y_left_pupil = 47
    dr.ellipse(screen, (0, 0, 0), (x0 + (x_left_pupil + a) / n, y0 + y_left_pupil / n, 5 / n, 32 / n))
    x_left_glimmer = 10
    y_left_glimmer = 61
    dr.line(screen, 'white', (x0 + (x_left_glimmer - 9 + a) / n, y0 + (y_left_glimmer - 6) / n),
            (x0 + (x_left_glimmer + a) / n, y0 + y_left_glimmer / n), int(5 / n))

    # Носик - Nose
    x_nose1 = 30
    y_nose1 = 82
    x_nose2 = 38
    y_nose2 = 82
    x_nose3 = 34
    y_nose3 = 86
    dr.polygon(screen, 'pink', (
        (x0 + x_nose1 / n, y0 + y_nose1 / n), (x0 + x_nose2 / n, y0 + y_nose2 / n),
        (x0 + x_nose3 / n, y0 + y_nose3 / n)))
    dr.polygon(screen, (0, 0, 0), (
        (x0 + (x_nose1 - 1) / n, y0 + y_nose1 / n), (x0 + (x_nose2 + 1) / n, y0 + y_nose2 / n),
        (x0 + x_nose3 / n, y0 + y_nose3 / n)), width=1)

    # Мoрдочка - Muzzle
    dr.line(screen, 'black', (x0 + x_nose3 / n, y0 + y_nose3 / n), (x0 + x_nose3 / n, y0 + (y_nose3 + 8) / n))
    x_muzzle = 22
    y_muzzle = 90
    dr.arc(screen, 'black', (x0 + x_muzzle / n, y0 + y_muzzle / n, 12 / n, 12 / n), 7 * pi / 6, 0)
    dr.arc(screen, 'black', (x0 + (x_muzzle + 12) / n, y0 + y_muzzle / n, 12 / n, 12 / n), pi, 11 * pi / 6)

    # Ушки - Ears
    x_ear1 = 48
    y_ear1 = 18
    x_ear2 = 79
    y_ear2 = 0
    x_ear3 = 74
    y_ear3 = 35
    dr.polygon(screen, coat_color,
               ((x0 + x_ear1 / n, y0 + y_ear1 / n), (x0 + x_ear2 / n, y0 + y_ear2 / n),
                (x0 + x_ear3 / n, y0 + y_ear3 / n)))
    dr.polygon(screen, (0, 0, 0),
               ((x0 + x_ear1 / n, y0 + y_ear1 / n), (x0 + x_ear2 / n, y0 + y_ear2 / n),
                (x0 + x_ear3 / n, y0 + y_ear3 / n)), 1)
    dr.polygon(screen, 'pink',
               ((x0 + (x_ear1 + 5) / n, y0 + y_ear1 / n), (x0 + (x_ear2 - 4) / n, y0 + (y_ear2 + 5) / n),
                (x0 + (x_ear3 - 4) / n, y0 + (y_ear3 - 5) / n)))
    dr.polygon(screen, (0, 0, 0), (
        (x0 + (x_ear1 + 4) / n, y0 + y_ear1 / n), (x0 + (x_ear2 - 3) / n, y0 + (y_ear2 + 4) / n),
        (x0 + (x_ear3 - 3) / n, y0 + (y_ear3 - 4) / n)), 1)

    h = 30
    dr.polygon(screen, coat_color,
               ((x0 + (x_ear1 - h) / n, y0 + y_ear1 / n), (x0 + (x_ear2 - 62 - h) / n, y0 + y_ear2 / n),
                (x0 + (x_ear3 - 52 - h) / n, y0 + y_ear3 / n)))
    dr.polygon(screen, (0, 0, 0),
               ((x0 + (x_ear1 - h) / n, y0 + y_ear1 / n), (x0 + (x_ear2 - 62 - h - 1) / n, y0 + y_ear2 / n),
                (x0 + (x_ear3 - 52 - h) / n, y0 + y_ear3 / n)), 1)
    dr.polygon(screen, 'pink',
               ((x0 + (x_ear1 - 4 - h) / n, y0 + y_ear1 / n), (x0 + (x_ear2 - 58 - h) / n, y0 + (y_ear2 + 5) / n),
                (x0 + (x_ear3 - 48 - h) / n, y0 + (y_ear3 - 5) / n)))
    dr.polygon(screen, (0, 0, 0),
               ((x0 + (x_ear1 - 4 - h) / n, y0 + y_ear1 / n), (x0 + (x_ear2 - 59 - h) / n, y0 + (y_ear2 + 4) / n),
                (x0 + (x_ear3 - 49 - h) / n, y0 + (y_ear3 - 4) / n)), 1)

    # Вибриссы - Vibrissae
    x_vibrissae1 = -10
    y_vibrissae1 = 94
    x_vibrissae2 = 20
    y_vibrissae2 = 89
    x_vibrissae3 = 41
    y_vibrissae3 = 79
    # Правая сторона
    dr.arc(screen, 'black', (x0 + x_vibrissae1 / n, y0 + y_vibrissae1 / n, 120 / n, 40 / n), pi / 6, pi / 2)
    dr.arc(screen, 'black', (x0 + x_vibrissae2 / n, y0 + y_vibrissae2 / n, 120 / n, 40 / n), pi / 6 + pi / 6,
           pi / 2 + pi / 6)
    dr.arc(screen, 'black', (x0 + x_vibrissae3 / n, y0 + y_vibrissae3 / n, 120 / n, 40 / n), pi / 6 + 2 * pi / 6,
           pi / 2 + 2 * pi / 6)
    # Левая сторона
    z = 30
    dr.arc(screen, 'black', (x0 + (x_vibrissae1 - z) / n, y0 + y_vibrissae1 / n, 120 / n, 40 / n), pi - pi / 2,
           pi - pi / 6)
    dr.arc(screen, 'black', (x0 + (x_vibrissae2 - z - 60) / n, y0 + y_vibrissae2 / n, 120 / n, 40 / n),
           pi - (pi / 2 + pi / 6), pi - (pi / 6 + pi / 6))
    dr.arc(screen, 'black', (x0 + (x_vibrissae3 - z - 102) / n, y0 + y_vibrissae3 / n, 120 / n, 40 / n),
           pi - (pi / 2 + 2 * pi / 6),
           pi - (pi / 6 + 2 * pi / 6))


def draw_tangle_with_thread(x0, y0, n, mirror):
    # Клубок - Tangle
    dr.circle(screen, 'grey', (x0, y0), 40 / n)
    dr.circle(screen, 'black', (x0, y0), 40 / n, width=1)
    dr.arc(screen, (0, 0, 0), (x0, y0, 50 / n, 50 / n), pi / 2 + pi / 6, pi)
    dr.arc(screen, (0, 0, 0), (x0 - 10 / n, y0 - 8 / n, 60 / n, 60 / n), pi / 2 + pi / 6, pi)
    dr.arc(screen, (0, 0, 0), (x0 - 20 / n, y0 - 15 / n, 70 / n, 70 / n), pi / 2 + pi / 6, pi)
    dr.arc(screen, (0, 0, 0), (x0 - 47 / n, y0 - 23 / n, 70 / n, 70 / n), 0, pi / 2)
    dr.arc(screen, (0, 0, 0), (x0 - 50 / n, y0 - 33 / n, 80 / n, 80 / n), 0, pi / 2)

    # Нитка - Thread
    if not mirror:
        x_thread = x0 - 20 / n
        y_thread = y0 + 25 / n
        for i in range(0, int(18 / n), 1):
            dr.aaline(screen, 'gray', [x_thread, y_thread], [x_thread - i, y_thread + 3 * sin(i * pi / 5)])
            x_thread -= i
            y_thread += 3 * sin(i * pi / 5)
    else:
        x_thread = x0 + 20 / n
        y_thread = y0 + 25 / n
        for i in range(0, int(18 / n), 1):
            dr.aaline(screen, 'gray', [x_thread, y_thread], [x_thread + i, y_thread + 3 * sin(i * pi / 5)])
            x_thread += i
            y_thread += 3 * sin(i * pi / 5)


draw_window(250, 20, 1.5)
draw_window(200, 20, 1.5)
draw_window(50, 20, 1.5)

draw_cat(180, 280, 2, (182, 86, 35), (90, 135, 0), False)
draw_cat(100, 370, 2, (181, 181, 181), (71, 255, 255), True)
draw_cat(50, 310, 4, (182, 86, 35), (90, 135, 0), False)
draw_cat(250, 450, 4, (182, 86, 35), (90, 135, 0), True)
draw_cat(140, 480, 4, (182, 86, 35), (90, 135, 0), False)
draw_cat(60, 550, 4, (181, 181, 181), (71, 255, 255), True)
draw_cat(300, 530, 4, (181, 181, 181), (71, 255, 255), False)

draw_tangle_with_thread(340, 500, 2, True)
draw_tangle_with_thread(250, 550, 1.5, False)
draw_tangle_with_thread(100, 510, 2.5, True)
draw_tangle_with_thread(340, 400, 1, False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
