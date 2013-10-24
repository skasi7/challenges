#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

# Code used to seek for the missing_numbers inside the uncompressed file
"""
import struct
import ctypes

if __name__ == '__main__':
  bitset = (ctypes.c_ubyte * (2**31 / 8))()

  print 'Done allocating memory'

  fd = open('/data/integers', 'rb')
  chunk_size = 8 * 1024
  buf = fd.read(chunk_size)
  fmt = 'I' * (chunk_size / 4)
  while len(buf) == chunk_size:
    integers = struct.unpack(fmt, buf)
    for i in integers:
      bitset[i / 8] |= 1 << (i % 8)
    buf = fd.read(chunk_size)
  integers = struct.unpack('I' * (len(buf) / 4), buf)
  for i in integers:
    bitset[i / 8] |= 1 << (i % 8)

  print 'Done processing file'

  fd = open('/data/output', 'wb')
  for position, i in enumerate(bitset):
    if i == 255:
      continue
    for j in xrange(8):
      if not (i & (1 << j)):
        print >> fd, 'missing', position * 8 + j

  print 'Done. Have a good day!'
"""

# This list was compiled with the /data/output file and some vim fu.
missing_numbers = [7303, 8243, 9854, 12009, 12793, 14346, 14680, 15093, 17857, 19375, 20084, 22525, 23054, 23250, 30197, 36318, 39334, 40018, 48871, 50654, 50721, 54592, 59393, 61063, 63138, 63241, 64549, 66259, 69103, 76165, 76685, 81278, 82333, 83089, 84011, 85250, 88429, 90254, 90271, 90981, 91165, 93661, 94654, 99088, 99146, 99612, 2147386534, 2147387515, 2147390868, 2147393636, 2147394767, 2147394776, 2147399790, 2147404278, 2147410474, 2147411181, 2147411772, 2147414329, 2147414440, 2147415261, 2147415351, 2147416362, 2147416780, 2147416956, 2147418296, 2147419403, 2147419606, 2147421475, 2147421911, 2147424275, 2147424781, 2147425007, 2147425958, 2147427008, 2147429783, 2147430753, 2147434866, 2147436265, 2147439441, 2147442423, 2147443250, 2147454548, 2147455603, 2147457507, 2147463138, 2147465967, 2147466563, 2147466673, 2147468436, 2147470025, 2147470723, 2147470869, 2147471405, 2147474036, 2147474185, 2147476664, 2147478255, 2147478824, 2147480866, 2147480904]

def getline():
  return sys.stdin.next().rstrip()

def challenge():
  N = int(getline())
  print missing_numbers[N - 1]

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    challenge()

