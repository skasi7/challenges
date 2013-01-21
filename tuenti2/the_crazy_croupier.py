#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import fractions

def simpleOne(N, L):
  original = range(N)
  cards = range(N)
  rounds = 0
  while True:
    firstStack = cards[:L]
    secondStack = cards[L:]
    cards = []
    while firstStack and secondStack:
      cards.append(firstStack.pop())
      cards.append(secondStack.pop())
    cards.extend(reversed(firstStack))
    cards.extend(reversed(secondStack))
    rounds += 1
    if cards == original:
      break
  return rounds

"""
for N in xrange(10):
  results = [(L, N - L, 2 * L - N, simpleOne(N, L)) for L in xrange(N + 1)]
  print results
sys.exit(-1)

for N in xrange(31):
  results = [simpleOne(N, L) for L in xrange(N + 1)]
  print 'N =', ''.join(['%4d' % N for _ in xrange(N + 1)])
  print 'L =', ''.join(['%4d' % L for L in xrange(N + 1)])
  print 'K =', ''.join(['%4d' % min(L, N - L) for L in xrange(N + 1)])
  print 'R =', ''.join(['%4d' % r for r in results])
  print ''.join(['%4d' % r for r in results])
sys.exit(-1)
"""

def lcm(l):
  return reduce(lambda a, b: a * b / fractions.gcd(a, b), l, 1)

def shortOneAux(N, L, i):
  if i < L + 1:
    return 2 * (L - i) + 1
  elif i < N - L + 1:
    return N - (i - (L + 1))
  else:
    return 2 * (N - i + 1)

def longOneAux(N, L, i):
  if i < 2 * L - N + 1:
    return N - i + 1
  elif i < L + 1:
    return 2 * (L - i) + 1
  else:
    return 2 * (N - i + 1)

def compute(N, L):
  if L < N - L:
    f = shortOneAux
    cards = set(range(1, 2 * L - 2) + range(N - L + 2, N + 1))
  else:
    f = longOneAux
    cards = set(range(1, 2 * (N - L)) + range(N - 2 * (N - L) + 1, N + 1))

  lengths = [2]
  while cards:
    start = cards.pop()
    current = f(N, L, start)
    pack = set([current])
    while current != start:
      current = f(N, L, current)
      pack.add(current)
    lengths.append(len(pack))
    cards = cards - pack

  return lcm(lengths)

def main():
  lines = (line for line in sys.stdin)
  cases = int(lines.next())
  for testcase in xrange(cases):
    N, L = map(int, lines.next().split())
    print 'Case #%d: %d' % (testcase + 1, compute(N, L))

if __name__ == '__main__':
  main()

