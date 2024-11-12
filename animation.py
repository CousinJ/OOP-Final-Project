import pygame

class Animation:
    def __init__(self, sprite_sheet_path: str, frame_count: int, frame_width: int, frame_height: int, scale_factor=1):
        # Load the sprite sheet and initialize properties
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.frame_count = frame_count
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frames = []  # Store original frames
        self.reflected_frames = []  # Store reflected frames
        self.scale_factor = scale_factor

        # Automatically cut frames and create reflections
        self.cut_frames()
        self.create_reflections()

    def cut_frames(self):
        # Cut frames from the sprite sheet
        for i in range(self.frame_count):
            x = i * self.frame_width
            rect = pygame.Rect(x, 0, self.frame_width, self.frame_height)
            frame = self.sprite_sheet.subsurface(rect)
            
            # Scale the frame if necessary
            if self.scale_factor != 1:
                frame = pygame.transform.scale(frame, (self.frame_width * self.scale_factor, self.frame_height * self.scale_factor))
            
            self.frames.append(frame)

    def create_reflections(self):
        # Create reflected frames
        for frame in self.frames:
            reflected_frame = pygame.transform.flip(frame, True, False)
            self.reflected_frames.append(reflected_frame)

    def get_frame(self, index: int, reflected=False):
        # Return the frame at the given index; if reflected, return the reflected frame
        if reflected:
            return self.reflected_frames[index % self.frame_count]
        return self.frames[index % self.frame_count]
