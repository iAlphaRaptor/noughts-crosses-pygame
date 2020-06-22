import pygame
pygame.init()

boxFont = pygame.font.Font("Fonts/font.ttf", 40)
WHITE = (255, 255, 255)

class InputBox(pygame.sprite.Sprite):
    def __init__(self, colour, boxColour, textColour, text, screenX, screenY):
        super().__init__()

        self.colour = colour
        self.boxColour = boxColour
        self.textColour = textColour
        self.questionText = text
        self.text = text
        self.inputText = ""

        self.image = pygame.Surface([int(len(text)*20), 120])
        self.rect = self.image.get_rect()
        self.rect.x = int((screenX / 2) - (len(text)*10))
        self.rect.y = (screenY / 2) - 60

        self.outputText = boxFont.render(self.questionText, True, textColour, None)
        self.boxText = boxFont.render(self.inputText, True, textColour, None)

        pygame.draw.rect(self.image, colour, (0, 0, int(len(text)*20), 120))
        self.image.blit(self.outputText, (60,10))
        pygame.draw.rect(self.image, boxColour, (10, 60, int((len(text)*20) - 20), 50))
        self.image.blit(self.boxText, (20, 60))

        self.active = False

    def isClicked(self, mousex, mousey):
        self.active = True
        return self.rect.collidepoint(mousex, mousey)

    def enterText(self,char):
        if char == pygame.K_BACKSPACE:
            self.inputText = self.inputText[:-1]
        else:
            self.inputText += chr(char)
        self.boxText = boxFont.render(self.inputText, True, self.textColour, None)

        self.image.fill(WHITE)
        pygame.draw.rect(self.image, self.colour, (0, 0, int(len(self.text)*20), 120))
        self.image.blit(self.outputText, (60,10))
        pygame.draw.rect(self.image, self.boxColour, (10, 60, int((len(self.text)*20) - 20), 50))
        self.image.blit(self.boxText, (20, 60))
