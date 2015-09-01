#! /usr/bin/env python
"""
 Project: Python Chess
 File name: ChessRules.py
 Description:  Functionality for determining legal chess moves.

 Copyright (C) 2009 Steve Osborne, srosborne (at) gmail.com
 http://yakinikuman.wordpress.com/
 """
class ChessRules():
	def IsCheckmate(self,board,color,ayniB,ayniN):
		#returns true if 'color' player is in checkmate
		#Call GetListOfValidMoves for each piece of current player
		#If there aren't any valid moves for any pieces, then return true

		if color == "negro":
			myColor = 'b'
			enemyColor = 'w'
		else:
			myColor = 'w'
			enemyColor = 'b'

		myColorValidMoves = [];
		for row in range(7):
			for col in range(7):
				piece = board[row][col]
				if myColor in piece:
					myColorValidMoves.extend(self.GetListOfValidMoves(board,color,(row,col),ayniB,ayniN))

		if len(myColorValidMoves) == 0:
			return True
		else:
			return False

	def GetListOfValidMoves(self,board,color,fromTuple,ayniBlanco,ayniNegro):
		ayniBa=ayniBlanco
		ayniNe=ayniNegro
		legalDestinationSpaces = []
		for row in range(7):
			for col in range(7):
				d = (row,col)
				if self.IsLegalMove(board,color,fromTuple,d,ayniBa,ayniNe):
					if not self.DoesMovePutPlayerInCheck(board,color,fromTuple,d):
						legalDestinationSpaces.append(d)
		return legalDestinationSpaces

	def IsLegalMove(self,board,color,fromTuple,toTuple,ayniBa,ayniNe):
		#print "IsLegalMove with fromTuple:",fromTuple,"and toTuple:",toTuple,"color = ",color
		fromSquare_r = fromTuple[0]
		fromSquare_c = fromTuple[1]
		toSquare_r = toTuple[0]
		toSquare_c = toTuple[1]
		fromPiece = board[fromSquare_r][fromSquare_c]
		toPiece = board[toSquare_r][toSquare_c]
		torreblanca = board[3][0]
		alfilblanca = board[5][0]
		blancatorre = board[6][3]
		blancalfil = board[6][1]
		torrenegra = board[0][3]
		alfilnegra = board[0][5]
		negratorre = board[3][6]
		negralfil = board[1][6]
		reynegro = board[0][6]
		reyblanco = board[6][0]
		rey1 = board[4][0]
		rey2 = board[5][0]
		rey3 = board[5][1]
		rey4 = board[6][1]
		rey5 = board[6][2]
		aynib=0
		aynin=0
		if color == "negro":
			enemyColor = 'w'
		if color == "blanco":
			enemyColor = 'b'

		if fromTuple == toTuple:
			return False

		if "P" in fromPiece:
			#Pawn
			if color == "negro":
				if toSquare_r-1 == fromSquare_r and toSquare_c+1 == fromSquare_c and toPiece == 'e':
					#black pawn on starting row can move forward 2 spaces if there is no one directly ahead
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_r == fromSquare_r+1 and toSquare_c == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_r == fromSquare_r and toSquare_c+1 == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True

			elif color == "blanco":
				if toSquare_r+1 == fromSquare_r and toSquare_c-1 == fromSquare_c and toPiece == 'e':
					#black pawn on starting row can move forward 2 spaces if there is no one directly ahead
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_r == fromSquare_r-1 and toSquare_c == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_r == fromSquare_r and toSquare_c-1 == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True

		elif "R" in fromPiece:
			#Rook
			if (toSquare_r == fromSquare_r or toSquare_c == fromSquare_c) and (toPiece == 'e' or enemyColor in toPiece):
				if self.IsClearPath(board,fromTuple,toTuple):
					return True

		elif "T" in fromPiece:
			#Knight
			col_diff = toSquare_c - fromSquare_c
			row_diff = toSquare_r - fromSquare_r
			if toPiece == 'e' or enemyColor in toPiece:
				if col_diff == 1 and row_diff == -2:
					return True
				if col_diff == 2 and row_diff == -1:
					return True
				if col_diff == 2 and row_diff == 1:
					return True
				if col_diff == 1 and row_diff == 2:
					return True
				if col_diff == -1 and row_diff == 2:
					return True
				if col_diff == -2 and row_diff == 1:
					return True
				if col_diff == -2 and row_diff == -1:
					return True
				if col_diff == -1 and row_diff == -2:
					return True

		elif "B" in fromPiece:
			#Bishop
			if ( abs(toSquare_r - fromSquare_r) == abs(toSquare_c - fromSquare_c) ) and (toPiece == 'e' or enemyColor in toPiece):
				if self.IsClearPath(board,fromTuple,toTuple):
					return True

		elif "Q" in fromPiece:
			#Queen
			if (toSquare_r == fromSquare_r or toSquare_c == fromSquare_c) and (toPiece == 'e' or enemyColor in toPiece):
				if self.IsClearPath(board,fromTuple,toTuple):
					return True
			if ( abs(toSquare_r - fromSquare_r) == abs(toSquare_c - fromSquare_c) ) and (toPiece == 'e' or enemyColor in toPiece):
				if self.IsClearPath(board,fromTuple,toTuple):
					return True

		elif "K" in fromPiece:
			#King
			col_diff = toSquare_c - fromSquare_c
			row_diff = toSquare_r - fromSquare_r
			if toPiece == 'e' or enemyColor in toPiece:
				if abs(col_diff) == 1 and abs(row_diff) == 0 :
					return True
				if abs(col_diff) == 0 and abs(row_diff) == 1:
					return True
				if abs(col_diff) == 1 and abs(row_diff) == 1:
					return True
			if toPiece == 'e' and fromPiece == reyblanco and color == "blanco" and  alfilblanca == 'e' and torreblanca == "wR" and ayniBa==0:
				if abs(col_diff) == 0 and abs(row_diff) == 2:
					return True
			if toPiece == 'e' and fromPiece == reyblanco and color == "blanco" and  blancalfil == 'e' and blancatorre == "wR" and ayniBa==0:
				if abs(col_diff) == 2 and abs(row_diff) == 0 :
					return True
			if toPiece == 'e' and fromPiece == reynegro and color == "negro" and  negralfil == 'e' and negratorre == "bR" and ayniNe==0:
				if abs(col_diff) == 0 and abs(row_diff) == 2:
					return True
			if toPiece == 'e' and fromPiece == reynegro and color == "negro" and  alfilnegra == 'e' and torrenegra == "bR" and ayniNe==0:
				if abs(col_diff) == 2 and abs(row_diff) == 0:
					return True

		elif "J" in fromPiece:
			#Jilanko
			if color == "negro":
                #moverse 2 espacios la primera vez
				if (fromSquare_r ==1 and fromSquare_c==4) and toSquare_r == fromSquare_r+2 and toSquare_c == fromSquare_c-2 and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if (fromSquare_r ==2 and fromSquare_c ==5)and toSquare_r == fromSquare_r+2 and toSquare_c == fromSquare_c-2 and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
                #posiciones para avanzar
				if toSquare_r-1 == fromSquare_r and toSquare_c+1 == fromSquare_c and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_c - fromSquare_c  ==1 and toSquare_r - fromSquare_r==1  and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_c - fromSquare_c  ==-1 and toSquare_r - fromSquare_r==-1  and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
                #posiciones para comer
				if toSquare_r == fromSquare_r+1 and toSquare_c == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_r == fromSquare_r and toSquare_c+1 == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True

			elif color == "blanco":
                #moverse 2 espacios la primera vez
				if (fromSquare_r ==4 and fromSquare_c==1) and toSquare_r+2 == fromSquare_r and toSquare_c-2 == fromSquare_c and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if (fromSquare_r ==5 and fromSquare_c ==2)and toSquare_r+2 == fromSquare_r and toSquare_c-2 == fromSquare_c and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
                #posiciones para avanzar
				if toSquare_r+1 == fromSquare_r and toSquare_c-1 == fromSquare_c and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_c - fromSquare_c  ==-1 and toSquare_r - fromSquare_r==-1  and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_c - fromSquare_c  ==1 and toSquare_r - fromSquare_r==1  and toPiece == 'e':
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
                #posiciones para comer
				if toSquare_r == fromSquare_r-1 and toSquare_c == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True
				if toSquare_r == fromSquare_r and toSquare_c-1 == fromSquare_c and enemyColor in toPiece:
					if self.IsClearPath(board,fromTuple,toTuple):
						return True


		return False #if none of the other "True"s are hit above

	def DoesMovePutPlayerInCheck(self,board,color,fromTuple,toTuple):
		#makes a hypothetical move; returns True if it puts current player into check
		fromSquare_r = fromTuple[0]
		fromSquare_c = fromTuple[1]
		toSquare_r = toTuple[0]
		toSquare_c = toTuple[1]
		fromPiece = board[fromSquare_r][fromSquare_c]
		toPiece = board[toSquare_r][toSquare_c]

		#make the move, then test if 'color' is in check
		board[toSquare_r][toSquare_c] = fromPiece
		board[fromSquare_r][fromSquare_c] = 'e'

		retval = self.IsInCheck(board,color)

		#undo temporary move
		board[toSquare_r][toSquare_c] = toPiece
		board[fromSquare_r][fromSquare_c] = fromPiece

		return retval

	def IsInCheck(self,board,color):
		#check if 'color' is in check
		#scan through squares for all enemy pieces; if there IsLegalMove to color's king, then return True.
		if color == "negro":
			myColor = 'b'
			enemyColor = 'w'
			enemyColorFull = 'blanco'
		else:
			myColor = 'w'
			enemyColor = 'b'
			enemyColorFull = 'negro'

		kingTuple = (0,0)
		#First, get current player's king location
		for row in range(7):
			for col in range(7):
				piece = board[row][col]
				if 'K' in piece and myColor in piece:
					kingTuple = (row,col)

		#Check if any of enemy player's pieces has a legal move to current player's king
		for row in range(7):
			for col in range(7):
				piece = board[row][col]
				if enemyColor in piece:
					if self.IsLegalMove(board,enemyColorFull,(row,col),kingTuple,0,0):
						return True
		return False

	def IsClearPath(self,board,fromTuple,toTuple):
		#Return true if there is nothing in a straight line between fromTuple and toTuple, non-inclusive
		#Direction could be +/- vertical, +/- horizontal, +/- diagonal
		fromSquare_r = fromTuple[0]
		fromSquare_c = fromTuple[1]
		toSquare_r = toTuple[0]
		toSquare_c = toTuple[1]
		fromPiece = board[fromSquare_r][fromSquare_c]

		if abs(fromSquare_r - toSquare_r) <= 1 and abs(fromSquare_c - toSquare_c) <= 1:
			#The base case: just one square apart
			return True
		else:
			if toSquare_r > fromSquare_r and toSquare_c == fromSquare_c:
				#vertical +
				newTuple = (fromSquare_r+1,fromSquare_c)
			elif toSquare_r < fromSquare_r and toSquare_c == fromSquare_c:
				#vertical -
				newTuple = (fromSquare_r-1,fromSquare_c)
			elif toSquare_r == fromSquare_r and toSquare_c > fromSquare_c:
				#horizontal +
				newTuple = (fromSquare_r,fromSquare_c+1)
			elif toSquare_r == fromSquare_r and toSquare_c < fromSquare_c:
				#horizontal -
				newTuple = (fromSquare_r,fromSquare_c-1)
			elif toSquare_r > fromSquare_r and toSquare_c > fromSquare_c:
				#diagonal "SE"
				newTuple = (fromSquare_r+1,fromSquare_c+1)
			elif toSquare_r > fromSquare_r and toSquare_c < fromSquare_c:
				#diagonal "SW"
				newTuple = (fromSquare_r+1,fromSquare_c-1)
			elif toSquare_r < fromSquare_r and toSquare_c > fromSquare_c:
				#diagonal "NE"
				newTuple = (fromSquare_r-1,fromSquare_c+1)
			elif toSquare_r < fromSquare_r and toSquare_c < fromSquare_c:
				#diagonal "NW"
				newTuple = (fromSquare_r-1,fromSquare_c-1)

		if board[newTuple[0]][newTuple[1]] != 'e':
			return False
		else:
			return self.IsClearPath(board,newTuple,toTuple)

if __name__ == "__main__":
	from ChessBoard import ChessBoard
	cb = ChessBoard()
	rules = ChessRules()
	print rules.IsCheckmate(cb.GetState(),"blanco",1,0)
	print rules.IsClearPath(cb.GetState(),(0,0),(5,5))
	print rules.IsClearPath(cb.GetState(),(1,1),(5,5))