from button import Button
import pygame, settings, sys, levels, options
from main import rpc, czas

button_1 = pygame.image.load("buttons/button_normal.png")
button_2 = pygame.image.load("buttons/button_over.png")

def Menu():
    rpc.update(
    state = "siedzi w menu",
    large_image = "couchpotato",
    start = czas)
    while True:
        settings.set_all_volume(settings.sounds, settings.volume)
        pygame.mixer.music.set_volume(settings.volume/100)
        bg = pygame.image.load("backgrounds/bg5.png")
        bg = pygame.transform.scale(bg, (settings.window_size[0],settings.window_size[1]))
        settings.screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = settings.get_font(1,140).render("COUCH POTATO", False, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=button_1, pos=(640, 300), 
                            text_input="Play", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("buttons/Options.png"), pos=(50,50), 
                            text_input=None, font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=button_1, pos=(640, 500), 
                            text_input="Quit", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")

        settings.screen.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS,button_1,button_2)
            button.update(settings.screen)
        
        for button in [OPTIONS_BUTTON]:
            button.update(settings.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.sounds[1].play()
                    levels.Levels()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.sounds[1].play()
                    pygame.quit()
                    sys.exit()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.sounds[1].play()
                    options.Options()

        pygame.display.update() 