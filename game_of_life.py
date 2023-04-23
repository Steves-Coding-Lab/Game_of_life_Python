import pygame, sys, os, copy, time

SC_WIDTH_HEIGHT = 800
TOTAL_ROWS_COLS = 80
CELL_SIZE = SC_WIDTH_HEIGHT // TOTAL_ROWS_COLS
ALIVE = 1
DEAD = 0

PAUSE_LENGTH = 0.15

#load cell image
ALIVE_IMG = pygame.image.load(os.path.join("Graphics", "ALIVE.jpg"))

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((SC_WIDTH_HEIGHT, SC_WIDTH_HEIGHT))


def load_init_pattern():
    next_gen=[]
    #Load initial population of alive and dead cells
    with open ("initial_pattern.txt", "r") as file:
        for line in file:
            row=[]
            for char in line.strip():
                row.append(int(char))
            next_gen.append(row)
    return next_gen


#Generate grid pattern
def draw_grid():
    for row in range(TOTAL_ROWS_COLS):
        for col in range(TOTAL_ROWS_COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

#Print all alive cells to screen
def display_cells(cells):
    for x in range(TOTAL_ROWS_COLS):
        for y in range(TOTAL_ROWS_COLS):
            if cells[y][x] == ALIVE:
                screen.blit(ALIVE_IMG, (x*CELL_SIZE, y*CELL_SIZE))


def get_next_gen(current_gen, next_gen):
    for x in range(TOTAL_ROWS_COLS):
        for y in range(TOTAL_ROWS_COLS):
            left = (x-1) % TOTAL_ROWS_COLS
            right = (x+1) % TOTAL_ROWS_COLS
            above = (y-1) % TOTAL_ROWS_COLS
            below = (y+1) % TOTAL_ROWS_COLS

            #Count the number of living neighbours
            numNeighbours = 0
            if current_gen[above][left] == ALIVE:
                numNeighbours += 1
            if current_gen[above][x] == ALIVE:
                numNeighbours += 1
            if current_gen[above][right] == ALIVE:
                numNeighbours += 1
            if current_gen[y][left] == ALIVE:
                numNeighbours += 1
            if current_gen[y][right] == ALIVE:
                numNeighbours += 1
            if current_gen[below][left] == ALIVE:
                numNeighbours += 1
            if current_gen[below][x] == ALIVE:
                numNeighbours += 1
            if current_gen[below][right] == ALIVE:
                numNeighbours += 1

            #Set cell based on Conway's rules
            if current_gen[y][x] == ALIVE and (numNeighbours == 2 or numNeighbours == 3):
                next_gen[y][x] = ALIVE
            elif current_gen[y][x] == DEAD and numNeighbours == 3:
                next_gen[y][x] = ALIVE
            else:
                next_gen[y][x] = DEAD