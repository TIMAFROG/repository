import random

import pygame

WHITH = 400
HEIGHT = 700
FPS = 60

pygame.init()
screen = pygame.display.set_mode(size=(WHITH, HEIGHT))
pygame.display.set_caption('Bird')  # название
clock = pygame.time.Clock()

bg = pygame.image.load('./img/bg.png')
ground = pygame.image.load('./img/ground.png')
ground_x = 0


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, position=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./img/pipe.png')
        self.rect = self.image.get_rect()  # хитбокст картинки
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)  # переворот
            self.rect.bottomleft = [x, y - 75]  # на 75 вверх
        if position == 0:
            self.rect.bottomleft = [x, y + 75]  # на 75 вниз

    def update(self):
        self.rect.x -= 1  # сдвиг на 1 влево


class Bird(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        self.velocity = 0.1
        for num in range(1, 4):
            img = pygame.image.load(f'./img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.counter += 1
        self.bird_time = 5
        if self.counter > self.bird_time:
            self.counter = 0
            self.index += 1
            if self.index > 2:
                self.index = 0
        self.image = self.images[self.index]
        self.velocity += 0.2
        self.rect.y += self.velocity
        global game_over
        if self.rect.bottom > 600:
            self.velocity = 0
            self.rect.bottom = 600
            game_over = True
        if not game_over:
            if pygame.mouse.get_pressed()[0]:  # содержит список из 3 кнопок мыши
                if self.rect.top > 0:
                    self.velocity = -3


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

bird_group.add(Bird(90, HEIGHT//2))
last_pipe = pygame.time.get_ticks()
pipe_flew = 5000


game_over = False
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ground_x -= 1
    if ground_x <= -500:
        ground_x = 0

    screen.blit(bg, (0, 0))

    time_now = pygame.time.get_ticks()
    if pipe_flew < time_now - last_pipe:
        pipe_height = random.randint(-100, 250)
        top_pipe = Pipe(WHITH, HEIGHT//2+pipe_height+HEIGHT//2, 0)
        bot_pipe = Pipe(WHITH, HEIGHT//2+pipe_height-HEIGHT//2, 1)
        last_pipe = time_now
        pipe_group.add(top_pipe, bot_pipe)

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        game_over = True

    pipe_group.draw(screen)
    pipe_group.update()

    screen.blit(ground, (ground_x, 600))

    bird_group.draw(screen)
    bird_group.update()

    pygame.display.flip()

pygame.quit()
