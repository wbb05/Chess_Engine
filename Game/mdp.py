# Abstract class for a Markov Decision Process
# Need states, possible actions, resulting state from actions, reward of taking action from s to s'

class MDP:
    def __init__(self, startState):
        self.state = startState

    def getState(self):
        # Returns current state
        pass

    def getActions(self, state):
        # Returns possible actions based on state
        pass

    def getResultingState(self, state, action):
        # Returns tuple (newState, probability of transition)
        pass

    def reward(self, state, action, statePrime):
        # Returns reward of taking action from state to statePrime
        pass

    def isTerminal(self, state):
        # Returns true if state is a terminal state
        pass

