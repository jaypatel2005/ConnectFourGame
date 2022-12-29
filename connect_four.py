import numpy as np 
import pygame
import os
import sys
from colors import *

row, col = 6, 7
SQUARESIZE = 100
win_width, win_height = col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE

class Board:
    def __init__(self, row, col, play_width, play_height):
        self.row = row
        self.col = col
        self.play_width = play_width
        self.play_height = play_height
        self.board = self.create_board(row, col)
        self.RADIUS = SQUARESIZE//2 - 5

    def winning(self, piece):
        # check horizontal
        for r in range(self.row):
            for c in range(self.col-3):
                if self.board[r][c] == self.board[r][c+1] == self.board[r][c+2] == self.board[r][c+3] == piece:
                    return True
        
        # check vertical
        for r in range(self.row-3):
            for c in range(self.col):
                if self.board[r][c] == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c] == piece:
                    return True

        # check positively slopped diaganols
        for r in range(self.row-3):
            for c in range(self.col-3):
                if self.board[r][c] == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3] == piece:
                    return True                

        # check negitively slopped diaganols
        for r in range(self.row-3):
            for c in range(3, self.col):
                if self.board[r][c] == self.board[r+1][c-1] == self.board[r+2][c-2] == self.board[r+3][c-3] == piece:
                    return True
                    
        return False 

    def create_board(self, row, col):
        return np.zeros((row, col))

    def drawBoard(self, win, x, y):
        pygame.time.delay(50)
        win.fill(BLACK)
        pygame.draw.rect(win, BLUE, (x, y, self.play_width, self.play_height))
        circleX, circleY = x, y
        for row in range(self.row):
            for col in range(self.col): 
                if self.board[row][col] == 0:
                    pygame.draw.circle(win, BLACK, (circleX+(SQUARESIZE//2), circleY+(SQUARESIZE//2)), self.RADIUS)
                elif self.board[row][col] == 1:
                    pygame.draw.circle(win, RED, (circleX+(SQUARESIZE//2), circleY+(SQUARESIZE//2)), self.RADIUS)
                elif self.board[row][col] == -1:
                    pygame.draw.circle(win, LIME, (circleX+(SQUARESIZE//2), circleY+(SQUARESIZE//2)), self.RADIUS)
                circleX += SQUARESIZE
            circleY += SQUARESIZE
            circleX = x

        pygame.display.update()

    def drawNextCircle(self, win, pos, color):
        if pos[0] > win_width - SQUARESIZE//2:
            x = win_width - SQUARESIZE//2
        elif pos[0] < SQUARESIZE//2:
            x = SQUARESIZE//2
        else:
            x = pos[0]

        pygame.draw.circle(win, color, (x, SQUARESIZE//2), self.RADIUS)
        pygame.display.update()

    def valid_move(self, c):
        for r in range(self.row):
            r = self.row - r - 1
            if self.board[r][c] == 0:
                return True
        return False

    def changeBoard(self, c, turn):
        for r in range(self.row):
            r = self.row - r - 1
            if self.board[r][c] == 0:
                self.board[r][c] = turn
                break

    def matchDrawcondi(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == 0:
                    return False
        return False

    def showWinning(self, win, turn, matchDraw=False):
        pygame.font.init()
        font = pygame.font.SysFont('lucidasans', 70)
        if matchDraw:
            text = font.render("Match Draw!", True, WHITE)
        elif turn == 1:
            text = font.render("Red wins!", True, RED)
        else:
            text = font.render("Green wins!", True, LIME)

        while True:
            win.blit(text, ((win_width - text.get_width())//2, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    return False

            pygame.display.update()
            pygame.time.delay(200)

    def restart(self):
        self.board = self.create_board(self.row, self.col)


play_width, play_height = win_width, win_height - SQUARESIZE
board = Board(row, col, play_width, play_height)

clock = pygame.time.Clock()

def main():
    os.chdir("C:\MY DATA\JAY\my games")
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Connect 4")
    
    nextColor = RED
    turn = 1
    running = True
    while running:
        clock.tick(60)

        board.drawBoard(win, 0, SQUARESIZE)

        pos = pygame.mouse.get_pos()
        board.drawNextCircle(win, pos, nextColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                c = pos[0] // SQUARESIZE
                if board.matchDrawcondi():
                    board.changeBoard(c, turn)
                    board.drawBoard(win, 0, SQUARESIZE)
                    if board.showWinning(win, turn):
                        running = False                        
                    board.restart()
                    
                if turn == 1:
                    if board.valid_move(c):
                        nextColor = LIME
                        board.changeBoard(c, turn)
                        if board.winning(turn):
                            board.drawBoard(win, 0, SQUARESIZE)
                            if board.showWinning(win, turn):
                                running = False                        
                            board.restart()
                        turn = -1
                else:
                    if board.valid_move(c):
                        nextColor = RED
                        board.changeBoard(c, turn)
                        if board.winning(turn):
                            board.drawBoard(win, 0, SQUARESIZE)
                            if board.showWinning(win, turn):
                                running = False
                            board.restart()
                        turn = 1

if __name__ == "__main__":
    main()