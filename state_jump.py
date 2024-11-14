from player_state import PlayerState

class Jump(PlayerState):
    def enter(self):
        print("ENTER Jump")
        self.player.animator.current_animation = self.player.animator.jump_up
        self.player.animator.frame_index = 0  # Start from the first frame of jump_up

    def update(self):
        if self.player.controller.is_grounded:
            self.player.state.switch_state(self.player.state.idle)
        # Set the correct animation based on vertical velocity
        if self.player.controller.player_velocity_y < 0:  # Going up
            if self.player.animator.current_animation != self.player.animator.jump_up:
                self.player.animator.current_animation = self.player.animator.jump_up
                self.player.animator.frame_index = 0  # Reset to first frame of jump_up

        elif self.player.controller.player_velocity_y > 0:  # Going down
            if self.player.animator.current_animation != self.player.animator.jump_down:
                self.player.animator.current_animation = self.player.animator.jump_down
                self.player.animator.frame_index = 0  # Reset to first frame of jump_down

        else:  # Landing or almost on the ground
            if self.player.controller.is_grounded:  # Assume this checks if the player has landed
                if self.player.animator.current_animation != self.player.animator.jump_land:
                    self.player.animator.current_animation = self.player.animator.jump_land
                    self.player.animator.frame_index = 0  # Reset to first frame of jump_land

        

    def exit(self):
        print("EXIT Jump")
