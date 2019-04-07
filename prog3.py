#!/usr/bin/python3
"""
					CSCI 503 - Assignment 3 - Spring 2019
					Progammer: Manoj Veluru
					Z-ID: Z1840907
					Section: 1
					Date Due: March 21, 2019
					Purpose: N Queens Puzzle
"""
from time import time
from random import seed,randint

'''Method to start the program by calling the solveNQueens function'''
def driver():
	for N in range(1,9):
		solveNQueens(initBoard(N))	#Function call to solveNQueens method with returned board as input

'''Method to initialize choosen seed value and also to return initialized two-dimensional list matrix'''	
def initBoard(N):
	seed(time())		
	startCol = False
	board = [[startCol for i in range(N)]for j in range(N)] #initialized 2-dimensional matrix with false
	return board

'''Method to print board size and also to place N Queens on the board'''	
def solveNQueens(N): 
	print("Board size = "+str(len(N)))
	if solveNQueensUtil(N,0):
		printBoard(N)	#Function call to Print board on screen
	else:
		print("Solution does not exist.")
	print()

'''Method to call recursive routine and also to use backtracking technique'''
def solveNQueensUtil(board,row):
	if row >= len(board):
		return True
	col = randint(0,len(board)-1) #initialized column with random column number
	for i in range(len(board)):
		if i==0 and isSafe(board,row,col): #loop to check whether its safe to place queen on particular position
			board[row][col]= True
			if solveNQueensUtil(board,row+1):	#recur to place rest of the queens
				return True
			board[row][col]=False #backtracking
		if i!=col and isSafe(board,row,i):	#loop to check whether its safe to place queen on particular position
			board[row][i]= True
			if solveNQueensUtil(board,row+1):	#recur to place rest of the queens
				return True
			board[row][i]=False	#backtracking
	return False

'''Method to check whether it is safe to place que
en in particular position'''	
def isSafe(board,row,col):
	for i in range(row):
		for j in range(len(board)):
			if board[i][j]:
				if abs(row-i)==abs(col-j):	#loop to check queen presence in same columns and diagonal
					return False
		if board[i][col]: #loop to check whether the queen is already present in particular position
			return False
	return True
	
'''Method to print properly formatted rectangular table'''	
def printBoard(board):
	horizontalLine = '-'*6
	for i in range(len(board)):
		print(" "+(horizontalLine*len(board))[:-1],end='')	#printing horizontalLines on board
		print()
		for l in range(len(board)):	#loop to print vertical lines
			print('|     ',end='')
		print('|')
		for j in range(len(board)):	#loop to print vertical lines along with queen and empty space
			if board[i][j]==True:
				print('|  Q  ',end='')
			else:
				print('|     ',end='')
		print('|')
		for k in range(len(board)):	#loop to print vertical lines
			print('|     ',end='')
		print('|')
	print(' '+(horizontalLine*len(board))[:-1],end='')	#printing horizontalLines on board
	print()

driver()	#Function call to start the program