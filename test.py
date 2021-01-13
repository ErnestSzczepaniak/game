import pygame
import math
import random
import collections
from function import normal_dist

WIDTH = 640
HEIGHT = 640

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
image = pygame.image.load('test_bg.png').convert_alpha()
image.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_SUB)
gradient = pygame.image.load('gradient.png').convert_alpha()
clock = pygame.time.Clock()

f0 = normal_dist(240, 110, 7, 0.08)
f1 = normal_dist(240, 100, 45, 0.2)
f2 = normal_dist(240, 120, 60, 0.4)


class Light():
    lights = []
    def __init__(self, index, x, y, scale):
        
        list = []
        scaled = pygame.transform.scale(gradient, (int(256 * scale), int(256 * scale)))
        
        for i in range(240):
            factor = 0
            if index == 0:
                factor = f0[i]
            elif index == 1:
                factor = f1[i]
            else:
                factor = f2[i]
            
            color = factor * 255
            
            frame = scaled.copy()
            frame.fill((0, color, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            
            list.append(frame)
        
        self.images = collections.deque(list)
        self.rect = scaled.get_rect()
        self.rect.center = (x, y)
        
        Light.lights.append(self)
        

    @staticmethod
    def render(screen):
        for light in Light.lights:
            if len(light.images) > 0:
                screen.blit(light.images.popleft(), light.rect, special_flags=pygame.BLEND_RGBA_ADD) 

            else:
                Light.lights.remove(light)
        

index = 0
shift = 70

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for index in range(3):
                if index == 0:
                    Light(index, x, y, 1 + 1 * index)    
                else:
                    Light(index, x + random.randint(-shift, shift),
                    y + random.randint(-shift, shift), 1 + 1 * index)    
            
            
    screen.blit(image, (0, 0))
    
    
    Light.render(screen)
    
    
    #screen.blit(actual2, rect2, special_flags=pygame.BLEND_RGB_ADD) 
    
    
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())