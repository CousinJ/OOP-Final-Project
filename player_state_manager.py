from player_state import PlayerState

from state_idle import Idle
from state_jump import Jump
from state_run import Run
from state_slide import Slide


class PlayerStateManager():
    def __init__(self, player):
        self.player = player
        #concrete player states
        self.idle = Idle(player)
        self.jump = Jump(player)
        self.run = Run(player)
        self.slide = Slide(player)


        self.current_state = self.idle


    def switch_state(self, newState: PlayerState):
        if newState != self.current_state:
            self.current_state.exit()
            self.current_state = newState
            self.current_state.enter()


    def update_state(self):
        #calling the concrete override update method
        self.current_state.update()
