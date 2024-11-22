import pygame

WHITH = 400
HEIGHT = 800
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
        self.image1 = pygame.image.load('./img/bird1.png')
        self.image2 = pygame.image.load('./img/bird2.png')
        self.image3 = pygame.image.load('./img/bird3.png')
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()

    def draw(self, screen):
        pass

    def update(self):
        self.rect1.y += 1


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./img/bg.png')
        self.rect = self.image.get_rect()

    def draw(self):
        pass


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=(WHITH, HEIGHT))
    pygame.display.set_caption('Bird')

    running = True
    while running:
        # прием и обработкa сообщений
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
