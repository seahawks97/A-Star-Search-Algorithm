import pygame as pg
import sys


def startAlgorithm():
    """
        NW   N   NE
           \ | /
        W -  x  - E
           / | \
        SW   S   SE

    Cost to travel from x to a direction:
    NW, NE, SW, SE = sqrt(2)
    N, E, S, W = 1

    Index updates for each direction from a cell at position [x, y]:
    NW = [x-1, y-1]
    N = [x, y-1]
    NE = [x+1, y-1]
    W = [x-1, y]
    E = [x+1, y]
    SW = [x-1, y+1]
    S = [x, y+1]
    SE = [x+1, y+1]
    """
    found = False
    while not found:
        pass
        break
    # heuristic = find_euclidian_distance()


def resetCell(cellRow, cellCol):
    board[cellRow][cellCol] = 0
    boardSurfs[cellRow][cellCol].fill(colors[0])


def find_euclidian_distance(x1, y1, x2, y2):
    return (abs(x2-x1)**2 + abs(y2-y1)**2) ** 0.5

pg.init()
size = width, height = 601, 661
screen = pg.display.set_mode(size)
pg.display.set_caption('A* Pathfinding Algorithm Visualizer')
fps = 32
clock = pg.time.Clock()

btnSpacing = 10
numRows, numCols = 20, 20
cellSize = 30
menuBarH = 60

# TO DO:
# Event Logic
# Algorithm

# Colors
white = 255, 255, 255
gray = 127, 127, 127
green = 0, 255, 0
red = 255, 0, 0
yellow = 255, 255, 0
slate = 63, 127, 190
darkGray = 63, 63, 63
black = 0, 0, 0
colors = [white, gray, green, red, yellow, slate, darkGray, black]

# Data Structure
# 20 rows, 20 cols of tiles init to 0
# Value tells type of cell & color index
# 0 -> empty, open pathway (white)
# 1 -> wall (not traversable) (gray)
# 2 -> (1) starting position tile (green)
# 3 -> (1) ending position tile (red)
# 4 -> cell checked but not traversed in path finding (yellow)

# Initialize structure
# Note: Walls are border of window
# Make cells for board
board, boardSurfs, boardPositions = [[]], [[]], [[]]
for row in range(numRows):
    for col in range(numCols):
        # Color/type structure
        board[row].append(0)
        # Surfaces structure
        newCellSurf = pg.Surface((cellSize-1, cellSize-1))
        newCellSurf.fill(white)
        boardSurfs[row].append(newCellSurf)
        # Positions of tiles
        tileX = 1 + (cellSize * col)
        tileY = 1 + menuBarH + (cellSize * row)
        boardPositions[row].append((tileX, tileY))
        # print(boardPositions[row][col])

    if row != numRows - 1:
        board.append([])
        boardSurfs.append([])
        boardPositions.append([])

# Menu Bar
menuBar = pg.Surface((size[0], menuBarH))
menuBar.fill(darkGray)

# Menu Button Text
ourFont = pg.font.SysFont(name='Times New Roman,Arial', size=24)
startBtnSrf = ourFont.render('Start Algorithm', True, black, white)
setStartBtnSrf = ourFont.render('Set Start', True, black, green)
setTargetBtnSrf = ourFont.render('Set Target', True, black, red)
drawWallBtnSrf = ourFont.render('Draw Walls', True, black, gray)
resetBtnSrf = ourFont.render('Reset Grid', True, black, white)

# Button dimensions
menuBarW = menuBar.get_size()[0]
startBtnW, startBtnH = startBtnSrf.get_size()
setStartBtnW, setStartBtnH = setStartBtnSrf.get_size()
setTargetBtnW, setTargetBtnH = setTargetBtnSrf.get_size()
drawWallBtnW, drawWallBtnH = drawWallBtnSrf.get_size()
resetBtnW, resetBtnH = resetBtnSrf.get_size()

# Button positions
startBtnPos = (1 * btnSpacing, menuBarH / 2 - startBtnH / 2)
setStartBtnPos = (2 * btnSpacing + startBtnW, menuBarH / 2 - setStartBtnH / 2)
setTargetBtnPos = (3 * btnSpacing + startBtnW + setStartBtnW, menuBarH / 2 - setTargetBtnH / 2)
drawWallBtnPos = (4 * btnSpacing + startBtnW + setStartBtnW + setTargetBtnW, menuBarH / 2 - drawWallBtnH / 2)
resetBtnPos = (5 * btnSpacing + startBtnW + setStartBtnW + setTargetBtnW + drawWallBtnW, menuBarH / 2 - resetBtnH / 2)

# Border
fieldSrf = pg.Surface((width, height - menuBarH))
fieldSrf.fill(white)
# Grid
for i in range(numRows+1):
    pg.draw.line(fieldSrf, black, (i*cellSize, 0), (i*cellSize, numRows*cellSize))
    pg.draw.line(fieldSrf, black, (0, i*cellSize), (numCols*cellSize, i*cellSize))

# Main
mouseType = 0
while True:
    for event in pg.event.get():
        # https://riptutorial.com/pygame/example/18046/event-loop
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            # mouseType = 0
            # Get mouse position
            x, y = pg.mouse.get_pos()

            # if it's over a button, select that button type no matter what
            # Start algorithm button
            if startBtnPos[0] < x < startBtnPos[0]+startBtnW and startBtnPos[1]< y < startBtnPos[1]+startBtnH:
                startAlgorithm()

            # Set start button
            elif setStartBtnPos[0] < x < setStartBtnPos[0]+setStartBtnW and setStartBtnPos[1] < y < setStartBtnPos[1]+setStartBtnH:
                if mouseType == 2:  # turn button off
                    setStartBtnSrf = ourFont.render('Set Start', True, black, green)
                    mouseType = 0
                else:  # turn button on
                    setStartBtnSrf = ourFont.render('Set Start', True, green, black)
                    setTargetBtnSrf = ourFont.render('Set Target', True, black, red)
                    drawWallBtnSrf = ourFont.render('Draw Walls', True, black, gray)
                    mouseType = 2

            # Set target button
            elif setTargetBtnPos[0] < x < setTargetBtnPos[0]+setTargetBtnW and setTargetBtnPos[1] < y < setTargetBtnPos[1]+setTargetBtnH:
                if mouseType == 3:  # turn button off
                    setTargetBtnSrf = ourFont.render('Set Target', True, black, red)
                    mouseType = 0
                else:  # turn button on
                    setStartBtnSrf = ourFont.render('Set Start', True, black, green)
                    setTargetBtnSrf = ourFont.render('Set Target', True, red, black)
                    drawWallBtnSrf = ourFont.render('Draw Walls', True, black, gray)
                    mouseType = 3

            # Draw walls
            elif drawWallBtnPos[0] < x < drawWallBtnPos[0]+drawWallBtnW and drawWallBtnPos[1] < y < drawWallBtnPos[1]+drawWallBtnH:
                if mouseType == 1:  # turn button off
                    drawWallBtnSrf = ourFont.render('Draw Walls', True, black, gray)
                    mouseType = 0
                else:  # turn button on
                    setStartBtnSrf = ourFont.render('Set Start', True, black, green)
                    setTargetBtnSrf = ourFont.render('Set Target', True, black, red)
                    drawWallBtnSrf = ourFont.render('Draw Walls', True, gray, black)
                    mouseType = 1

            # Clear all button
            elif resetBtnPos[0] < x < resetBtnPos[0]+resetBtnW and resetBtnPos[1] < y < resetBtnPos[1]+resetBtnH:
                setStartBtnSrf = ourFont.render('Set Start', True, black, green)
                setTargetBtnSrf = ourFont.render('Set Target', True, black, red)
                drawWallBtnSrf = ourFont.render('Draw Walls', True, black, gray)
                mouseType = 0
                for row in range(len(board)):
                    for col in range(len(board[row])):
                        board[row][col] = 0
                        boardSurfs[row][col].fill(colors[0])

            elif y > menuBarH:  # mouse is on board
                # find which tile clicked
                y -= menuBarH
                cellRow, cellCol = y//cellSize, x//cellSize
                #  - if button is selected, change tile to button type
                if mouseType != 0:
                    for row in range(numRows):
                        for col in range(numCols):
                            if board[row][col] == 2 and mouseType == 2:
                                resetCell(row, col)
                            elif board[row][col] == 3 and mouseType == 3:
                                resetCell(row, col)

                board[cellRow][cellCol] = mouseType
                boardSurfs[cellRow][cellCol].fill(colors[mouseType])
                #  - if no button selected, do nothing

        elif event.type == pg.MOUSEMOTION:
            # Get mouse position
            try:
                x, y = pg.mouse.get_pos()
                if y > menuBarH:  # mouse is on board (nothing if on menu)
                    y -= menuBarH
                    cellRow, cellCol = y//cellSize, x//cellSize
                    if mouseType == 1 and pg.mouse.get_pressed()[0]:
                        board[cellRow][cellCol] = 1
                        boardSurfs[cellRow][cellCol].fill(colors[1])
                    if mouseType == 0 and pg.mouse.get_pressed()[0]:
                        resetCell(cellRow=cellRow, cellCol=cellCol)
            except IndexError:
                # mouse is off window on launch
                pass
            except AttributeError:
                # mouse is off window, clicks, and is dragged back onto window
                pass

    # Update stuff
    clock.tick(fps)
    # Blits
    screen.blit(menuBar, (0, 0))
    screen.blit(fieldSrf, (0, menuBarH))
    screen.blit(startBtnSrf, startBtnPos)
    screen.blit(setStartBtnSrf, setStartBtnPos)
    screen.blit(setTargetBtnSrf, setTargetBtnPos)
    screen.blit(drawWallBtnSrf, drawWallBtnPos)
    screen.blit(resetBtnSrf, resetBtnPos)

    # Tiles rendered
    for row in range(numRows):
        for col in range(numCols):
            screen.blit(boardSurfs[row][col], (boardPositions[row][col]))

    # Final Update
    pg.display.update()



