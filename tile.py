import pygame

loadN = pygame.image.load("Images/nought.png")
loadC = pygame.image.load("Images/cross.png")
NOUGHT = pygame.transform.scale(loadN, (300,300))
CROSS = pygame.transform.scale(loadC, (300,300))

class Tile(pygame.sprite.Sprite):
    def __init__(self, index, width, height):
        super().__init__()

        self.index = index
        self.width = width
        self.height = height
        self.x = (self.index // 3) * 300
        self.y = (self.index % 3) * 300
        self.value = False
        self.image = pygame.Surface([width, height])

        self.rect = self.image.get_rect()

    def changeValue(self, changeTo):
        self.value = changeTo
        if self.value == "NOUGHT":
            self.image.blit(NOUGHT, (self.x, self.y))
        elif self.value == "CROSS":
            self.image.blit(CROSS, (self.x, self.y))

    def isClicked(self, mousex, mousey):
        return self.rect.collidepoint(mousex, mousey)
