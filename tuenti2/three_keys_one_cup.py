#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
from PIL import Image

def firstKey():
  """
  strings three_keys_one_cup.png | grep --color -E ^[0-9a-fA-F]{32}
  """
  pass

def secondKey():
  im = Image.open('three_keys_one_cup.png')
  data = list(im.getdata())[:128]
  bits = ''.join([str(d[0] % 2) + str(d[1] % 2) + str(d[2] % 2)
      for d in data])
  key = []
  for n in xrange(32):
    key.append(chr(int(bits[8 * n: 8 * (n + 1)], 2)))
  print ''.join(key)

def thirdKey():
  """
  Just point your favorite QR decoder to the QR on the right.
  """
  pass

keys = ['a541714a17804ac281e6ddda5b707952'
    ,   '62cd275989e78ee56a81f0265a87562e'
    ,   'ed8ce15da9b7b5e2ee70634cc235e363']

def main():
  keys.append((l.strip() for l in  sys.stdin).next())
  print ''.join(map(lambda n: hex(n)[2:], 
    [sum([int(x, 16) for x in y]) % 16 for y in zip(*keys)]))

if __name__ == '__main__':
  main()

