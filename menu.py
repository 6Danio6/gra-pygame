from button import Button
import pygame, settings, sys, gra

def Menu():
    while True:
        bg = pygame.image.load("backgrounds/bg4.png")
        bg = pygame.transform.scale(bg, (settings.window_size[0],settings.window_size[1]))
        settings.screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = settings.get_font(1,140).render("COUCH POTATO", False, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("buttons/Play.png"), pos=(640, 250), 
                            text_input="Play", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("buttons/Options.png"), pos=(640, 400), 
                            text_input="Options", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("buttons/Quit.png"), pos=(640, 550), 
                            text_input="Quit", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")

        settings.screen.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(settings.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gra.Gra()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gra.Gra()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()