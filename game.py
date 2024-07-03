import pygame
from wizard import Wizard  # Ensure you have a Wizard class defined in wizard.py


class Game:
    def __init__(self, config):
        self.window_size = config['resolution']
        self.full_screen = config['full-screen']
        self.window = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN if self.full_screen else 0)
        pygame.display.set_caption(config['title'])
        self.clock = pygame.time.Clock()

        # Initialize your wizard and add it to a sprite group
        wizard_images = {
            'right': 'assets/wizard_right.png',
            'left': 'assets/wizard_left.png',
            'forward': 'assets/wizard_forward.png',
            'back': 'assets/wizard_back.png'
        }

        # Load heart images
        self.heart_images = [
            pygame.image.load(f'assets/{i}heart.png').convert_alpha() for i in range(6)
        ]

        # Initialize your wizard and add it to a sprite group
        self.wizard = Wizard("Harry", 100, 200, wizard_images)
        self.sprites = pygame.sprite.Group()
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
            elif event.key == pygame.K_w:  # Check if the 'w' key is pressed
                self.wizard.move('forward', 10)  # Move the wizard forward by 10 units
            elif event.key == pygame.K_a:  # Check if the 'a' key is pressed
                self.wizard.move('left', 10)  # Move the wizard left by 10 units
            elif event.key == pygame.K_s:  # Check if the 's' key is pressed
                self.wizard.move('back', 10)  # Move the wizard back by 10 units

    def update(self):
        self.sprites.update()

    def render(self):
        self.window.fill((0, 0, 0))
        self.sprites.draw(self.window)
        self.wizard.display_hearts(self.window, self.heart_images)
        pygame.display.flip()
