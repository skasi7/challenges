#!C:\Python27\python.exe
#-*- coding: utf-8 -*-

import sys

scores = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	, [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1,
		 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]))

def precomputeAux(node, letterList, word):
	c = letterList[0]
	newNode = node[1].setdefault(c, (node[0] + scores[c], {}, None))
	if len(letterList) == 1:
		currentWord = newNode[2]
		if currentWord is None or word < currentWord:
			node[1][c] = (newNode[0], newNode[1], word)
	else:
		precomputeAux(newNode, letterList[1:], word)

def precompute(tree):
	for word in (word.strip()
			for word in open('descrambler_wordlist.txt')):
		letterList = list(word)
		letterList.sort()

		precomputeAux(tree, letterList, word)


def computeAux(node, letterList, boardUsed):
	if not letterList:
		return (0, '')
	# If there's no board letters and the word doesn't contain one...
	if not boardUsed and sum([s for c, s in letterList]) == 0:
		return (0, '')

	c, ctype = letterList[0]
	newNode = node[1].get(c)
	if newNode is not None and newNode[2] is not None:
		# The current word
		results = [(-newNode[0], newNode[2])]
	else:
		results = []
		
	if newNode is None:
		# Avoid all the c's from letterList
		letterList = [l for l in letterList if l[0] != c]
		results.append(computeAux(node, letterList, boardUsed))
	else:
		# Try like c not present
		results.append(computeAux(node, letterList[1:], boardUsed))
		# Continue looking taking into account what kind of letter was looked
		if ctype == 1:
			letterList = [l for l in letterList[1:] if l[1] != 1]
			boardUsed = True
		else:
			letterList = letterList[1:]
		results.append(computeAux(newNode, letterList, boardUsed))

	# TODO: return real word instead of scramble representation
	results.sort(reverse=True)
	return results[-1]

def compute(rack, board, tree):
	# Real calculation
	letterList = zip(rack, [0] * len(rack)) \
			+ zip(board, [1] * len(board))
	letterList.sort()

	solution = computeAux(tree, letterList, False)
	print '%s %d' % (solution[1], -solution[0])

def main():
	# Precalculation
	tree = (0, {})
	precompute(tree)

	lines = (line for line in sys.stdin)
	cases = int(lines.next())
	for _ in xrange(cases):
		rack, board = lines.next().strip().split()
		compute(rack, board, tree)

if __name__ == '__main__':
	main()
