import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

dr.circle(screen, (255, 255, 0), (200, 200), 75)
dr.circle(screen, (255, 0, 0), (170,175), 15)
dr.circle(screen, (255, 0, 0), (230,175), 10)
dr.circle(screen, (0, 0, 0), (170,175), 7)
dr.circle(screen, (0, 0, 0), (230,175), 6)
dr.rect(screen, (0, 0 , 0), (180, 240, 50, 10), 0)
# dr.polygon(screen, (0, 0, 0), [(160,140), (160,140)], 0)
dr.line(screen, (0, 0, 0), (160,150), (190,175), 6)
dr.line(screen, (0, 0, 0), (250, 150), (220, 167), 6)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()