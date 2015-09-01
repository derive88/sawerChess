#! /usr/bin/env python
"""
 Project: Python Chess
 File name: ChessBoard.py
 Description:  Board layout; contains what pieces are present
	at each square.

 Copyright (C) 2009 Steve Osborne, srosborne (at) gmail.com
 http://yakinikuman.wordpress.com/
 """

import string

class ChessBoard:
	def __init__(self,setupType=0):
		self.squares = 	[['e','e','e','e','e','e','e'],\
						['e','e','e','e','e','e','e'],\
						['e','e','e','e','e','e','e'],\
						['e','e','e','e','e','e','e'],\
						['e','e','e','e','e','e','e'],\
						['e','e','e','e','e','e','e'],\
						['e','e','e','e','e','e','e']]
		if setupType == 0:
			self.squares[0] = ['e','e','bP','bR','bT','bB','bK']
			self.squares[1] = ['e','e','e','bP','bJ','bQ','bB']
			self.squares[2] = ['wP','e','e','e','bP','bJ','bT']
			self.squares[3] = ['wR','wP','e','e','e','bP','bR']
			self.squares[4] = ['wT','wJ','wP','e','e','e','bP']
			self.squares[5] = ['wB','wQ','wJ','wP','e','e','e']
			self.squares[6] = ['wK','wB','wT','wR','wP','e','e']

		#Debugging set-ups
		#Testing IsLegalMove
		if setupType == 1:
			self.squares[0] = ['e','e','e','bR','bT','bB','bK']
			self.squares[1] = ['e','e','e','e','e','bQ','bB']
			self.squares[2] = ['wP','e','e','e','e','e','bT']
			self.squares[3] = ['wR','wP','e','e','e','e','bR']
			self.squares[4] = ['wT','wJ','wP','e','e','e','e']
			self.squares[5] = ['wB','wQ','wJ','wP','e','e','e']
			self.squares[6] = ['wK','wB','wT','wR','wP','e','e']


		#Testing IsInCheck, Checkmate
		if setupType == 2:
			self.squares[0] = ['e','e','e','e','e','e','e']
			self.squares[1] = ['e','e','e','e','e','e','e']
			self.squares[2] = ['e','e','e','e','bK','e','e']
			self.squares[3] = ['e','e','e','e','bR','e','e']
			self.squares[4] = ['e','e','bB','e','e','e','wR']
			self.squares[5] = ['wB','e','e','e','e','e','e']
			self.squares[6] = ['e','e','e','wK','wQ','e','wT']

		#Testing Defensive AI
		if setupType == 3:
			self.squares[0] = ['e','e','e','e','e','e','e']
			self.squares[1] = ['e','e','e','e','e','e','e']
			self.squares[2] = ['e','e','e','e','bK','e','e']
			self.squares[3] = ['e','e','e','e','bR','e','e']
			self.squares[4] = ['e','e','bB','e','e','e','wR']
			self.squares[5] = ['e','e','e','e','e','e','e']
			self.squares[6] = ['e','e','e','wK','wQ','e','wT']

	def GetState(self):
		return self.squares

	def ConvertMoveTupleListToAlgebraicNotation(self,moveTupleList):
		newTupleList = []
		for move in moveTupleList:
			newTupleList.append((self.ConvertToAlgebraicNotation(move[0]),self.ConvertToAlgebraicNotation(move[1])))
		return newTupleList

	def ConvertSquareListToAlgebraicNotation(self,list):
		newList = []
		for square in list:
			newList.append(self.ConvertToAlgebraicNotation(square))
		return newList

	def ConvertToAlgebraicNotation(self,(row,col)):
		#Converts (row,col) to algebraic notation
		#(row,col) format used in Python Chess code starts at (0,0) in the upper left.
		#Algebraic notation starts in the lower left and uses "a..h" for the column.
		return  self.ConvertToAlgebraicNotation_col(col) + self.ConvertToAlgebraicNotation_row(row)

	def ConvertToAlgebraicNotation_row(self,row):
		#(row,col) format used in Python Chess code starts at (0,0) in the upper left.
		#Algebraic notation starts in the lower left and uses "a..h" for the column.
		B = ['g','f','e','d','c','b','a']
		return B[row]

	def ConvertToAlgebraicNotation_col(self,col):
		#(row,col) format used in Python Chess code starts at (0,0) in the upper left.
		#Algebraic notation starts in the lower left and uses "a..h" for the column.
		A = ['1','2','3','4','5','6','7']
		return A[col]


	def GetFullString(self,p):
		if 'b' in p:
			name = "negro"
		else:
			name = "blanco"

		if 'P' in p:
			name = "Guerrero " + name
		if 'R' in p:
			name = "Pucara " + name
		if 'T' in p:
			name = "Llama " + name
		if 'B' in p:
			name = "Amauta " + name
		if 'Q' in p:
			name = "Coya " + name
		if 'K' in p:
			name = "Inca " + name
		if 'J' in p:
			name = "Jilanko " + name

		return name

	def color(self,p):
		if 'b' in p:
			color = 1
		else:
			color = 0
		return color

	def MovePiece(self,moveTuple):
		ayni=0
		counter=1
		counterking=2
		fromSquare_r = moveTuple[0][0]
		fromSquare_c = moveTuple[0][1]
		toSquare_r = moveTuple[1][0]
		toSquare_c = moveTuple[1][1]
		torreblanca = self.squares[3][0]
		alfilblanca = self.squares[5][0]
		blancatorre = self.squares[6][3]
		blancaalfil = self.squares[6][1]
		reyblanca = self.squares[6][0]
		torrenegra = self.squares[0][3]
		alfilnegro = self.squares[0][5]
		negratorre = self.squares[3][6]
		negroalfil = self.squares[1][6]
		reynegro = self.squares[0][6]

		fromPiece = self.squares[fromSquare_r][fromSquare_c]
		toPiece = self.squares[toSquare_r][toSquare_c]

		self.squares[toSquare_r][toSquare_c] = fromPiece
		self.squares[fromSquare_r][fromSquare_c] = 'e'

		fromPiece_fullString = self.GetFullString(fromPiece)
		toPiece_fullString = self.GetFullString(toPiece)
		piezaComida = self.color(toPiece)

		if toPiece == 'e' and reynegro=="bK" and torrenegra=="bR" and alfilnegro=='e' and fromPiece=="bK":
			messageString = fromPiece_fullString+ " ejecuta el AYNI URINZAYA "
		elif toPiece == 'e' and reynegro=="bK" and negratorre=="bR" and negroalfil=='e'and fromPiece=="bK":
			messageString = fromPiece_fullString+ " ejecuta el AYNI ARANZAYA "
		elif toPiece == 'e' and reyblanca=="wK" and torreblanca=="wR" and alfilblanca=='e' and fromPiece=="wK":
			messageString = fromPiece_fullString+ " ejecuta el AYNI ARANZAYA"
		elif toPiece == 'e' and reyblanca=="wK" and blancatorre=="wR" and blancaalfil=='e'and fromPiece=="wK":
			messageString = fromPiece_fullString+ " ejecuta el AYNI URINZAYA"

		elif toPiece == 'e':
			messageString = fromPiece_fullString+ " se mueve de "+self.ConvertToAlgebraicNotation(moveTuple[0])+\
						    " a "+self.ConvertToAlgebraicNotation(moveTuple[1])
			counter=1
			counterking=2
		else:
			messageString = fromPiece_fullString+ " de "+self.ConvertToAlgebraicNotation(moveTuple[0])+\
						" captura "+toPiece_fullString+" de "+self.ConvertToAlgebraicNotation(moveTuple[1])+"!"
			counter=0
			if piezaComida==1:
				counterking=1
			elif piezaComida==0:
				counterking=0
		if fromPiece == 'wK' or fromPiece=="wR":
			ayni=1
		if fromPiece == 'bK' or fromPiece=="bR":
			ayni=2

		#capitalize first character of messageString
		messageString = string.upper(messageString[0])+messageString[1:len(messageString)]

		return messageString,counter,counterking,ayni

"""	def Comer(self,moveTuple):
		toSquare_r = moveTuple[1][0]
		toSquare_c = moveTuple[1][1]

		toPiece = self.squares[toSquare_r][toSquare_c]

		if toPiece == 'e':
			comida = 1
		else:
			comida = 0

		return comida"""

if __name__ == "__main__":

	cb = ChessBoard(0)
	board1 = cb.GetState()
	for r in range(7):
		for c in range(7):
			print board1[r][c],
		print ""

	print "Move piece test..."
	cb.MovePiece(((0,0),(4,4)))
	board2 = cb.GetState()
	for r in range(7):
		for c in range(7):
			print board2[r][c],
		print ""