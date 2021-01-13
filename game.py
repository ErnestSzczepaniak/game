import pygame
import constant
import camera
import random

class Game():
    def __init__(self, ):
        pygame.init()
        self.camera = camera.Camera(1024, 768)
        self.load_map()
        
        self.camera.position.min = [self.camera.size.x.value / 2, self.camera.size.y.value / 2]
        self.camera.position.max = [self.map.get_width() - self.camera.size.x.value / 2, self.map.get_height() - self.camera.size.y.value / 2]


        self.clock = pygame.time.Clock()
        self.group = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()

    def load_map(self):
        self.map = pygame.Surface((6400, 6400))
        
        item = []
        
        for i in range(5):
            image = pygame.image.load('item' + str(i) + '.png').convert_alpha()
            image = pygame.transform.scale(image, (64, 64))
            item.append(image)

        for col in range(100):
            for row in range(100):
                c = random.choices(item, [20, 1, 1, 1, 1])
                rot = random.choice([0, 90, 180, 360])
                c = pygame.transform.rotate(c[0], rot)
                
                self.map.blit(c, (col * 64, row * 64))
        
        
        #self.map = pygame.image.load('bg.png').convert_alpha()

    def refresh(self):
        self.camera.update(self.map)

        self.group.update()
        self.particles.update()

        #updates = self.group.draw(self.camera.screen)

        # pygame.display.update(updates)

        #self.group.clear(self.camera.screen, self.camera.background)

        for sprite in self.group:
            self.camera.adjust(sprite)

        for sprite in self.particles:
            self.camera.adjust(sprite)

        self.particles.draw(self.camera.screen)
        self.group.draw(self.camera.screen)

        pygame.display.flip()

        self.clock.tick(constant.fps)
        
        print(self.clock.get_fps())
