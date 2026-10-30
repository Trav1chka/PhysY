from enum import Enum, auto
import pygame

class ObjectType(Enum):
    Static = auto()
    Dynamic = auto()
    DynamicControllable = auto()


class BaseObject(pygame.sprite.Sprite):
    def __init__(
        self,
        name: str,
        pos: tuple[float, float],
        dima: tuple[float, float],
        object_type: ObjectType,
        color: tuple[int, int, int],
        acceleration: float = 300,
        jump_force: float = 100
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
        pass
