import pygame, settings, sys, menu
from button import Button
from kartofel import Player
from main import rpc, czas

def Gra(map_number):
    rpc.update(
    state = "przechodzi level "+ str(map_number),
    large_image = "couchpotato",
    start = czas)

    tile_pics = settings.load_tiles()
    game_map = settings.load_map(f"maps/map{map_number}.txt")
    player_x, player_y = settings.load_map_player_cords(map_number)
    player = Player(player_x, player_y,map_number)
    tiles, saws, couch, spikes, border = settings.display_map(game_map, tile_pics, settings.angle)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        settings.Display.fill((140, 255, 234))

        settings.angle -= 2
        settings.scroll[0] += int((player.hitbox.x - settings.scroll[0] - 300)/10)
        settings.scroll[1] += int((player.hitbox.y - settings.scroll[1] - 152)/10)

        keys = pygame.key.get_pressed()
        tiles, saws, couch, spikes, border = settings.display_map(game_map, tile_pics, settings.angle)

        player.tick(keys, tiles, saws, spikes, couch, border)
        player.draw()

        PLAY_BACK = Button(image=None, pos=(120, 40), text_input="BACK", font=settings.get_font(1,60), base_color="White", hovering_color="Green")

        settings.screen.blit(pygame.transform.scale(settings.Display,(settings.window_size)),(0,0))
        
        PLAY_BACK.update(settings.screen)
        pygame.display.update()
        settings.Clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    settings.sounds[1].play()
                    menu.Menu()