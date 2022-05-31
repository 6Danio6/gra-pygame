from button import Button
import pygame, settings, sys, gra, menu

buttonimg = pygame.image.load("buttons/square.png")

def Levels():
    while True:
        bg = pygame.image.load("backgrounds/bg5.png")
        bg = pygame.transform.scale(bg, (settings.window_size[0],settings.window_size[1]))
        settings.screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = settings.get_font(1,100).render("LEVELS", False, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        BUTTON_1 = Button(image=buttonimg, pos=(490, 300), 
                            text_input="1", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        BUTTON_2 = Button(image=buttonimg, pos=(640, 300), 
                            text_input="2", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        BUTTON_3 = Button(image=buttonimg, pos=(790, 300), 
                            text_input="3", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        BUTTON_4 = Button(image=buttonimg, pos=(490, 450), 
                            text_input="4", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        BUTTON_5 = Button(image=buttonimg, pos=(640, 450), 
                            text_input="5", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        BUTTON_6 = Button(image=buttonimg, pos=(790, 450), 
                            text_input="6", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        PLAY_BACK = Button(image=None, pos=(120, 40), text_input="BACK", font=settings.get_font(1,75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(MENU_MOUSE_POS)
        settings.screen.blit(MENU_TEXT, MENU_RECT)

        for button in [BUTTON_1,BUTTON_2,BUTTON_3,BUTTON_4,BUTTON_5,BUTTON_6]:
            button.update(settings.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_1.checkForInput(MENU_MOUSE_POS, ):
                    gra.Gra(1,20,120)
                if BUTTON_2.checkForInput(MENU_MOUSE_POS):
                    gra.Gra(2)
                if BUTTON_3.checkForInput(MENU_MOUSE_POS):
                    gra.Gra(3)
                if BUTTON_4.checkForInput(MENU_MOUSE_POS):
                    gra.Gra(4)
                if BUTTON_5.checkForInput(MENU_MOUSE_POS):
                    gra.Gra(5)
                if BUTTON_6.checkForInput(MENU_MOUSE_POS):
                    gra.Gra(6)
                if PLAY_BACK.checkForInput(MENU_MOUSE_POS):
                    menu.Menu()

        pygame.display.update()