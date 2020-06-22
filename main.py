import pygame, tile, time, input_box
from win_check import winCheck
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 145, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (120, 120, 120)

FONT = pygame.font.Font("Fonts/font.ttf", 100)

SCREENWIDTH = 750
SCREENHEIGHT = 750
size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Noughts and Crosses")

carryOn = True
won = False
playing = "nought"
move = 1
clock = pygame.time.Clock()

NOUGHT, CROSS = tile.createPieces(SCREENWIDTH, SCREENHEIGHT)
tiles = pygame.sprite.Group()
for i in range(3):
    for j in range(3):
        tiles.add(tile.Tile((i*3)+j, SCREENWIDTH, SCREENHEIGHT, NOUGHT, CROSS))

boxes = pygame.sprite.Group()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not won:
                mousex, mousey = pygame.mouse.get_pos()
                for tile in tiles:
                    if tile.isClicked(mousex, mousey):
                        if not tile.played:
                            if playing == "nought":
                                tile.changeValue("NOUGHT")
                                playing = "cross"
                            else:
                                tile.changeValue("CROSS")
                                playing = "nought"
                            move += 1
                            if move >= 5:
                                if winCheck(tiles.sprites(), tile.index):
                                    if move % 2 == 1:
                                        winMessage = FONT.render("Crosses Wins!", True, BLUE, None)
                                    else:
                                        winMessage = FONT.render("Noughts Wins!", True, BLUE, None)
                                    won = True
                                elif move == 10:
                                    winMessage = FONT.render("DRAW!", True, BLUE, None)
                                    won = True
            for box in boxes:
                box.isClicked(mousex, mousey)
        if event.type == pygame.KEYDOWN:
            for box in boxes:
                if box.active:
                    box.enterText(event.key)

    #Game Logic
    tiles.update()
    boxes.update()

    ## Drawing Code ##
    if not won:
        # Background
        screen.fill(GREEN)
        pygame.draw.line(screen, WHITE, (SCREENWIDTH / 3, 0), (SCREENWIDTH / 3, SCREENHEIGHT), 5)
        pygame.draw.line(screen, WHITE, (SCREENWIDTH * 2/3, 0), (SCREENWIDTH * 2/3, SCREENHEIGHT), 5)
        pygame.draw.line(screen, WHITE, (0, SCREENHEIGHT / 3), (SCREENWIDTH, SCREENHEIGHT / 3), 5)
        pygame.draw.line(screen, WHITE, (0, SCREENHEIGHT * 2/3), (SCREENWIDTH, SCREENHEIGHT * 2/3), 5)

        # Tiles
        tiles.draw(screen)
    else:
        tiles.draw(screen)
        screen.blit(winMessage, (SCREENWIDTH/5, SCREENHEIGHT/3, 0, 0))

    boxes.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
