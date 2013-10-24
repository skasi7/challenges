#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def challenge():
  getline() # First comment
  dict_filename = getline()
  getline() # Second comment
  N = int(getline())
  getline() # Third comment
  words = list()
  for _ in xrange(N):
    words.append(getline())

  # Preprocessing
  dictionary = dict()
  for word in open(dict_filename, 'rb'):
    word = word.rstrip()
    key = ''.join(sorted(word))
    dictionary.setdefault(key, list()).append(word)

  # Processing
  for word in words:
    key = ''.join(sorted(word))
    suggestions = dictionary.get(key)
    if suggestions is not None:
      suggestions = suggestions[:]
      suggestions.remove(word)
    print word, '->%s%s' % (
        suggestions and ' ' or '',
        ' '.join(sorted(suggestions)))

# Main entry point
if __name__ == '__main__':
  challenge()

