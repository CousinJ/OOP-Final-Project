from animation import Animation
import pygame
class PlayerAnimator():
    def __init__(self):
        self.frame_index = 0  # Start at the first frame
        self.idle = Animation("./ANIM/sPlayerIdle.png", 4, 50, 50)  # Assuming 4 frames in the idle animation
        self.last_update = pygame.time.get_ticks()  # Track the last time the frame changed
        self.frame_duration = 100  # Time per frame (in milliseconds)

    def update(self, dt):
        # Update the frame based on the time passed (animation speed)
        if pygame.time.get_ticks() - self.last_update > self.frame_duration:
            self.frame_index = (self.frame_index + 1) % self.idle.frame_count  # Loop through frames
            self.last_update = pygame.time.get_ticks()  # Update last change time

    def get_current_frame(self):
        # Return the current frame of the idle animation
        return self.idle.get_frame(self.frame_index)