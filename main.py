import pygame

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Metal Slug")


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/img/player/idle/0.png')
        self.image = pygame.transform.scale(
            img, (int(img.get_width() * scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)


player = Soldier(200, 200, 3)
x = 200
y = 200
scale = 3

run = True
while run:
    player.draw()
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
