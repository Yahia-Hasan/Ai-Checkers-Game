import pygame

# Import constants and game-related functions from other modules
from checkers.constants import WIDTH, HEIGHT, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax,get_all_moves

# Set the frames per second for Pygame window updates
FPS = 1

# Create a Pygame window with specified dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    # Create a new game and store its initial state
    game = Game(WIN)
    new_board = game.get_board()
    level=3
    while run:
        clock.tick(FPS)

        # If it's the AI player's turn (white), choose a move
        if game.turn == WHITE:
            moves = get_all_moves(game.get_board(), WHITE, game)

            # Check if there are any valid moves for the AI player
            if not moves:
                print("no more moves ,WHITE WINS!")
                run = False

            # Choose a move using selected algorithm and search depth
            else:
                    value, new_board = minimax(game.get_board(), level, WHITE, game)
                    # Update the game state with the chosen move
                    game.ai_move(new_board)

        # If it's the human player's turn (red), choose a random move
        else:
            moves = get_all_moves(game.get_board(), RED, game)

            # Check if there are any valid moves for the human player
            if not moves:
                print("no moves for red ,WHITE WINS!")
                run = False

            # Choose a random move
            else:
                game.random_move(new_board)

        # Check if there is a winner yet
        if game.winner() is not None:
            # Display winner message and end the game loop
            if(game.winner()==WHITE):
                print("WHITE WINS!")
            else:
                print("RED WINS!")
            run = False

        # Update the Pygame window with the current game state
        game.update()

    # Quit the Pygame window after the game ends
    pygame.quit()

# Call the main function to execute the game
main()
