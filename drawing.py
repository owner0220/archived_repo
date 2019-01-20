import pygame , sys
from pygame.locals import *

width, height = 500, 500
radius = 20
mouseX, mouseY = 0, 0

pygame.init()
window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255, 255, 255))

fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                window.fill(pygame.Color(255, 255, 255))
        mouseX,mouseY = pygame.mouse.get_pos()
        b = pygame.mouse.get_pressed()
        if b[0] == 1:
            pygame.draw.circle(window, pygame.Color(255, 0, 0), (mouseX, mouseY), radius, 0)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(30)

    