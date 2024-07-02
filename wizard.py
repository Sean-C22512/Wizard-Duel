import pygame


class Wizard(pygame.sprite.Sprite):
    def __init__(self, name, max_health, max_mana, image_path):
        super().__init__()
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.spells = []
        self.image = pygame.image.load(image_path).convert_alpha()  # Load the image for the sprite
        self.rect = self.image.get_rect()  # The rectangle that encloses the image
        self.position = self.rect.topleft  # Set the initial position

    def cast_spell(self, spell, target):
        if spell.mana_cost <= self.mana:
            spell.effect(target)
            self.mana -= spell.mana_cost
            return True
        return False

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def regenerate_mana(self, amount):
        self.mana += amount
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def move(self, direction, distance):
        # Move the wizard according to the direction
        if direction == 'up':
            self.rect.y -= distance
        elif direction == 'down':
            self.rect.y += distance
        elif direction == 'left':
            self.rect.x -= distance
        elif direction == 'right':
            self.rect.x += distance

    def die(self):
        print(f"{self.name} has died.")

    def update(self):
        # This method would be called each frame to handle automatic updates
        self.regenerate_mana(1)  # Example: Regenerate 1 mana per frame

    def add_spell(self, spell):
        self.spells.append(spell)
