#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import string

alphabet = ' 1abc2def3ghi4jkl5mno6pqrs7tuv8wxyz90'
keysRepetitions = [2, 4, 4, 4, 4, 4, 5, 4, 5, 1]
keys = sum([[i] * x for i, x in enumerate(keysRepetitions)], [])

mayusKey = 10

distances = [
    [500, 200, 400, 300, 350, 550, 600, 650, 700, 950, 1000],
    [500, 200, 350, 300, 350, 650, 600, 650, 900, 950],
    [500, 550, 350, 300, 700, 650, 600, 950, 900],
    [500, 200, 400, 300, 350, 550, 650, 700],
    [500, 200, 350, 300, 350, 600, 650],
    [500, 550, 350, 300, 650, 600],
    [500, 200, 400, 350, 550],
    [500, 200, 300, 350],
    [500, 350, 300],
    [500, 200]
  ]

def computeChange(k, i):
  k, i = min(k, i), max(k, i)
  return distances[k][i - k]

def compute(line):
  totalTime = 0

  key = 9
  lowercase = True
  for c in line:
    # Compute change of case (if any)
    if c in string.ascii_letters and c.islower() ^ lowercase:
      lowercase = not lowercase
      totalTime += computeChange(key, mayusKey) + 100
      key = mayusKey

    # Compute finger movement
    lkey = keys[alphabet.find(c.lower())]
    totalTime += computeChange(key, lkey)
    key = lkey

    # Compute key presses
    repetitions = alphabet.find(c.lower()) - keys.index(lkey) + 1
    totalTime += repetitions * 100
    
  print totalTime

def main():
  lines = (line for line in sys.stdin)
  cases = int(lines.next())
  for _ in xrange(cases):
    case = lines.next()
    compute(case[:-1])

if __name__ == '__main__':
  main()
