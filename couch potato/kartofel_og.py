import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
Clock = pygame.time.Clock()

window_size = [1280,720]

Display = pygame.Surface((640,360))

screen = pygame.display.set_mode(window_size)

tiles = [pygame.Rect(0,350,1000,50), pygame.Rect(300,250,100,25)]

class Player:
    def __init__(self):
        self.image = pygame.image.load("idle\Layer-1 1.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(0,0,self.width,self.height)
        self.momentum = 0
        self.movementem = [0,0]
        self.collisions = []

    def collision_test(self,rect, tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile):
                collisions.append(tile)
        return collisions

    def move(self,rect,movement,tiles):
        rect.x += movement[0]
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        collisions = self.collision_test(rect,tiles)
        for tile in collisions:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            if movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        collisions = self.collision_test(rect,tiles)
        for tile in collisions:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types


    def tick(self, keys, tiles):
        speed = 5
        jump_power = 12
        self.movementem = [0,0]
        if keys[pygame.K_w]:
            if self.collisioins['bottom']:
                self.momentum -= jump_power
        if keys[pygame.K_a]:
            self.movementem[0] -= speed
        if keys[pygame.K_d]:
            self.movementem[0] += speed
        if keys[pygame.K_s]:
            self.movementem[1] += speed
        self.hitbox = pygame.Rect(self.hitbox.x,self.hitbox.y,self.width,self.height)
        self.movementem[1] += self.momentum
        self.momentum += 0.2
        if(self.momentum > 4):
            self.momentum = 4
        self.hitbox, self.collisioins = self.move(self.hitbox,self.movementem,tiles)
        if self.collisioins['top']:
            self.momentum = 0

    def draw(self):
        Display.blit(self.image,(self.hitbox.x,self.hitbox.y))
    



def main():
    run = True
    player = Player()
    while run:
        Display.fill((140, 255, 234))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        player.tick(keys, tiles)
        player.draw()
        for tile in tiles:
            pygame.draw.rect(Display,(255,0,0), tile)

        screen.blit(pygame.transform.scale(Display,(window_size)),(0,0))
        pygame.display.update()
        Clock.tick(60)
        print(Clock.get_fps())
if __name__ == "__main__":
    main()