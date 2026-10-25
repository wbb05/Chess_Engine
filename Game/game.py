# Rules for game of chess
# Inherits from MDP
from mdp import MDP
from state import GameState
import json

class Game(MDP):
    def __init__(self):
        self.state = GameState()

        # Load tables from JSON file
        with open("non_sliding_tables.json", 'r') as file:
            self.non_sliding_tables = json.load(file)

    # MDP method
    def getState(self): # type: ignore
        return self.state

    # MDP method
    def getActions(self, state: GameState):
        # Determine player
        # Calculate moves
        pass


    # Rules for moving
    # Non-sliding pieces: Lookup tables
    # TODO: Put in seperate file?
    def white_pawn_moves(self, state: GameState):
        pass