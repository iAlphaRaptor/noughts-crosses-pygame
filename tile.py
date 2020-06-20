import pygame

WHITE = (255,255,255)

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
        self.value = False

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, (100, 100, 200), [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.rect.x = (self.index % 3) * 300
        self.rect.y = (self.index // 3) * 300

    def changeValue(self, changeTo):
        self.value = changeTo
        if self.value == "NOUGHT":
            self.image.fill(WHITE)
            self.image.blit(NOUGHT, (0,0))
        elif self.value == "CROSS":
            self.image.fill(WHITE)
            self.image.blit(CROSS, (0,0))
        else:
            pygame.draw.rect(self.image, (0,0,0), [0, 0, self.width, self.height])

    def isClicked(self, mousex, mousey):
        return self.rect.collidepoint(mousex, mousey)
