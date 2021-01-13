import pygame
import loop
import compute
import sys
dt = 1/60


class Rotate():
    def __init__(self, parent):
        self.parent = parent
        self.loop = loop.Loop()

    def left(self, value, speed=0, count=sys.maxsize):
        if speed == 0:
            self.parent.image = pygame.transform.rotate(
                self.parent.image, value)
            self.parent.dirty = True
        else:
            da = speed * dt
            steps = value / da
            path = [da * i for i in range(int(steps))]
            self.loop.program(path, count)
            self.image = self.parent.image

    def right(self, value, speed=0, count=sys.maxsize):
        if speed == 0:
            self.parent.image = pygame.transform.rotate(
                self.parent.image, -value)
            self.parent.dirty = True
        else:
            da = speed * dt
            steps = value / da
            path = [-da * i for i in range(int(steps))]
            self.loop.program(path, count)
            self.image = self.parent.image

    def update(self):
        pass
        # if self.loop.in_progress():
        #     self.parent.image = pygame.transform.rotate(
        #         self.image, self.loop.pop())
        # if not self.loop.is_active():
        #     self.parent.image = self.image
        #self.parent.dirty = True
