#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def topologicalSort(letters, partialOrderings, branch=None):
  L = []
  S = []
  for i in xrange(len(letters)):
    if sum([l[i] for l in partialOrderings]) == 0:
      S.append(i)

  while S:
    if len(S) > 1: # multiple choices
      return None
    n = S.pop()
    L.append(n)
    for m in [i for i, x in enumerate(partialOrderings[n]) if x]:
      partialOrderings[n][m] = 0
      if sum([l[m] for l in partialOrderings]) == 0:
        S.append(m)

  return L

def challenge():
  script = getline()

  scene = list()
  scenes = list()
  for c in script:
    if c in ('.', '<', '>') and scene:
      scenes.append(''.join(scene))
      scene = list()
    scene += c
  else:
    scenes.append(''.join(scene))

  scenes_list = list(set([s[1:] for s in scenes]))

  partialOrderings = []
  for _ in scenes_list:
    partialOrderings.append([0] * len(scenes_list))
  
  prev_scene = None
  for scene in scenes:
    scene_idx = scenes_list.index(scene[1:])
    if scene[0] == '<':
      partialOrderings[scene_idx][prev_scene] = 1
    elif scene[0] == '>':
      partialOrderings[prev_scene][scene_idx] = 1
    else:
      if prev_scene is not None:
        partialOrderings[prev_scene][scene_idx] = 1
      prev_scene = scene_idx
  
  L = topologicalSort(scenes_list, partialOrderings)

  if L is None:
    print 'valid'
  elif len(L) != len(partialOrderings):
    print 'invalid'
  else:
    print ','.join([scenes_list[i] for i in L])

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    challenge()

