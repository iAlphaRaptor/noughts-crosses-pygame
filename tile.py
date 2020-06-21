import pygame

WHITE = (255,255,255)

def createPieces(screenwidth, screenheight):
    loadN = pygame.image.load("Images/nought.png")
    loadC = pygame.image.load("Images/cross.png")
    NOUGHT = pygame.transform.scale(loadN, (int((screenwidth/3)-(screenwidth/18)), int((screenheight/3)-(screenheight/18))))
    CROSS = pygame.transform.scale(loadC, (int((screenwidth/3)-(screenwidth/18)), int((screenheight/3)-(screenheight/18))))
    return NOUGHT, CROSS

class Tile(pygame.sprite.Sprite):
    def __init__(self, index, screenX, screenY, NOUGHT, CROSS):
        super().__init__()

        self.index = index
        self.width = (screenX / 3) - screenX / 18
        self.height = (screenY / 3) - screenY / 18
        self.NOUGHT = NOUGHT
        self.CROSS = CROSS
        self.value = False
        self.played = False

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = (self.index % 3) * (screenX / 3) + screenX / 36
        self.rect.y = (self.index // 3) * (screenY / 3) + screenX / 36

    def changeValue(self, changeTo):
        self.value = changeTo
        if self.value == "NOUGHT":
            self.image.fill(WHITE)
            self.image.blit(self.NOUGHT, (0,0))
        elif self.value == "CROSS":
            self.image.fill(WHITE)
            self.image.blit(self.CROSS, (0,0))
        self.played = True

    def isClicked(self, mousex, mousey):
        return self.rect.collidepoint(mousex, mousey)
