from player_animator import PlayerAnimator
class Player():
    def __init__(self, w: int, h: int, win):
        self.w = w
        self.h = h
        self.pos = {"X": 600, "Y": 500}  # Set a default Y position
        self.win = win
        self.animator = PlayerAnimator()
    
    def draw(self):
        # Get the current frame from the animator and draw it
        current_frame = self.animator.get_current_frame()
        self.win.blit(current_frame, (self.pos["X"], self.pos["Y"]))