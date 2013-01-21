#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

__pychecker__ = 'no-callinit no-classattr'


# External imports
import cmd
import optparse
import readline
import sys
import time

# Internal imports (if any)
import problemset

class Problem_Controller(cmd.Cmd):
  
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.prompt = 'Euler> '

  # TODO: complete_* de los comandos para el autocompletado

  def __tokenize(self
      , line
      , mandargs=1
      , optargs=0):
    tokens = line.split()
    assert len(tokens) >= mandargs and len(tokens) <= mandargs + optargs \
        , "el comando espera %d-%d argumentos, %d dados" % (mandargs
            , mandargs + optargs
            , len(tokens))
    while len(tokens) < mandargs + optargs:
      tokens.append(None)
    return (len(tokens) == 1) and tokens[0] or tokens

  def __solve_problem(self
      , problem_num):

    try: 
      method = getattr(problemset, 'problem%04d' % problem_num)
    except AttributeError:
      print 'No solution available (yet)!'
      return

    print 'Euler problem #%s:' % problem_num, method.__doc__
    
    t1 = time.time()
    
    print 'Solution:', method()

    lapse = time.time() - t1
    for unit in ('s'
        , 'ms'
        , 'us'
        , 'ns'):
      if lapse > 1 or unit == 'ns':
        lapse = '%.3f %s' % (lapse
            , unit)
        break
      lapse *= 1000
    print 'Time: %s' % lapse

  def do_solve_problem(self
      , line):
    """Resuelve el problema Euler que se indique"""
    problem_num = int(self.__tokenize(line))
    self.__solve_problem(problem_num)

  def do_EOF(self
      , line):
    """Sale de la aplicacion de control
uso: Ctrl-D"""
    line = (line, ) # silence pychecker
    return True

  def do_help(self
      , line):
    """Muestra esta ayuda en linea"""
    cmd.Cmd.do_help(self
        , line)

  def onecmd(self
      , line):
    try:
      return cmd.Cmd.onecmd(self
          , line)
    except AssertionError, msg:
      print 'Error: %s' % msg

  def emptyline(self):
    pass

  def default(self
      , line):
    print 'Error: Comando no reconocido: %s' % line


def main():
  pr_controller = Problem_Controller()

  if options.problem:
    pr_controller.do_solve_problem('%d' % options.problem)
    pr_controller.do_EOF('')
  else:
    try:
      pr_controller.cmdloop()
    except KeyboardInterrupt:
      sys.exit(1)


if __name__ == '__main__':
  parser = optparse.OptionParser(usage="uso: %prog [options]")
  parser.add_option('-p'
    , '--problem'
    , dest='problem'
    , type='int'
    , default=None
    , help='problema a resolver')
  (options, args) = parser.parse_args()

  main()

  sys.exit(0)

