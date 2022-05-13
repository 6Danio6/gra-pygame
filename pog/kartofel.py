import pygame

from random import randint

from pygame.locals import *

from game_proba import move
pygame.init()

clock = pygame.time.Clock()
Clock = pygame.time.Clock()

window_size = [1280,720]

Display = pygame.Surface((640,360))

screen = pygame.display.set_mode(window_size)

tiles = [pygame.Rect(0,350,1000,50), pygame.Rect(300,300,100,25)]

class Player:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("kartofel.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord,self.y_cord,self.width,self.height)
        self.momentum = 0

    def tick(self, keys, tiles):
        speed = 5
        jump_power = 8
        if keys[pygame.K_w]:
            self.momentum -= jump_power
        if keys[pygame.K_a]:
            self.x_cord -= speed
        if keys[pygame.K_d]:
            self.x_cord += speed
        if keys[pygame.K_s]:
            self.y_cord += speed
        self.hitbox = pygame.Rect(self.x_cord,self.y_cord,self.width,self.height)
        self.y_cord += self.momentum
        self.momentum += 0.3
        move(self,[self.x_cord,self.y_cord],tiles)
        if(self.momentum > 4):
            self.momentum = 4
    def draw(self):
        Display.blit(self.image,(self.x_cord,self.y_cord))
    
    def collision_test(self, tiles):
        collisions = []
        for tile in tiles:
            if self.hitbox.colliderect(tile):
                collisions.append(tile)
        return collisions

    def move(self,movement,tiles):
        self.hitbox.x += movement[0]
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        collisions = collision_test(self,tiles)
        for tile in collisions:
            if movement[0] > 0:
                self.hitbox.right = tile.left
                collision_types['right'] = True
            if movement[0] < 0:
                self.hitbox.left = tile.right
                collision_types['left'] = True
        self.hitbox.y += movement[1]
        collisions = collision_test(self,tiles)
        for tile in collisions:
            if movement[1] > 0:
                self.hitbox.bottom = tile.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                self.hitbox.top = tile.bottom
                collision_types['top'] = True
        return self.hitbox, collision_types



def main():
    run = True
    player = Player()
    while run:
        Display.fill((0,0,0))

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