import pygame
import settings, menu

pygame.init()
pygame.mixer.pre_init(44100,16,2,512)
pygame.mixer.set_num_channels(64)

def main():
    settings.intro()
    menu.Menu()
if __name__ == "__main__":
    main()