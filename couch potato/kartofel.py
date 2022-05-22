import pygame

import settings

class Player:
    def __init__(self):
        self.image = pygame.image.load("player_animations\idle\idle_0.png")
        self.image.set_colorkey((34, 177, 76))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(0,0,self.width,self.height)
        self.momentum = 0
        self.movement = [0,0]
        self.collisions = []
        self.speed = 4
        self.jump_power = 6
        self.idle_animation = settings.load_animation("player_animations/idle", [20,20], (34, 177, 76))
        self.run_animation = settings.load_animation("player_animations/run", [6,6,6,6,6,6,6,6], (34, 177, 76))
        self.jump_animation = settings.load_animation("player_animations/jump", [1,1,1], (34, 177, 76))
        self.current_frame = 0
        self.flip = False
        self.picture_cords = [0,0]

    def tick(self, keys, tiles):
        self.picture_cords = [self.hitbox.x, self.hitbox.y]
        self.movement = [0,0]
        if keys[pygame.K_w]:
            if self.collisioins['bottom']:
                self.momentum = 0
                self.momentum -= self.jump_power
        if keys[pygame.K_a]:
            self.movement[0] -= self.speed
            self.flip = True
        if keys[pygame.K_d]:
            self.movement[0] += self.speed
            self.flip = False
        self.hitbox = pygame.Rect(self.hitbox.x,self.hitbox.y,self.width,self.height)
        self.movement[1] += self.momentum
        self.momentum += 0.2
        if(self.momentum > 4):
            self.momentum = 4
        self.hitbox, self.collisioins = settings.move(self.hitbox,self.movement,tiles)
        if self.collisioins['top']:
            self.momentum = 0
        if self.collisioins['bottom']:
            if self.movement[0] == 0:
                self.flip = False
                if self.current_frame > len(self.idle_animation) - 1:
                    self.current_frame = 0
                self.image = self.idle_animation[self.current_frame]
            if self.movement[0] != 0:
                if self.current_frame > len(self.run_animation) - 1:
                    self.current_frame = 0
                self.image = self.run_animation[self.current_frame]
                self.picture_cords[0] -= 13
                self.picture_cords[1] -= 9
            self.current_frame += 1

    def draw(self):
        settings.Display.blit(pygame.transform.flip(self.image,self.flip,False),(self.picture_cords[0] ,self.picture_cords[1]))