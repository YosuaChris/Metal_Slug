import pygame

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Metal Slug")


x = 200
y = 200
img = pygame.image.load('img/player/idle/0.png')


run = True
while run:
    for event in pygame.event.get():
        # quit Game
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
