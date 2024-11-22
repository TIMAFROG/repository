import pygame

WHITH = 400
HEIGHT = 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode(size=(WHITH, HEIGHT))
pygame.display.set_caption('Bird')  # название
clock = pygame.time.Clock()
