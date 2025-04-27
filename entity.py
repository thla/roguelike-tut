from typing import Tuple

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int,int,int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
  
    def move(self, dx: int, dy: int):
        """
        Move the entity by dx and dy.
        """
        self.x += dx
        self.y += dy
        # Ensure the entity stays within the bounds of the map
        if self.x < 0:
            self.x = 0
        elif self.x >= 80:
            self.x = 79
        if self.y < 0:
            self.y = 0
        elif self.y >= 50:
            self.y = 49
    