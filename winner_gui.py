import pygame

# Function for displaying winner message on a Pygame window
def display_winner(displayed_text):
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
