import random

class Dice:
    def roll(self):
        low,high=1,6
        first=random.randint(low,high)
        second=random.randint(low,high)
        return first, second
    
p=Dice()
print(p.roll())