import pygame, settings, sys, menu
from button import Button
from kartofel import Player

def Gra(map_number):
    tile_pics = settings.load_tiles()
    game_map = settings.load_map(f"maps/map{map_number}")
    player = Player()
    tiles = []
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        settings.Display.fill((140, 255, 234))

        keys = pygame.key.get_pressed()
        tiles = settings.display_map(game_map, tile_pics)

        player.tick(keys, tiles)
        player.draw()

        PLAY_BACK = Button(image=None, pos=(120, 40), text_input="BACK", font=settings.get_font(1,75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)

        settings.screen.blit(pygame.transform.scale(settings.Display,(settings.window_size)),(0,0))
        
        PLAY_BACK.update(settings.screen)
        pygame.display.update()
        settings.Clock.tick(60)
        #print(settings.Clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    menu.Menu()