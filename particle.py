import object
import pygame
import random

class Particle(object.Object, pygame.sprite.Sprite):
    def __init__(self, x, y):
        object.Object.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.time = random.randint(1, 32)
        self.position.value = [x, y]
        self.image = pygame.Surface([self.time, self.time])
        self.rect = self.image.get_rect()

    def update(self):
        self.time -= random.randint(1, 3)
        if self.time > 0:
            self.image = pygame.Surface([self.time, self.time])
            br = 60 - self.time
            self.image.fill((150 - br, 150 - br, 150 - br))
            self.rect = self.image.get_rect()
        else:
            self.kill()

def spawn(game, player):
    x, y = player.position.value
    for _ in range(5):
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)
        p = Particle(x, y)
        game.particles.add(p)