import pygame, settings, menu, time

class Player:
    def __init__(self, player_x, player_y):
        self.image = pygame.image.load("player_animations\idle\idle_0.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(player_x,player_y,self.width,self.height)
        self.momentum = 0
        self.movement = [0,0]
        self.collisions = []
        self.speed = 4
        self.jump_power = 6
        self.idle_animation = settings.load_animation("player_animations/idle", [20,20])
        self.run_animation = settings.load_animation("player_animations/run", [6,6,6,6,6,6,6,6])
        self.jump_animation = settings.load_animation("player_animations/jump", [1,1,1])
        self.current_frame = 0
        self.flip = False
        self.picture_cords = [0,0]
        self.potato_image = pygame.image.load("on_couch_potato.png")

    def tick(self, keys, tiles, saws, spikes,couch):
        self.picture_cords = [self.hitbox.x, self.hitbox.y]
        self.movement = [0,0]
        if keys[pygame.K_w]:
            if self.collisions['bottom']:
                self.momentum = 0
                self.momentum -= self.jump_power
        if keys[pygame.K_a]:
            self.movement[0] -= self.speed
            self.flip = True
        if keys[pygame.K_d]:
            self.movement[0] += self.speed
            self.flip = False

        self.hitbox = pygame.Rect(self.hitbox.x,self.hitbox.y,self.width,self.height)
        if self.momentum < 0:
            self.image = self.jump_animation[1]
        elif self.momentum > 0:
            self.image = self.jump_animation[2]
        self.movement[1] += self.momentum
        self.momentum += 0.2
        if self.momentum > 4:
            self.momentum = 4
            
        self.hitbox, self.collisions = settings.move(self.hitbox,self.movement,tiles)
        if self.collisions['top']:
            self.momentum = 0
        if self.collisions['bottom']:
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
        if len(settings.collision_test(self.hitbox,saws)) > 0:
            menu.Menu()
        if len(settings.collision_test(self.hitbox,spikes)) > 0:
            menu.Menu()
        if len(settings.collision_test(self.hitbox,couch)) > 0:
            settings.Display.blit(self.potato_image,(self.picture_cords[0]-2 ,self.picture_cords[1]+4))
            menu.Menu()

    def draw(self):
        self.image = pygame.transform.flip(self.image,self.flip,False)
        settings.Display.blit(self.image,(self.picture_cords[0] - settings.scroll[0] ,self.picture_cords[1] - settings.scroll[1]))