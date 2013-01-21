#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/toolbox.py $
# $Author: SkAsI.7 $
# $Id: toolbox.py 51 2011-05-03 14:48:12Z SkAsI.7 $
# $Revision: 51 $


# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
from itertools import count, islice, ifilter, tee
from itertools import starmap, izip, takewhile, groupby
from itertools import chain, cycle
from math import sqrt
import operator

# Internal imports (if any)


# Auxiliar functions

def next(it, default):
  """next built-in function from python2.6"""
  try:
    return it.next()
  except StopIteration:
    return default

def first(it):
  """Returns the first element from it"""
  return it.next()

def last(it):
  """Returns the last element from it"""
  for elem in it: pass
  return elem

def index(n, it):
  """Returns the nth element from it"""
  return islice(it, n, n + 1).next()

def take(n, it):
  """Take n elements from it"""
  return islice(it, n)

def drop(n, it):
  """Drop n elements from iterable and return the rest"""
  return islice(it, n, None)

def take_every(n, it):
  """Take an element from it every n elements"""
  return islice(it, 0, None, n)

def groups(it, n, step=1):
  """Returns groups of n elements taken from the iterable in step steps"""
  it_list = tee(it, n)
  one_step_it = izip(*(starmap(drop, enumerate(it_list))))
  return take_every(step, one_step_it)

def compact(it):
  """remove None elements of the iterator"""
  return ifilter(bool, it)

def cartesian_product(*args, **kwargs):
  """itertools.product function from python2.6"""
  pools = map(tuple, args) * kwargs.get('repeat', 1)
  return (tuple(x) for x in reduce(lambda r, p: [x + [y]
        for x in r
        for y in p], pools, [[]]))

def permutations(it, r=None):
  """itertools.permutations function from python2.6"""
  pool = tuple(it)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = range(n)
  cycles = range(n, n - r, -1)
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i + 1:] + indices[i:i + 1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return

def ilen(it):
  """Returns the number of elements exhausting it"""
  return sum(1 for _ in it)

def ireduce(func, it, init=None):
  """Returns partial reduce() results using iterators"""
  it = iter(it)
  cur = init or it.next()
  yield cur
  for x in it:
    cur = func(cur, x)
    yield cur

def iunique(it):
  """Returns unique elements from it (order preserved)"""
  # Not functional, but fast
  seen = set()
  for x in it:
    if x not in seen:
      seen.add(x)
      yield x

def product(nums):
  """Returns the product of nums"""
  return reduce(operator.mul, nums, 1)

def get_cardinal_name(n):
  """Get cardinal name for number (0 to 1 million)"""
  numbers = {
      0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
      6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
      11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
      15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
      19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
      50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
  if n > 999:
    return '%s thousand%s' % (numbers[n / 1000],
        (' and %s' % get_cardinal_name(n % 1000)) if n % 1000 else '')
  if n > 99:
    return '%s hundred%s' % (numbers[n / 100],
        (' and %s' % get_cardinal_name(n % 100)) if n % 100 else '')
  if n > 19:
    return '%s%s' % (numbers[n / 10 * 10],
        ('-%s' % numbers[n % 10]) if n % 10 else '')
  return numbers[n]

def flatten(ls):
  """Flatten a list of lists"""
  return (b for a in ls for b in a)

def compose(f, g):
  """Compose two functions -> compose(f, g)(x) -> f(g(x))"""
  def _wrapper(*args, **kwargs):
    return f(g(*args, **kwargs))
  return _wrapper

# Generators

def fibonacci():
  """Generate fibonacci serie"""
  return (b for _, b in ireduce(lambda (a, b), _: (b, a + b),
    count(), (0, 1)))

def primes(start=2, memoized=False):
  """Generate the prime numbers from start"""
  return ifilter(memoize(is_prime) if memoized else is_prime, count(start))

def pythagorean_triplets():
  """Generate the pythagorean triplets in perimeter ascending order"""
  primitive_triples = [
      (3, 4, 5),    (5, 12, 13),  (8, 15, 17),  (7, 24, 25),
      (20, 21, 29), (12, 35, 37), (9, 40, 41),  (28, 45, 53),
      (11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73),
      (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)
    ]
  for i, triplet in enumerate(cycle(primitive_triples)):
    factor = (i / 16) + 1
    yield map(lambda x: x * factor, triplet)

def accsum(it):
  """Yield accumulated sums of iterable: accsum(count(1)) -> 1,3,6,10,..."""
  return drop(1, ireduce(operator.add, it, 0))

# Boolean math functions

def is_prime(n):
  """Returns True if n is prime (1 is not considered prime)"""
  if n < 3:
    return n == 2
  if n % 2 == 0:
    return False
  return not any((n % x == 0 for x in xrange(3, int(sqrt(n)) + 1, 2)))

def is_palindromic(n, base=10):
  """Returns True is n is palindromic"""
  digits = digits_from_num(n, base)
  return digits == list(reversed(digits))

def is_pandigital(digits, through=range(1, 10)):
  """Returns True if digits are pandigital"""
  return sorted(digits) == through

def is_amicable_number(n):
  """Returns True if n is amicable (The sum of proper divisors of the sum of proper divisors is itself)"""
  m = sum(proper_divisors(n))
  return n != m and sum(proper_divisors(m)) == n

def is_perfect(n):
  """Returns 0 if n is perfect, 1 if is abundant and -1 if is deficient"""
  return cmp(sum(proper_divisors(n)), n)

def is_triangle(n):
  """Returns True if n is a triangle number, False otherwise"""
  x = sqrt(1 + 8 * n)
  if x != int(x):
    return False
  return (int(x) - 1) % 2 == 0

def is_pentagonal(n):
  """Returns True if n is a pentagonal number, False otherwise"""
  x = sqrt(1 + 24 * n)
  if x != int(x):
    return False
  return (int(x) + 1) % 6 == 0

def is_integer(x, epsilon=1e-6):
  """Return True if the float x "seems" an integer"""
  return (abs(round(x) - x) < epsilon)

# List math functions

def prime_factors(n, start=2):
  """Returns all prime factors (ordered) of n in a list"""

  # TODO: Non-recursive version
  factor = next((x for x in xrange(start, int(sqrt(n)) + 1)
    if n % x == 0), None)
  return ([factor] + prime_factors(n / factor, factor) if factor else [n])

def factorize(n):
  """Factorize n: factorize(12) -> (2, 2), (3, 1)"""
  return ((factor, ilen(fs)) for (factor, fs) in groupby(prime_factors(n)))

def divisors(n):
  """Returns all divisors of n: divisors(12) -> 1, 2, 3, 6, 12"""
  all_factors = [[f ** p for p in range(fp + 1)]
      for (f, fp) in factorize(n)]
  return (product(ns) for ns in cartesian_product(*all_factors))

def proper_divisors(n):
  """Returns all the proper divisors (divisors under n)"""
  return (divisor for divisor in divisors(n) if divisor < n)

def digits_from_num_r(n, base=10):
  """Returns all digits from n in base in a list"""
  # Optimization for base 10
  if base == 10:
    return map(int, str(n))

  def recursive(n, base, current):
    if n < base:
      return [n] + current
    return recursive(n / base, base, [n % base] + current)
  return recursive(n, base, [])

def digits_from_num(n, base=10):
  """Returns all digits from n in base in a list"""
  # Optimization for base 10
  if base == 10:
    return map(int, str(n))

  digits = list()
  while n:
    digits.insert(0, n % base)
    n /= base
  return digits

def num_from_digits(digits, base=10):
  """Returns the value of the digits in base"""
  return sum(digit * base ** n for n, digit
      in enumerate(reversed(list(digits))))

# Single-value math functions

def greatest_common_divisor(a, b):
  """Returns the greatest_common_divisor of a and b"""
  return greatest_common_divisor(b, a % b) if b else a

def least_common_multiple(a, b):
  """Returns the least common multiple of a and b"""
  return (a * b) / greatest_common_divisor(a, b)

def factorial(n):
  """Returns n!"""
  return reduce(operator.mul, range(1, n + 1), 1)

def triangle(n):
  """Returns the nth triangle number"""
  return n * (n + 1) / 2

def pentagonal(n):
  """Returns the nth pentagonal number"""
  return n * (3 * n - 1) / 2

def hexagonal(n):
  """Returns the nth hexagonal number"""
  return n * (2 * n - 1)

# Decorators

def memoize(f, maxcache=None, cache={}):
  """Decorator to keep a cache of input/output for a given function"""
  cachelen = [0]
  def g(*args, **kwargs):
    key = (f, tuple(args), frozenset(kwargs.items()))
    if maxcache is not None and cachelen[0] > maxcache:
      return f(*args, **kwargs)
    if key not in cache:
      cache[key] = f(*args, **kwargs)
      cachelen[0] += 1
    return cache[key]
  return g

class persistent(object):

  def __init__(self, it):
    self._it = it
      
  def __getitem__(self, x):
    self._it, temp = tee(self._it)
    if type(x) is slice:
      return list(islice(temp, x.start, x.stop, x.step))
    else:
      return islice(temp, x, x + 1).next()
      
  def __iter__(self):
    self._it, temp = tee(self._it)
    return temp

