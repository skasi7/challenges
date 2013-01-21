#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys

def compute(line):
  data = map(int, line)
  result = []
  byte = []
  while len(data) >= 7:
    d, data = data[:7], data[7:]
    p1 = d[0] + d[2] + d[4] + d[6]
    p2 = d[1] + d[2] + d[5] + d[6]
    p3 = d[3] + d[4] + d[5] + d[6]
    err = sum([(p1 % 2) and 1 or 0,
      (p2 % 2) and 2 or 0,
      (p3 % 2) and 4 or 0])
    d[err - 1] = (d[err - 1] + 1) % 2
    byte.extend([d[2], d[4], d[5], d[6]])
    if len(byte) == 8:
      byteValue = int(''.join(map(str, byte)), 2)
      result.append(byteValue)
      byte = []

  if data or min(result) < 32 or max(result) > 127:
    return 'Error!'

  return ''.join(map(chr, result))

def main():
  lines = (line for line in sys.stdin)
  for line in lines:
    print compute(line.strip())

if __name__ == '__main__':
  main()
