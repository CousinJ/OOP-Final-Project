from player_state import PlayerState

class Run(PlayerState):

    def enter(self):
        print("ENTER Run")

    def update(self):
        if not self.player.controller.is_grounded:
            self.player.state.switch_state(self.player.state.jump)
        self.player.animator.current_animation = self.player.animator.run

        if abs(self.player.controller.player_velocity_x)  < .5 and self.player.controller.is_grounded and not self.player.controller.is_sliding:
            self.player.state.switch_state(self.player.state.idle)
        print("run")

    def exit(self):
        print("EXIT Run")