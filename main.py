import pygame
from player import Player
# Pygame Setup
pygame.init()

# Screen settings
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
FPS = 60
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("OOP Final Project")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock to control the game's framerate
clock = pygame.time.Clock()

# Game loop
def main():
    player = Player(50, 100, win)
    run = True

    while run:
        clock.tick(FPS)  # Control the framerate

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Update animation
        dt = clock.get_time()  # Get delta time (milliseconds)
        player.animator.update(dt)  # Update the player's animator

        # Draw the player
        win.fill(WHITE)  # Clear screen
        player.draw()  # Draw the player

        # Update the display
        pygame.display.flip()

    pygame.quit()

# Start the game
main()