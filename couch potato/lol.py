import pygame, os

window_size = [640,360]
screen = pygame.display.set_mode(window_size,0,32)

image = pygame.image.load("player_animations\idle\idle_0.png")
image.set_colorkey((34, 177, 76))
image = pygame.transform.flip(image,True,False)
image.set_colorkey((34, 177, 76))

while True:
    screen.fill((0,0,0))

    screen.blit(image,(0,0))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()



