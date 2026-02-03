import random  # CRITICAL: random.choice needs this
from abc import ABC, abstractmethod

class Player(ABC):
    """abstract class defining the player"""
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self) -> tuple:
        # 10. Get random move
        move = random.choice(self.moves)
        
        # 11. Update position attribute
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)
        
        # 12. Append new position to path
        self.path.append(self.position)
        
        # 13. Return updated position attribute
        return self.position
    
    @abstractmethod
    def level_up(self) -> None:
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self) -> None:
        self.moves += [(1, 1), (1, -1), (-1, -1), (-1, 1)]

# --- YOUR CODE ABOVE ---

# 1. Check if we can create a Pawn
p = Pawn()
print(f"Initial Position: {p.position}")
print(f"Initial Path: {p.path}")

# 2. Check if make_move works
# This should pick a random move from [(0, 1), (0, -1), (-1, 0), (1, 0)]
p.make_move()
print(f"\nAfter Move 1:")
print(f"New Position: {p.position}")
print(f"Path Length: {len(p.path)} (Should be 2)")
print(f"Current Path: {p.path}")

# 3. Check if level_up works
print(f"\nMoves before level_up: {len(p.moves)}")
p.level_up()
print(f"Moves after level_up: {len(p.moves)} (Should be 8)")

# 4. Final Position Check
p.make_move()
print(f"\nAfter Move 2:")
print(f"Final Position: {p.position}")
print(f"Final Path: {p.path}")
