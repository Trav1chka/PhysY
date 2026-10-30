from physy.mod.base_object import BaseObject as Object, ObjectType

import pygame


pygame.init()

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 800
screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock: pygame.Clock = pygame.time.Clock()
font: pygame.Font = pygame.font.Font(None, 24)
is_running: bool = True

FPS: int = 181

GRAVITY: float = 10.0
ACCELERATION: float = 300.0
JUMP_FORCE: float = -800.0






object1: Object = Object("Piska", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (100.0, 50.0), ObjectType.DynamicControllable, (115, 78, 9))

objects: list[Object] = []
objects.append(object1)

all_sprites: pygame.sprite.Group = pygame.sprite.Group()
all_sprites.add(object1)


while is_running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((30, 30, 30))

    for object in objects:
        pygame.draw.rect(screen, pygame.Color(*object.color, 255), object)

    dt = clock.tick(FPS) / 1000
    all_sprites.update(dt)


pygame.quit
