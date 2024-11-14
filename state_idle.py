from player_state import PlayerState

class Idle(PlayerState):

    def enter(self):
        print("ENTER IDLE")

    def update(self):
        self.player.animator.current_animation = self.player.animator.idle
        if not self.player.controller.is_grounded:
            self.player.state.switch_state(self.player.state.jump)
        elif abs(self.player.controller.player_velocity_x)  > .5 and self.player.controller.is_grounded and not self.player.controller.is_sliding:
            self.player.state.switch_state(self.player.state.run)
        elif self.player.controller.is_sliding:
            self.player.state.switch_state(self.player.state.slide)
        print("idle")

    def exit(self):
        print("EXIT IDLE")