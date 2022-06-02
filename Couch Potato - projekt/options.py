from button import Button
import pygame, settings, sys, gra, levels, menu

button_1 = pygame.image.load("buttons/button_normal.png")
button_2 = pygame.image.load("buttons/button_over.png")
plus_1 = pygame.image.load("buttons/plus1.png")
plus_2 = pygame.image.load("buttons/plus2.png")
minus_1 = pygame.image.load("buttons/minus1.png")
minus_2 = pygame.image.load("buttons/minus2.png")

def Options():
    file = open("volume.txt", "w")
    while True:
        bg = pygame.image.load("backgrounds/bg5.png")
        bg = pygame.transform.scale(bg, (settings.window_size[0],settings.window_size[1]))
        settings.screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = settings.get_font(1,100).render("OPTIONS", False, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        volume1_text = settings.get_font(2,60).render("Volume", False, "#ffffff")
        volume1_rect = volume1_text.get_rect(center=(640, 270))
        volume2_text = settings.get_font(2,60).render(f"{settings.volume}%", False, "#ffffff")
        volume2_rect = volume2_text.get_rect(center=(640, 360))

        QUIT_BUTTON = Button(image=button_1, pos=(640, 600), 
                            text_input="Back", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        MINUS_BUTTON = Button(image=minus_1, pos=(490, 360), 
                            text_input=None, font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")
        PLUS_BUTTON = Button(image=plus_1, pos=(790, 360), 
                            text_input=None, font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")

        settings.screen.blit(MENU_TEXT, MENU_RECT)
        settings.screen.blit(volume1_text, volume1_rect)
        settings.screen.blit(volume2_text, volume2_rect)
        
        for button in [QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, button_1, button_2)
            button.update(settings.screen)
        for button in [PLUS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, plus_1, plus_2)
            button.update(settings.screen)
        for button in [MINUS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, minus_1, minus_2)
            button.update(settings.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings.sounds[1].play()
                file.truncate(0)
                file.write(str(settings.volume))
                file.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.sounds[1].play()
                    file.truncate(0)
                    file.write(str(settings.volume))
                    file.close()
                    menu.Menu()
                if MINUS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.sounds[1].play()
                    if settings.volume > 0:
                        settings.volume -= 10
                if PLUS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.sounds[1].play()
                    if settings.volume < 100:
                        settings.volume += 10

        settings.set_all_volume(settings.sounds, settings.volume)
        pygame.mixer.music.set_volume(settings.volume/100)

        pygame.display.update()