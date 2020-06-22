import pygame, random
pygame.init()

boxFont = pygame.font.Font("Fonts/font.ttf", 40)
WHITE = (255, 255, 255)

class InputBox(pygame.sprite.Sprite):
    def __init__(self, colour, boxColour, textColour, text, screenX, screenY):
        super().__init__()

        self.colour = colour
        self.boxColour = boxColour
        self.textColour = textColour
        self.inactiveColour = boxColour
        temp = []
        for i in range(3):
            if self.boxColour[i] < 100:
                temp.append(self.boxColour[i] + 30)
            else:
                temp.append(self.boxColour[i] - random.randint(25, 100))
        print(temp)
        self.activeColour = (temp[0], temp[1], temp[2])

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
        self.image.blit(self.outputText, (10,10))
        pygame.draw.rect(self.image, boxColour, (10, 60, int((len(text)*20) - 20), 50))
        self.image.blit(self.boxText, (20, 60))

        self.active = False

    def isClicked(self, mousex, mousey):
        if self.rect.collidepoint(mousex, mousey):
            self.active = True
            self.boxColour = self.activeColour
        else:
            self.active = False
            self.boxColour = self.inactiveColour

        pygame.draw.rect(self.image, self.colour, (0, 0, int(len(self.text)*20), 120))
        self.image.blit(self.outputText, (10,10))
        pygame.draw.rect(self.image, self.boxColour, (10, 60, int((len(self.text)*20) - 20), 50))
        self.image.blit(self.boxText, (20, 60))

    def enterText(self,char):
        if char == pygame.K_BACKSPACE:
            self.inputText = self.inputText[:-1]
        else:
            self.inputText += chr(char)
        self.boxText = boxFont.render(self.inputText, True, self.textColour, None)

        self.image.fill(WHITE)
        pygame.draw.rect(self.image, self.colour, (0, 0, int(len(self.text)*20), 120))
        self.image.blit(self.outputText, (10,10))
        pygame.draw.rect(self.image, self.boxColour, (10, 60, int((len(self.text)*20) - 20), 50))
        self.image.blit(self.boxText, (20, 60))
