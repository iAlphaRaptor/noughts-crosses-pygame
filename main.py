import pygame
from tile import Tile
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 145, 0)

SCREENWIDTH = 900
SCREENHEIGHT = 900
size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Noughts and Crosses")

carryOn = True
clock = pygame.time.Clock()

tiles = pygame.sprite.Group()
for i in range(3):
    for j in range(3):
        tiles.add(Tile((i*3)+j, SCREENWIDTH/3, SCREENHEIGHT/3))

tiles.sprites()[2].changeValue("NOUGHT")
tiles.sprites()[5].changeValue("CROSS")
tiles.sprites()[1].changeValue("CROSS")

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            for tile in tiles:
                if tile.isClicked(mousex, mousey):
                    print(tile.index)

    #Game Logic
    tiles.update()

    ## Drawing Code ##
    # Background
    screen.fill(GREEN)
    pygame.draw.line(screen, WHITE, (SCREENWIDTH / 3, 0), (SCREENWIDTH / 3, SCREENHEIGHT), 5)
    pygame.draw.line(screen, WHITE, (SCREENWIDTH * 2/3, 0), (SCREENWIDTH * 2/3, SCREENHEIGHT), 5)
    pygame.draw.line(screen, WHITE, (0, SCREENHEIGHT / 3), (SCREENWIDTH, SCREENHEIGHT / 3), 5)
    pygame.draw.line(screen, WHITE, (0, SCREENHEIGHT * 2/3), (SCREENWIDTH, SCREENHEIGHT * 2/3), 5)

    #for t in tiles:
    #    pygame.draw.rect(screen, (0,0,0), (t.rect.x, t.rect.y, SCREENWIDTH/3, SCREENHEIGHT/3))

    tiles.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
