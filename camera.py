import pygame
import object
import attribute
import action

class Camera(object.Object):
    def __init__(self, width, height):
        super().__init__()
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface((width, height))
        self.move = action.Move(self)
        self.follow = action.Follow(self)

        self.size.value = [width, height]


    def mouse_position(self):
        x, y = pygame.mouse.get_pos()
        return attribute.Position(
            self.position.x.value - self.size.x.value / 2 + x,
            self.position.y.value - self.size.y.value / 2 + y)


    def adjust(self, item):
            item.rect.centerx = item.position.x.value - \
                self.position.x.value + self.size.x.value / 2
            item.rect.centery = item.position.y.value - \
                self.position.y.value + self.size.y.value / 2
        
        # if compute.are_intersecting(self.position, self.size, item.position, item.size):  # new

        #     item.dirty = True
        #     item.visible = True
        # else:
        #     item.visible = False

    def update(self, map):
        self.follow.update()
        self.move.update()
        self.background.blit(map, (0, 0), (self.position.x.value - self.size.x.value / 2,
                                                self.position.y.value - self.size.y.value / 2, self.size.x.value, self.size.y.value))
        self.screen.blit(self.background, (0, 0))