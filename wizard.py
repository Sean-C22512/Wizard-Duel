import pygame


class Wizard(pygame.sprite.Sprite):
    def __init__(self, name, max_health, max_mana, image_paths):
        super().__init__()
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.spells = []
        # Load images for different directions
        self.images = {
            'right': pygame.image.load(image_paths['right']).convert_alpha(),
            'left': pygame.image.load(image_paths['left']).convert_alpha(),
            'forward': pygame.image.load(image_paths['forward']).convert_alpha(),
            'back': pygame.image.load(image_paths['back']).convert_alpha()
        }

        self.image = self.images['forward']  # Start with the forward image
        self.rect = self.image.get_rect()
        self.position = self.rect.topleft

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

        # Update the wizard's image based on direction
        if direction in self.images:
            self.image = self.images[direction]

        if direction == 'forward':
            self.rect.y -= distance
        elif direction == 'back':
            self.rect.y += distance
        elif direction == 'left':
            self.rect.x -= distance
        elif direction == 'right':
            self.rect.x += distance

    def die(self):
        print(f"{self.name} has died.")

    def update(self):
        self.regenerate_mana(1)

    def add_spell(self, spell):
        self.spells.append(spell)
