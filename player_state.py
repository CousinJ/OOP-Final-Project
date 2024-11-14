from abc import ABC, abstractmethod

class PlayerState(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def enter(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def exit(self):
        pass