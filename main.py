import pygame
pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Metal Slug")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# player action var
moving_left = False
moving_right = False

# define colours
BG = (144, 201, 120)


def draw_bg():
    screen.fill(BG)


class Soldier(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'assets/img/{self.char_type}/idle/0.png')
        self.image = pygame.transform.scale(
            img, (int(img.get_width() * scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0

        if moving_left:
            dx = - self.speed
            self.flip = True
            self.direction = - 1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # update rect positition
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rect)


player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 200, 3, 5)


x = 200
y = 200
scale = 3

run = True
while run:

    clock.tick(FPS)
    draw_bg()

    player.draw()
    enemy.draw()

    player.move(moving_left, moving_right)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False

        # keyboard bttn released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    pygame.display.update()
pygame.quit()
