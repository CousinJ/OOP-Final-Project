from player_state import PlayerState

class Slide(PlayerState):
    def __init__(self, player):
        self.player = player
        self.initial_velocity = 4
        self.multiplier = 1.5

    def enter(self):
        print("ENTER Slide")
        # Set sliding animation
        self.initial_velocity = abs(self.player.controller.player_velocity_x )* self.multiplier
        self.player.animator.current_animation = self.player.animator.slide_start
        # Set initial sliding speed based on direction
        
        self.player.controller.player_velocity_x = self.initial_velocity if self.player.controller.facing_right else -self.initial_velocity

    def update(self):
        # Debugging print to show current velocity
        print(f"Current Velocity: {self.player.controller.player_velocity_x}")

        # Apply friction to decrease velocity over time
        friction = 0.5
        if self.player.controller.player_velocity_x > 0:
            
            self.player.controller.player_velocity_x = max(0, self.player.controller.player_velocity_x - friction)
        elif self.player.controller.player_velocity_x < 0:
            self.player.controller.player_velocity_x = min(0, self.player.controller.player_velocity_x + friction)

        if abs(self.player.controller.player_velocity_x) < self.initial_velocity / 1.3:
            
            self.player.animator.current_animation = self.player.animator.sliding
        if abs(self.player.controller.player_velocity_x) < self.initial_velocity / 4:
            
            self.player.animator.current_animation = self.player.animator.slide_end

        # Transition to idle if the velocity is near zero
        if abs(self.player.controller.player_velocity_x) < 0.5:
            self.player.controller.is_sliding = False
            print("Transitioning to idle")
            self.player.state.switch_state(self.player.state.idle)

    def exit(self):
        print("EXIT Slide")
