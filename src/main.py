import pygame
from enum import Enum, auto


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


class ObjectType(Enum):
    Static = auto()
    Dynamic = auto()
    DynamicControllable = auto()


class Object(pygame.sprite.Sprite):
    def __init__(
        self, 
        name: str, 
        pos: tuple[float, float], 
        dima: tuple[float, float], 
        object_type: ObjectType, 
        color: tuple[int, int, int],
        acceleration: float = ACCELERATION,
        jump_force: float = JUMP_FORCE
    ) -> None:
        super().__init__()
        self.name: str = name
        self.rect: pygame.Rect = pygame.Rect(*pos, *dima)
        self.object_type: ObjectType = object_type
        self.color: tuple[int, int, int] = color
        if object_type == ObjectType.DynamicControllable:
            self.acceleration: float = acceleration
            self.jump_force: float = jump_force
            self.speedx: float = 0.0
            self.speedy: float = 0.0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.speedx = 0
        self.speedy = 0

        if keys[pygame.K_a] and keys[pygame.K_w]:
            self.speedx = -self.acceleration*dt
            self.speedy = -self.acceleration*dt
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.speedx = -self.acceleration*dt
            self.speedy = self.acceleration*dt
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.speedx = self.acceleration*dt
            self.speedy = -self.acceleration*dt
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.speedx = self.acceleration*dt
            self.speedy = self.acceleration*dt
        elif keys[pygame.K_a]:
            self.speedx = -self.acceleration*dt
        elif keys[pygame.K_d]:
            self.speedx = self.acceleration*dt
        elif keys[pygame.K_w]:
            self.speedy = -self.acceleration*dt
        elif keys[pygame.K_s]:
            self.speedy = self.acceleration*dt

        print(self.speedx, self.speedy)

        self.rect.x += self.speedx
        self.rect.y += self.speedy


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