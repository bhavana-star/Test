import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("type", help="type of the piece", type=str)
parser.add_argument("position", help="position of the piece", type=str)
args = parser.parse_args()
piece = args.type
col = args.position[0]
row = args.position[1]

def knightMoves(col,row):
	moves = []
	if (int(row) + 1) < 9:
		moves.append(cp(col,int(2))+str(abs(int(row) + 1)))
		moves.append(cp(col,-int(2))+str(abs(int(row) + 1)))
	if (int(row) + 2) < 9:
		moves.append(cp(col,int(1))+str(abs(int(row) + 2)))
		moves.append(cp(col,-int(1))+str(abs(int(row) + 2)))
	if (int(row) - 1) > 0:
		moves.append(cp(col,int(2))+str(abs(int(row) - 1)))
		moves.append(cp(col,-int(2))+str(abs(int(row) - 1)))
	if (int(row) - 2) > 0:
		moves.append(cp(col,int(1))+str(abs(int(row) - 2)))
		moves.append(cp(col,-int(1))+str(abs(int(row) - 2)))
	return moves

def cp(col, posMove):
	return chr(ord(col) + int(posMove))


def rookMoves(col,row):
	moves = []
	rows = filter(lambda x: x,range(1,9))
	list1 = [col+str(x) for x in rows if x!=int(row)]
	cols = list(map(chr, range(97, 105)))
	list2 = [str(x)+str(row) for x in cols if x!=col]
	moves = list1 + list2
	return moves

def bishopMoves(col,row):
	moves = []
	deci_value = ord(col)
	val1 = deci_value
	count1 = 0
	while val1 - 97 > 0:
		val1 = val1 - 1
		count1 = count1 + 1
		if (int(row) + int(count1)) < 9:
			moves.append(chr(val1)+str(abs(int(row) + int(count1))))
		if (int(row) - int(count1)) > 0:
			moves.append(chr(val1)+str(abs(int(row) - int(count1))))

	val2 = deci_value
	count2 = 0
	while 104 - val2 > 0:
		val2 = val2 + 1
		count2 = count2 + 1
		if (int(row) + int(count2)) < 9:
			moves.append(chr(val2)+str(abs(int(row) + int(count2))))
		if (int(row) - int(count2)) > 0:
			moves.append(chr(val2)+str(abs(int(row) - int(count2))))
			
	return moves


if piece == "knight":
	knightSteps = knightMoves(col,row)
	print("\""+', '.join(knightSteps)+"\"")

if piece == "rook":
	rookSteps = rookMoves(col,row)
	print("\""+', '.join(rookSteps)+"\"")

if piece == "bishop":
	bishopSteps = bishopMoves(col,row)
	print("\""+', '.join(bishopSteps)+"\"")

if piece == "queen":
	bishopSteps = bishopMoves(col,row)
	rookSteps = rookMoves(col,row)
	queenSteps = bishopSteps + rookSteps
	print("\""+', '.join(queenSteps)+"\"")


