import pygame, settings, menu

class Couch:
    def __init__(self):
        self.image = pygame.image.load("couch.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(0,0,self.width,self.height)
        self.collisions = []

    def tick(self, keys, tiles):
        self.picture_cords = [self.hitbox.x, self.hitbox.y]
        self.movement = [0,0]
        if len(self.collisions) > 0:
            menu.Menu()

    def draw(self):
        self.image = pygame.transform.flip(self.image,self.flip,False)
        settings.Display.blit(self.image,(self.picture_cords[0] ,self.picture_cords[1]))