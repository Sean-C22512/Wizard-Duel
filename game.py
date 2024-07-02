import pygame
from wizard import Wizard  # Ensure you have a Wizard class defined in wizard.py


class Game:

    def __init__(self, config):
        self.window_size = config['resolution']
        self.full_screen = config['full-screen']
        self.window = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN if self.full_screen else 0)
        pygame.display.set_caption(config['Wizard Duel'])
        self.clock = pygame.time.Clock()

        # Initialize your wizard and add it to a sprite group
        self.wizard = Wizard("Harry", 100, 200, 'assets/wizard.png')
        self.sprites = pygame.sprite.Group()
        # noinspection PyTypeChecker
        self.sprites.add(self.wizard)  # Add the wizard to the sprite group

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_events(event)

            self.update()
            self.render()
            self.clock.tick(60)  # Maintain 60 frames per second

    def handle_events(self, event):
        # Handle game-specific events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # Check if the 'd' key is pressed
                self.wizard.move('right', 10)  # Move the wizard right by 10 units

    def update(self):
        # Update the game logic here, move sprites, check for collisions etc.
        self.sprites.update()

    def render(self):
        # Clear the screen each frame
        self.window.fill((0, 0, 0))
        # Draw all sprites
        self.sprites.draw(self.window)
        # Flip the display buffers
        pygame.display.flip()