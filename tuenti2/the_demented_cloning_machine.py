#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import hashlib

def compute(initialQueue, transformations):
  reference = transformations.pop()
  while transformations:
    transformation = transformations.pop()
    for k, v in transformation.iteritems():
      transformation[k] = ''.join([reference.get(c, c) for c in v])
    for k, v in reference.iteritems():
      if k not in transformation:
        transformation[k] = v
    reference = transformation

  m = hashlib.md5()

  for c in initialQueue:
    m.update(reference.get(c, c))

  return m.hexdigest()

def main():
  lines = (line for line in sys.stdin)
  initialQueue = lines.next().strip()
  transformations = []
  for line in lines:
    transformationSerie = {}
    for transformation in line.strip().split(','):
      orig, dest = transformation.split('=>')
      transformationSerie[orig] = dest
    transformations.append(transformationSerie)

  print compute(initialQueue, transformations)

if __name__ == '__main__':
  main()

