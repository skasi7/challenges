#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import math

def compute(w, h, ct, text):
  # width and height in pix
  words = map(len, text.split())

  totalChars = len(text)
  minFontSize = min(h, w / totalChars)

  longestWord = max(words)
  maxFontSize = w / longestWord

  charsPerLine = lines = 0
  for fs in xrange(maxFontSize, minFontSize - 1, -1):
    if charsPerLine == w / fs and lines == h / fs:
      continue # Don't repeat yourself

    charsPerLine = w / fs
    lines = h / fs

    lineStart = True
    charsLeft = charsPerLine + 1
    l = lines
    for word in words:
      charsLeft -= word + 1 # +1 for space

      if charsLeft < 0:
        # Close the line
        l -= 1
        if not l:
          break # Too bad, this fs it's invalid

        charsLeft = charsPerLine - word
    else:
      break

  else:
    fs = 0

  # Non white chars * font size ^ 2 / 2 / ct
  return int(math.ceil(1.0 \
      * (len(text) - text.count(' ')) \
      * fs * fs / 2 / ct))

def main():
  lines = (line for line in sys.stdin)
  cases = int(lines.next())
  for testcase in xrange(cases):
    w, h, ct = map(int, lines.next().split())
    text = lines.next().strip()
    print 'Case #%d: %d' % (testcase + 1, compute(w * ct, h * ct, ct, text))

if __name__ == '__main__':
  main()

