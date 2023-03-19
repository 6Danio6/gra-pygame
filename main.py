import pygame
import settings, menu
from pypresence import Presence
import time

czas=time.time()
rpc = Presence("1068973511420416122")
rpc.connect()
rpc.update(
    #details = "gra jest grana",
    state = "oglada epickie intro",
    large_image = "couchpotato",
    start = czas)

pygame.init()
pygame.mixer.pre_init(44100,16,2,512)
pygame.mixer.set_num_channels(64)

def main():
    settings.intro()
    menu.Menu()
if __name__ == "__main__":
    main()