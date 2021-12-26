# bird Class file
import pygame
import itertools


class Bird(pygame.sprite.Sprite):
    def __init__(self, images, idx, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = list(images.values())[idx]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = position

        # vertical direction speed, up is positive
        self.speed = 9

        # change bird flying images index
        self.bird_idx = idx
        self.bird_idx_cycle = itertools.cycle([0, 1, 2, 1])
        self.bird_idx_change_count = 0

        # game logic attrib
        self.is_dead = False

    # update the bird
    def update(self, boundary_values, time_passed):
        # update in vertical position
        self.speed -= 77 * time_passed
        self.rect.top -= self.speed

        # check if bird collides with the top or bottom boundaries
        is_dead = False
        if self.rect.bottom > boundary_values[1]:
            is_dead = True
            self.speed = 0
            self.rect.bottom = boundary_values[1]
        if self.rect.top < boundary_values[0]:
            is_dead = True
            self.speed = 0
            self.rect.top = boundary_values[0]
        self.is_dead = is_dead

        # change bird flying images index to simulate the flap effects
        self.bird_idx_change_count += 1
        if self.bird_idx_change_count % 5 == 0:
            self.bird_idx = next(self.bird_idx_cycle)
            self.image = list(self.images.values())[self.bird_idx]
            self.bird_idx_change_count = 0

    # do the flap action
    def flap(self):
        self.speed = max(9, self.speed + 2)

    # put the bird onto the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
