# Abstract class for a Markov Decision Process
# Need states, possible actions, resulting state from actions, reward of taking action from s to s'
from abc import ABC, abstractmethod

class MDP(ABC):

    @abstractmethod
    def getState(self):
        # Returns current state
        pass

    @abstractmethod
    def getActions(self, state):
        # Returns possible actions based on state
        pass

    @abstractmethod
    def getResultingState(self, state, action):
        # Returns tuple (newState, probability of transition)
        pass

    @abstractmethod
    def reward(self, state, action, statePrime):
        # Returns reward of taking action from state to statePrime
        pass

    @abstractmethod
    def isTerminal(self, state):
        # Returns true if state is a terminal state
        pass

