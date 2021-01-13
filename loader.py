import json
import pygame

animations = {}


def init():
    pass


def load(name, scale=1):
    with open(name + '.json') as file_json:

        animations[name] = {}
        info = json.load(file_json)
        image = pygame.image.load(name + '.png').convert_alpha()
        width = info['width']
        height = info['height']

        for action in info['actions']:

            animations[name][action] = {}

            for direction in info['actions'][action]:

                animations[name][action][direction] = []

                row = info['actions'][action][direction]['row']
                frames = info['actions'][action][direction]['frames']

                for index in range(frames):
                    surface = pygame.Surface([width, height])
                    surface.set_colorkey((0, 0, 0))
                    surface.blit(image, (0, 0),
                                 (index * width, row * height, 32, 32))

                    if scale != 1:
                        surface = pygame.transform.scale(
                            surface, [width * scale, height * scale])

                    animations[name][action][direction].append(surface)
