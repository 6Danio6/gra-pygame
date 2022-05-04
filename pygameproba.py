import pygame, sys

from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

window_size = [640,360]

screen = pygame.display.set_mode(window_size,pygame.RESIZABLE,32)

player_image = pygame.image.load('kartofel.png')

player = pygame.Rect(100,100,player_image.get_width(),player_image.get_height())

tiles = [pygame.Rect(0,350,1000,50), pygame.Rect(300,300,100,25)]

def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

def move(rect,movement,tiles):
    rect.x += movement[0]
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    collisions = collision_test(rect,tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    collisions = collision_test(rect,tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

player_y_momentum = 0

up = False
down = False
right = False
left = False

fullscreen = False

while True:
    screen.fill((0,0,0))

    if fullscreen:
        pygame.FULLSCREEN

    movement = [0, 0]
    if up == True:
        if collisions['bottom']:
            player_y_momentum = -8
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -= 5

    movement[1] += player_y_momentum
    player_y_momentum += 0.3
    if(player_y_momentum > 4):
        player_y_momentum = 4

    player, collisions = move(player,movement, tiles)

    if collisions['top']:
        player_y_momentum = 0

    screen.blit(player_image,player)

    #pygame.draw.rect(screen, (255,255,255), player)

    for tile in tiles:
        pygame.draw.rect(screen,(255,0,0), tile)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE,32)
        if event.type == KEYDOWN:
            if event.key == K_w:
                up = True
            if event.key == K_s:
                down = True
            if event.key == K_d:
                right = True
            if event.key == K_a:
                left = True
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),pygame.FULLSCREEN,32)
                else:
                    screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),pygame.RESIZABLE,32)
            if event.key == K_r:
                if fullscreen:
                    screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN,32)
                else:
                    screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE,32)
            if event.key == K_ESCAPE:
                pygame.QUIT
                sys.exit(0)
        if event.type == KEYUP:
            if event.key == K_w:
                up = False
            if event.key == K_s:
                down = False
            if event.key == K_d:
                right = False
            if event.key == K_a:
                left = False

    pygame.display.update()
    clock.tick(60)