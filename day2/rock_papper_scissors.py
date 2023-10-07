from dataclasses import dataclass
from typing import ClassVar

"""
My plays:
    Rock        -> X
    Papper      -> Y
    Scissors    -> Z

Their plays:
    Rock        -> A
    Papper      -> B
    Scissors    -> C
    
Second Part
    X -> Lose
    Y -> Draw
    Z -> Win
"""

@dataclass
class Shape:
    
    SHAPE_POINTS: ClassVar[dict] = {"Rock": 1, "Papper": 2, "Scissors": 3}
    ROUND_POINT: ClassVar[dict] = {"W": 6, "D": 3, "L": 0}
    
    # Part one
    MAPPER: ClassVar[dict] = {"A": "Rock", "B": "Papper", "C": "Scissors", "X": "Rock", "Y": "Papper", "Z": "Scissors"}
    
    # Part two
    I_WIN_MAPPER: ClassVar[dict] = {"A": "Y", "B": "Z", "C": "X"}
    I_LOSE_MAPPER: ClassVar[dict] = {"A": "Z", "B": "X", "C": "Y"}
    DRAW_MAPPER: ClassVar[dict] = {"A": "X", "B": "Y", "C": "Z"}
    DECISION_MAPPER: ClassVar[dict] = {"Z": I_WIN_MAPPER, "Y": DRAW_MAPPER, "X": I_LOSE_MAPPER}
    
    shape: str
    
    def __and__(self, other):
        
        my_play = Shape.MAPPER[other.shape]
        his_play = Shape.MAPPER[self.shape]
        
        sum = Shape.SHAPE_POINTS[Shape.MAPPER[other.shape]]
        
        if my_play == his_play:
            sum += Shape.ROUND_POINT["D"]
        elif (his_play, my_play) in [("Rock", "Scissors"), ("Papper", "Rock"), ("Scissors", "Papper")]:
            sum += Shape.ROUND_POINT["L"]
        else:
            sum += Shape.ROUND_POINT["W"]
        return sum
    
    @staticmethod
    def part_two(him, result):

        return Shape(him) & Shape(Shape.DECISION_MAPPER[result][him])
            

with open("day2/data.txt") as f:
    
    lines = f.readlines()
    total_score = sum([Shape(line[0]) & Shape(line[2]) for line in lines])
    
    # part one
    print("1:", total_score)
    
    # part two
    total_score = sum([Shape.part_two(line[0], line[2]) for line in lines])
    print("2:", total_score)
    
    