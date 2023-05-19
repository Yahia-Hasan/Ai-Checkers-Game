from copy import deepcopy
import pygame

# Constants for colors
RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    # Recursive function to evaluate potential moves and choose best move using minimax algorithm
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def alpha_beta(position, depth, alpha, beta, max_player, game):
    # Recursive function to evaluate potential moves and choose best move using alpha-beta pruning algorithm
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = alpha_beta(move, depth - 1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval >= beta:
                break
            if maxEval > alpha:
                alpha = maxEval
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = alpha_beta(move, depth - 1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval <= alpha:
                break
            if minEval < beta:
                beta = minEval
                best_move = move
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    # Simulates a move on the game board by moving a piece to a new position and removing any skipped pieces
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    # Returns a list of all possible moves for a given color
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game, board, piece):
    # Draws all valid moves for a given piece on the game board (not currently used in code)
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)
