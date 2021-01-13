import pygame


class Texture():
    def __init__(self, parent):
        self.parent = parent

    def file(self, filename, scale=1):
        self.parent.image = pygame.image.load(filename).convert_alpha()
        if scale != 1:
            self.scale(scale)
        self.update()

    def image(self, image, scale=1):
        self.parent.image = image
        if scale != 1:
            self.scale(scale)
        self.update()

    def scale(self, scale):
        w, h = self.parent.image.get_size()
        self.parent.image = pygame.transform.scale(
            self.parent.image, (w * scale, h * scale))

    def update(self):
        self.parent.rect = self.parent.image.get_rect()
        self.parent.dirty = True
