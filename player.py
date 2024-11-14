from player_animator import PlayerAnimator
from player_controller import PlayerController
from player_state_manager import PlayerStateManager

class Player():
    def __init__(self, w: int, h: int, win, scale_factor=1):
        
        self.w = w
        self.h = h
        self.pos = {"X": 600, "Y": 500}  # Set a default Y position
        self.win = win
        self.scale_factor = scale_factor

        self.animator = PlayerAnimator(self)
        self.controller = PlayerController(self)
        self.state = PlayerStateManager(self)
    
    def draw(self):
        # Get the current frame from the animator and draw it
        current_frame = self.animator.get_current_frame()
        self.win.blit(current_frame, (self.pos["X"], self.pos["Y"]))