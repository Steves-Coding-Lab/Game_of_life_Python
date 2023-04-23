from game_of_life import *


next_gen = load_init_pattern()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()

    current_gen = copy.deepcopy(next_gen)
    
    screen.fill(WHITE) #refresh screen with white background
    draw_grid() # Draw grid squares on top of white background
    display_cells(current_gen)

    time.sleep(PAUSE_LENGTH) #pause while loop for short time

    pygame.display.update()

    get_next_gen(current_gen, next_gen)