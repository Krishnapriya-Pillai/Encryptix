import sys
import pygame
import numpy

pygame.init()

White = (255, 255, 255)
Black = (0, 0, 0)   
Red = (255, 0, 0)
Green = (0, 255, 0) 
Gray = (130, 130, 130)

Width = 300
Height = 300
Line_width = 5
Board_rows = 3
Board_cols = 3
square_size = Width // Board_cols
circle_radius = square_size // 3
circle_radius = 15
cross_width = 25

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic Tac Toe")   
screen.fill(Black)

board = numpy.zeros((Board_rows, Board_cols))

def draw_lines(color=White):
    for i in range(1, Board_rows):
        pygame.draw.line(screen, color, (0, i * square_size), (Width, i * square_size), Line_width)
        pygame.draw.line(screen, color, (i * square_size, 0), (i * square_size, Height), Line_width)


def draw_figures(color=White):
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, Line_width)
            elif board[row][col] == 2:
                start_pos = (int(col * square_size + square_size // 4), int(row * square_size + square_size // 4))
                end_pos = (int((col + 1) * square_size - square_size // 4), int((row + 1) * square_size - square_size // 4))
                pygame.draw.line(screen, color, start_pos, end_pos, cross_width)
                pygame.draw.line(screen, color, (start_pos[0], end_pos[1]), (end_pos[0], start_pos[1]), cross_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0


def is_board_full(check_board = board):
    for row in range(Board_rows):
        for col in range(Board_cols):
            if check_board[row][col] == 0:
                return False
    return True




def check_win(play, check_board = board):
    for row in range(Board_rows):
        if all(check_board[row][col] == play for col in range(Board_cols)):
            return True

    for col in range(Board_cols):
        if all(check_board[row][col] == play for row in range(Board_rows)):
            return True
        
    if check_board[0][0] == play and check_board[1][1] == play and check_board[2][2] == play:
        return True
    
    if check_board[0][2] == play and check_board[1][1] == play and check_board[2][0] == play:
        return True


    return False


def min_max(minmax_board, depth, is_maximizing):
    if check_win(2, minmax_board):
        return 10 - depth
    elif check_win(1, minmax_board):
        return depth - 10
    elif is_board_full(minmax_board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(Board_rows):
            for col in range(Board_cols):
                if minmax_board[row][col] == 0:
                    minmax_board[row][col] = 2
                    score = min_max(minmax_board, depth + 1, False)
                    minmax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(Board_rows):
            for col in range(Board_cols):
                if minmax_board[row][col] == 0:
                    minmax_board[row][col] = 1
                    score = min_max(minmax_board, depth + 1, True)
                    minmax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

    

def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == 0:
                board[row][col] = 2
                score = min_max(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False



def reset_game():
    screen.fill(Black)
    draw_lines()
    for row in range(Board_rows):
        for col in range(Board_cols):
            board[row][col] = 0

draw_lines()

player = 1
running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and running:
            mouseX = event.pos[0]// square_size
            mouseY = event.pos[1]// square_size


            if available_square(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_win(player):
                    draw_figures(Red)
                    running = False
                player = player % 2 + 1

                if running:
                    if best_move():
                        draw_figures(Green)
                        if check_win(2):
                            running = False
                        player = player % 2 + 1

                if running:
                    if is_board_full():
                        draw_figures(Gray)
                        running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                running = True
                player =1
        
    if running:
        draw_figures()

    else:
        if check_win(1):
            draw_figures(Green)
            draw_lines(Green)

        elif check_win(2):
            draw_figures(Red)
            draw_lines(Red)

        else:
            draw_figures(Gray)
            draw_lines(Gray)

    pygame.display.update()
                

    

        
