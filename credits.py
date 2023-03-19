from button import Button
import pygame, settings, sys, menu
from main import rpc, czas

button_1 = pygame.image.load("buttons/button_normal.png")
button_2 = pygame.image.load("buttons/button_over.png")

def Credits():
    rpc.update(
    state = "zdobyl esse",
    large_image = "couchpotato",
    start = czas)
    while True:
        bg = pygame.image.load("backgrounds/bg5.png")
        bg = pygame.transform.scale(bg, (settings.window_size[0],settings.window_size[1]))
        settings.screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        grats_text = settings.get_font(1,80).render("Gratulacje uzytkowniku!!!", False, "#ffffff")
        grats_rect = grats_text.get_rect(center=(640, 100))
        credits_text = settings.get_font(2,30).render("Twórcy wszystkiego: Danio i Kerasjan - KD Studio", False, "#ffffff")
        credits_rect = credits_text.get_rect(center=(640, 270))

        QUIT_BUTTON = Button(image=button_1, pos=(640, 600), text_input="Back", font=settings.get_font(2,75), base_color="#d7fcd4", hovering_color="White")

        settings.screen.blit(credits_text, credits_rect)

        settings.screen.blit(grats_text, grats_rect)
        
        for button in [QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, button_1, button_2)
            button.update(settings.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.Menu()

        settings.set_all_volume(settings.sounds, settings.volume)

        pygame.display.update() 