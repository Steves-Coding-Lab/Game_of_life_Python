from game_of_life import *

#Generate the initial population
grid_state = [[DEAD for _ in range(TOTAL_ROWS_COLS)]
              for _ in range(TOTAL_ROWS_COLS)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            #Save gridstate to txt file when quitting
            with open ("initial_pattern.txt", "w") as file:
                for row in grid_state:
                    row_string = ""
                    for cell in row:
                        row_string += str(cell)
                    file.write(row_string + "\n")       
            pygame.quit()
            sys.exit()

        #Handle mouse events and toggle cell states
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE   

            #Toggle cell states
            if grid_state[row][col] == DEAD:
                grid_state[row][col] = ALIVE
            else:
                grid_state[row][col] = DEAD

    screen.fill(WHITE) #refresh screen with white background
    draw_grid() # Draw grid squares on top of white background
    display_cells(grid_state)   #Display all cells currently alive

    pygame.display.update()