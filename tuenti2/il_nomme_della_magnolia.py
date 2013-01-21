#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import pickle
import multiprocessing

def precompute(currentFile):
  print currentFile
  wordDict = {}
  fd = open('il_nomme_della_magnolia/%04d' % currentFile)
  for currentLine, line in enumerate(fd):
    for currentWord, word in enumerate(line.split()):
      word = word.lower()
      wordDict[word] = wordDict.get(word, 0) + 1

  pickle.dump(wordDict,
      open('il_nomme_della_magnolia/%04d.dat' % currentFile, 'wb'))

# Parallel processing of file indexes
"""
pool = multiprocessing.Pool()
result = pool.map_async(precompute, xrange(1, 801))
result.get()
"""

def compute(words, results):
  for currentFile in xrange(1, 801):
    wordDict = pickle.load(
        open('il_nomme_della_magnolia/%04d.dat' % currentFile, 'rb'))

    newWords = {}
    for word, occurrences in words.iteritems():
      if word in wordDict:
        fileOccurrences = wordDict[word]
        if occurrences[0][0] <= fileOccurrences:
          # There's something of interest in this file
          break
        else:
          newWords[word] = [(n - fileOccurrences, m) for n, m in occurrences]
    else:
      # There's nothing of interest in this whole file
      words.update(newWords)
      continue

    fd = open('il_nomme_della_magnolia/%04d' % currentFile)
    for currentLine, line in enumerate(fd):
      for currentWord, word in enumerate(line.split()):
        word = word.lower()
        if word in words:
          newElement = []
          for occurrences, i in words[word]:
            occurrences -= 1
            if not occurrences:
              results[i] = '%d-%d-%d' % \
                  (currentFile, currentLine + 1, currentWord + 1)
            else:
              newElement.append((occurrences, i))
          if newElement:
            words[word] = newElement
          else:
            del words[word]
          if not words:
            return results

def main():
  lines = (line for line in sys.stdin)
  cases = int(lines.next())

  words = {}
  for i in xrange(cases):
    word, occurrences = lines.next().strip().split()
    word = word.lower()
    occurrences = int(occurrences)
    if word in words:
      words[word].append((occurrences, i))
    else:
      words[word] = [(occurrences, i)]

  for occurrences in words.itervalues():
    occurrences.sort()

  results = [0] * cases
  compute(words, results)
  for result in results:
    print result

if __name__ == '__main__':
  main()

