import pygame, settings, menu

class Couch:
    def __init__(self):
        self.image = pygame.image.load("couch.png")
        self.image = pygame.transform.scale(self.image, (32,32))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(0,0,self.width,self.height)
        self.collisions = []

    def tick(self):
        self.picture_cords = [self.hitbox.x, self.hitbox.y]
        if len(self.collisions) > 0:
            menu.Menu()

    def draw(self):
        settings.Display.blit(self.image,(self.picture_cords[0] ,self.picture_cords[1]))