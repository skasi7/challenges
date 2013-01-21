#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# Special thanks to safull by the tips

import sys

operators = {
    'mirror': lambda s: s.append(-s.pop()),
    '$': lambda s: s.append(s.pop(-2) - s.pop()),
    '&': lambda s: s.append(s.pop(-2) / s.pop()),
    '@': lambda s: s.append(s.pop() + s.pop()),
    'dance': lambda s: s.extend([s.pop(), s.pop()]),
    'conquer': lambda s: s.append(s.pop(-2) % s.pop()),
    'fire': lambda s: s.pop(),
    'breadandfish': lambda s: s.append(s[-1]),
    '#': lambda s: s.append(s.pop() * s.pop())
  }

def compute(tokens):
  stack = []

  for token in tokens:
    if token == '.':
      return stack.pop()
    elif token in operators:
      operators[token](stack)
    else:
      stack.append(int(token))

def main():
  for line in sys.stdin:
    print compute(line.strip().split())

if __name__ == '__main__':
  main()

