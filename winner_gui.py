import time

import pygame

# Function for displaying winner message on a Pygame window
def display_winner(displayed_text,start_time,algorithm):
    # Set up the window dimensions and background color
    screen_width = 500
    screen_height = 100
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0,0,0))

    # Set the window title and font style
    pygame.display.set_caption("WINNER!")
    font = pygame.font.Font(None, 36)

    # Render and position the winner message text on the window
    text = font.render(displayed_text, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, text_rect)

    # Update the window and wait for user input to quit the game
    pygame.display.update()
    end_time=time.time()
    total_time=end_time-start_time
    print("time ellapsed for the game to end using",algorithm,"algorithm:",total_time,"seconds")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Function for selecting AI algorithm via button selection on a Pygame window
def select_algorithm(algorithm):
    # Initialize Pygame

    # Set up the window dimensions
    win_width = 700
    win_height = 700

    # Initialize the font module
    pygame.font.init()

    # Set up the fonts for the buttons
    BUTTON_FONT = pygame.font.Font(None, 36)

    # Set up the colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Set up the window
    WIN = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Select Algorithm")

    # Set up the buttons
    MINIMAX_BUTTON = pygame.Rect(50, 100, 150, 50)
    ALPHA_BETA_BUTTON = pygame.Rect(225, 100, 150, 50)

    # Set up the default algorithm

    # Main game loop
    while not algorithm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user closes the window
                pygame.quit()
                exit()

            # Check if a button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MINIMAX_BUTTON.collidepoint(event.pos):
                    algorithm = "Minimax"
                elif ALPHA_BETA_BUTTON.collidepoint(event.pos):
                    algorithm = "Alpha-Beta"

        # Draw the buttons on the window
        pygame.draw.rect(WIN, RED, MINIMAX_BUTTON)
        pygame.draw.rect(WIN, GREEN, ALPHA_BETA_BUTTON)

        # Add text to the buttons
        minimax_text = BUTTON_FONT.render("Minimax", True, WHITE)
        alpha_beta_text = BUTTON_FONT.render("Alpha-Beta", True, WHITE)

        WIN.blit(minimax_text, (65, 115))
        WIN.blit(alpha_beta_text, (240, 115))

        # Update the window
        pygame.display.update()

    # Quit the Pygame window and return the selected algorithm
    #pygame.display.quit()
    return algorithm
