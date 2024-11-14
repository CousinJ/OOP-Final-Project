import pygame 

class PlayerController:
    def __init__(self, player):
        self.player = player
        self.is_grounded = True
        self.is_sliding = False  # Track if the player is sliding
        
        self.player_velocity_x = 0
        self.player_velocity_y = 0
        self.player_acceleration = 0.5
        self.jump_force = -20
        self.gravity = 0.8
        self.drag = 0.9
        self.max_speed_x = 10
        self.max_fall_speed = 20
        self.facing_right = True

    def update(self):
        keys = pygame.key.get_pressed()

        # Check for sliding
        if keys[pygame.K_s] and self.is_grounded and not self.is_sliding:
            self.slide()

        # If not sliding, handle horizontal movement
        if not self.is_sliding:
            if keys[pygame.K_LEFT]:
                self.run(-1)
                self.facing_right = False
            elif keys[pygame.K_RIGHT]:
                self.run(1)
                self.facing_right = True
            else:
                # Apply drag if no horizontal movement key is pressed
                self.player_velocity_x *= self.drag
                if abs(self.player_velocity_x) < 0.1:
                    self.player_velocity_x = 0

        # Jumping
        if keys[pygame.K_SPACE] and self.is_grounded:
            self.jump()
        

        # Apply gravity if in the air
        self.apply_gravity()

        # Update the player's position
        self.player.pos["X"] += self.player_velocity_x
        self.player.pos["Y"] += self.player_velocity_y

        # Check if grounded (for example, at ground level Y=500)
        if self.player.pos["Y"] >= 500:
            self.player.pos["Y"] = 500
            self.is_grounded = True
            self.player_velocity_y = 0
        else:
            self.is_grounded = False

    def apply_gravity(self):
        if not self.is_grounded:
            self.player_velocity_y += self.gravity
            if self.player_velocity_y > self.max_fall_speed:
                self.player_velocity_y = self.max_fall_speed

    def jump(self):
        if not self.is_sliding:
            self.player_velocity_y = self.jump_force
            self.is_grounded = False
            self.is_sliding = False  # Disable sliding when jumping

    def run(self, direction):
        if not self.is_sliding:  # Prevent running while sliding
            self.player_velocity_x += direction * self.player_acceleration
            if abs(self.player_velocity_x) > self.max_speed_x:
                self.player_velocity_x = self.max_speed_x * direction

    def slide(self):
        # Start sliding: prevent any transition back to run while sliding
        if not self.is_sliding and abs(self.player_velocity_x) > 5:
            self.is_sliding = True
            self.player.state.switch_state(self.player.state.slide)  # Switch to Slide state

        
