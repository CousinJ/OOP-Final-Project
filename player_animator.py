import pygame
from animation import Animation
class PlayerAnimator():
    def __init__(self, player):
        self.player = player
        self.frame_index = 0  # Start at the first frame
        
        # Load animations
        self.idle = Animation("./ANIM/sPlayerIdle.png", 4, 50, 50,self.player.scale_factor)
        self.run = Animation("./ANIM/sPlayerRun.png", 10, 50, 50,self.player.scale_factor)
        self.dash = Animation("./ANIM/sPlayerDash.png", 3, 50, 50,self.player.scale_factor)
        # Jumping animations
        self.jump_down = Animation("./ANIM/JUMP/sPlayerJumpDown.png", 4, 50, 50,self.player.scale_factor)
        self.jump_land = Animation("./ANIM/JUMP/sPlayerJumpLand.png", 3, 50, 50,self.player.scale_factor)
        self.jump_up = Animation("./ANIM/JUMP/sPlayerJumpUp.png", 3, 50, 50,self.player.scale_factor)
        # Sliding animations
        self.sliding = Animation("./ANIM/SLIDE/sPlayerSlide.png", 2, 50, 50,self.player.scale_factor)
        self.slide_end = Animation("./ANIM/SLIDE/sPlayerSlideEnd.png", 2, 50, 50,self.player.scale_factor)
        self.slide_start = Animation("./ANIM/SLIDE/sPlayerSlideStart.png", 2, 50, 50,self.player.scale_factor)
        
        self.current_animation = self.idle
        self.last_update = pygame.time.get_ticks()  # Track the last time the frame changed
        self.frame_duration = 100  # Time per frame in milliseconds (adjust for smoother animation)

    def update(self):
        # Check if enough time has passed to update to the next frame
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            # Move to the next frame and loop back if at the end
            self.frame_index = (self.frame_index + 1) % self.current_animation.frame_count
            self.last_update = now  # Reset the last update time

    def get_current_frame(self):
        # Determine which direction to face based on the controller's facing_right attribute
        flipped = not self.player.controller.facing_right
        return self.current_animation.get_frame(self.frame_index, flipped)

    
   
