import pygame
from kartofel import Player

from pygame.locals import *
pygame.init()

import settings

def main():
    tile_pics = settings.load_tiles()
    game_map = settings.load_map("map")
    run = True
    player = Player()
    tiles = []
    while run:
        settings.Display.fill((140, 255, 234))

        keys = pygame.key.get_pressed()

        tiles = settings.display_map(game_map, tile_pics)

        player.tick(keys, tiles)
        player.draw()

        settings.screen.blit(pygame.transform.scale(settings.Display,(settings.window_size)),(0,0))
        pygame.display.update()
        settings.Clock.tick(60)
        #print(settings.Clock.get_fps())
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
if __name__ == "__main__":
    main()