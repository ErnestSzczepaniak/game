import object
import action
import pygame

class Player(object.Object, pygame.sprite.Sprite):
    def __init__(self):
        object.Object.__init__(self)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([32, 32])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.move = action.Move(self)

    def update(self):
        self.move.update()