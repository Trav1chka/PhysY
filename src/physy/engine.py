from collections import deque

from physy.mod.base_object import BaseObject

class PhysEngine:
    def __init__(self) -> None:
        self.elements: deque[BaseObject] = deque([])
