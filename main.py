import pygame
import sys
import object
import time
import random
import game
import player
import callback
import particle




    

game = game.Game()
game.camera.position.value = [512, 512]

player = player.Player()

player.position.value = [320, 320]
player.move.on_move = callback.Callback(particle.spawn, game, player)

game.camera.follow.start(player, distance=1, speed=150)

game.group.add(player)

cam = 10

# # bullet = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #game.camera.move.cartesian(game.camera.mouse_position(), speed=300)
            player.move.cartesian(game.camera.mouse_position(), speed=450)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        game.camera.position.y.value += cam
    if keys[pygame.K_w]:
        game.camera.position.y.value -= cam
    if keys[pygame.K_a]:
        game.camera.position.x.value -= cam
    if keys[pygame.K_d]:
        game.camera.position.x.value += cam

    game.refresh()
