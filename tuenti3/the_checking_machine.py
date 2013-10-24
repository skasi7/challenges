#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import md5
import sys

# Internal imports (if any)

class MD5Sum(object):

  def __init__(self, md5sum):
    object.__init__(self)
    self.__md5sum = md5sum
    self.__buffer = list()

  def update(self, buf):
    print buf
    self.__buffer += buf
    if len(self.__buffer) >= 1024:
      self.__md5sum.update(''.join(self.__buffer[:1024]))
      self.__buffer = self.__buffer[1024:]

  def hexdigest(self):
    if self.__buffer:
      self.__md5sum.update(''.join(self.__buffer))
    return self.__md5sum.hexdigest()

def process(md5sum, msg):
  processed = 0
  word = list()
  number = list()
  while msg:
    c, msg = msg[0], msg[1:]
    processed += 1
    if 'a' <= c <= 'z':
      word.append(c)
    elif c in ('[', ']'):
      if c == '[':
        number = int(''.join(number))
        for _ in xrange(number):
          subprocessed = process(md5sum, msg)
        number = list()
        msg = msg[subprocessed:]
        processed += subprocessed
      else:
        if word:
          md5sum.update(word)
          word = list()
        return processed
    else:
      if word:
        md5sum.update(word)
        word = list()
      number.append(c)

  if word:
    md5sum.update(word)

# Main entry point
if __name__ == '__main__':
  for line in sys.stdin:
    md5sum = MD5Sum(md5.new())
    process(md5sum, line.strip())
    print md5sum.hexdigest()

