from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    # Constants for piece graphics
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        # Initialize piece object with row, column, and color properties
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()     # Calculate position of the piece on the board

    def calc_pos(self):
        # Calculate x and y position of piece based on its row and column on the board
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        # Sets king status of a piece to True
        self.king = True
    
    def draw(self, win):
        # Draws piece on the board in appropriate location with appropriate graphics
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        # Move piece to new row and column on the board
        self.row = row
        self.col = col
        self.calc_pos()     # Recalculate position of the piece after the move

    def __repr__(self):
        # Returns a string representation of the piece object (its color)
        return str(self.color)
