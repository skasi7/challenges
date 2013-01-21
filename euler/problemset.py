#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

__pychecker__ = 'no-callinit no-classattr'

# External imports
import string

# Internal imports (if any)
from toolbox import *


def problem0001():
  """Add all the natural numbers below 1000 that are multiples of 3 or 5."""
  return sum(x for x in xrange(1, 1000) if x % 3 == 0 or x % 5 == 0)

def problem0002():
  """Find the sum of all the even-valued terms in the Fibonacci < 4 million."""
  even_fibonacci = (x for x in fibonacci() if x % 2)
  return sum(takewhile(lambda x: x < 4e6, even_fibonacci))

def problem0003():
  """Find the largest prime factor of a composite number."""
  return max(prime_factors(600851475143))

def problem0004():
  """Find the largest palindrome made from the product of two 3-digit numbers."""
  # A brute-force solution is a bit slow, let's try to simplify it a little bit:
  # xy = "abccba" = 100001a + 10010b + 1100c = 11 * (9091a + 910b + 100c)
  # So at least one of them must be multiple of 11.
  candidates = (x * y
      for x in xrange(110, 1000, 11)
      for y in xrange(x, 1000))
  return max(x for x in candidates if is_palindromic(x))

def problem0005():
  """What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?."""
  return reduce(least_common_multiple, range(1, 21))

def problem0006():
  """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
  sum_of_squares = sum(x * x for x in xrange(1, 101))
  square_of_sums = sum(xrange(1, 101)) ** 2
  return square_of_sums - sum_of_squares

def problem0007():
  """What is the 10001st prime number?."""
  return index(10000, primes())

def problem0008():
  """Find the greatest product of five consecutive digits in the 1000-digit number"""
  data = ''.join(open('problem0008.txt').read().strip().splitlines())
  digits = map(int, data)
  return max(product(nums) for nums in groups(digits, 5))
  
def problem0009():
  """There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."""
  candidates = ((a, b, 1000 - a - b)
      for a in xrange(1, 999)
      for b in xrange(a + 1, 999))
  return first(a * b * c for (a, b, c) in candidates
      if a * a + b * b == c * c)
  
def problem0010():
  """Find the sum of all the primes below two million."""
  return sum(takewhile(lambda x: x < 2e6, primes()))

def problem0011():
  """What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20x20 grid?"""
  grid = [map(int, line.split())
      for line in open('problem0011.txt').read().strip().splitlines()]
  def grid_get(x, y, nx, ny):
    return grid[x][y] if 0 <= x < nx and 0 <= y < ny else 0
  diffs = [(0, 1), (1, 0), (1, 1), (1, -1)]
  nx, ny = len(grid), len(grid[0])
  return max(product(grid_get(x + i * dx, y + i * dy, nx, ny)
    for i in range(4))
      for x in xrange(nx)
      for y in xrange(ny)
      for (dx, dy) in diffs)

def problem0012():
  """What is the value of the first triangle number to have over five hundred divisors?"""
  triangle_numbers = (triangle(n) for n in count(1))
  return first(tn for tn in triangle_numbers if ilen(divisors(tn)) > 500)

def problem0013():
  """Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""
  numbers = map(int, open('problem0013.txt').read().strip().splitlines())
  return int(str(sum(numbers))[:10])

def problem0014():
  """The following iterative sequence is defined for the set of positive integers: n -> n/2 (n is even), n -> 3n + 1 (n is odd). Which starting number, under one million, produces the longest chain?"""

  # TODO: Non-recursive version
  def collatz_function(n):
    return (3 * n + 1) if (n % 2) else (n / 2)
  @memoize
  def collatz_series_length(n):
    return (1 + collatz_series_length(collatz_function(n)) if n > 1 else 0)
  return max(xrange(1, int(1e6)), key=collatz_series_length)

def problem0015():
  """How many routes are there through a 20x20 grid?"""
  return factorial(2 * 20) / factorial(20) ** 2

def problem0016():
  """What is the sum of the digits of the number 2^1000?"""
  return sum(digits_from_num(2 ** 1000))

def problem0017():
  """If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?"""
  strings = (get_cardinal_name(n) for n in xrange(1, 1001))
  return ilen(c for c in flatten(strings) if c.isalpha())

def problem0018():
  """Find the maximum total from top to bottom of the triangle below:"""
  data = [map(int, line.split())
      for line in open('problem0018.txt').read().strip().splitlines()]
  return reduce(lambda r1, r2: [max(a) + b
    for a, b in izip(izip(r1[:-1], r1[1:]), r2)],
    reversed(data))[0]

def problem0019():
  """How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?"""
  def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
  def get_days_for_month(year, month):
    days = [31, 28 + (1 if is_leap_year(year) else 0), 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]
    return days[month - 1]
  return reduce(lambda x, y: (x[0] + (1 if x[1] % 7 == 0 else 0),
    x[1] + y),
    starmap(get_days_for_month, ((y, m)
      for y in xrange(1901, 2001)
      for m in xrange(1, 13))), (0, 0))[0]

def problem0020():
  """Find the sum of the digits in the number 100!"""
  return sum(digits_from_num(factorial(100)))

def problem0021():
  """Evaluate the sum of all the amicable numbers under 10000."""
  cache = dict((n, sum(proper_divisors(n))) for n in xrange(1, 10000))
  return sum(a for (a, b) in cache.iteritems() if a != b and cache.get(b, 0) == a)

def problem0022():
  """What is the total of all the name scores in the file?"""
  def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)
  data = sorted([name.replace('"', '')
      for name in open('problem0022.txt').read().strip().split(',')])
  return sum(name_score(name) * (i + 1) for i, name in enumerate(data))

def problem0023():
  """Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
  abundants = set(x for x in xrange(1, 28124) if is_perfect(x) == 1)
  return sum(x for x in xrange(1, 28124) if not any(((x - a) in abundants)
    for a in abundants))

def problem0024():
  """What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
  return num_from_digits(index(1e6 - 1, permutations(range(10))))

def problem0025():
  """What is the first term in the Fibonacci sequence to contain 1000 digits?"""
  return first(i for i, x in enumerate(fibonacci()) if x > 10 ** 999) + 1

def problem0026():
  """Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
  def manual_division(numerator, denominator):
    """Return (quotient, (remainder, cycle_length))"""
    def recursive(numerator, denominator, quotients, remainders):
      q, r = divmod(numerator, denominator)
      if r == 0:
        return (quotients + [q], 0)
      if r in remainders:
        return (quotients, len(remainders) - remainders.index(r))
      return recursive(10 * r, denominator, quotients + [q],
          remainders + [r])
    return (numerator / denominator,
        recursive(10 * (numerator % denominator), denominator, [], []))
  return max(xrange(2, 1000), key=lambda d: manual_division(1, d)[1][1])

def problem0027():
  """Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""
  def f(a_b):
    """Return the lenght of the serie"""
    a, b = a_b
    return ilen(takewhile(is_prime, (n * n + a * n + b for n in count())))
  b_candidates = list(x for x in xrange(1000) if is_prime(x))
  candidates = ((a, b) for a in xrange(-999, 1000) for b in b_candidates)
  return product(max(candidates, key=f))

def problem0028():
  """What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""
  return sum((2 + l - n) * l + 1
      for n in xrange(4)
      for l in xrange(2, 1001, 2)) + 1

def problem0029():
  """How many distinct terms are in the sequence generated by a**b for 2 <= a <= 100 and 2 <= b <= 100?"""
  return ilen(iunique((a ** b
    for a in xrange(2, 101)
    for b in xrange(2, 101))))

def problem0030():
  """Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
  return sum(n for n in xrange(2, 6*(9**5))
      if sum(x ** 5 for x in digits_from_num(n)) == n)

def problem0031():
  """How many different ways can 2 pounds be made using any number of coins?"""
  def recursive(amount, coins):
    """Returns the combinations of coins for the given amount"""
    if len(coins) == 1:
      return 1 if amount % coins[0] == 0 else 0
    return sum(recursive(amount - coins[0] * n, coins[1:])
      for n in xrange(amount / coins[0] + 1))
  return recursive(200, [200, 100, 50, 20, 10, 5, 2, 1])

def problem0032():
  """Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital"""
  def get_permutation(ndigits):
    return ((num_from_digits(ds), list(ds))
        for ds in permutations(range(1, 10), ndigits))
  def get_multiplicands(ndigits1, ndigits2):
    return cartesian_product(get_permutation(ndigits1),
        get_permutation(ndigits2))
  candidates = chain(get_multiplicands(1, 4), get_multiplicands(2, 3))
  return sum(iunique(a*b for ((a, adigits), (b, bdigits)) in candidates
    if a*b < 1e4
    and is_pandigital(adigits + bdigits + digits_from_num(a*b))))

def problem0033():
  """There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator. If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""
  def reduce_fraction(num, denom):
    gcd = greatest_common_divisor(num, denom)
    return (num / gcd, denom / gcd)
  def is_curious(numerator, denominator):
    if numerator == denominator \
        or numerator % 10 == 0 \
        or denominator % 10 == 0:
      return False
    # numerator / denominator = ab / cd
    (a, b), (c, d) = map(digits_from_num, [numerator, denominator])
    return (b == c and a * denominator == d * numerator or
        a == d and b * denominator == c * numerator)
  curious_fractions = ((num, denom) for num in xrange(10, 100)
      for denom in xrange(num + 1, 100) if is_curious(num, denom))
  numerator, denominator = map(product, zip(*curious_fractions))
  return reduce_fraction(numerator, denominator)[1]

def problem0034():
  """Find the sum of all numbers which are equal to the sum of the factorial of their digits."""
  # Cache digits from 0 to 9 to speed it up a little bit
  dfactorials = dict((x, factorial(x)) for x in xrange(10))
  # upper_bound = first(dfactorials[9] * n for n in count(1) if dfactorials[9] * n < 10 ** n)
  return sum(x for x in xrange(2540161)
      if sum(dfactorials[n] for n in digits_from_num(x)) == x)

def problem0035():
  """How many circular primes are there below one million?"""
  def is_circular_prime(digits):
    return all(is_prime(num_from_digits(digits[r:] + digits[:r]))
        for r in xrange(len(digits)))
  circular_primes = (num_from_digits(ds) for n in xrange(2, 7)
      for ds in cartesian_product([1, 3, 7, 9], repeat=n)
      if is_circular_prime(ds))
  return ilen(chain([2, 3, 5, 7], circular_primes))

def problem0036():
  """Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2."""
  # Apply a basic constraint: a binary number starts with 1, and to be
  # palindromic it must also end with 1, so candidates are odd numbers.
  return sum(x for x in xrange(1, 10**6, 2)
      if is_palindromic(x, base=10) and is_palindromic(x, base=2))

def problem0037():
  """Find the sum of the only eleven primes that are both truncatable from left to right and right to left."""
  def truncatable_get_primes():
    for ndigits in count(2):
      digit_groups = [[2, 3, 5, 7]] + [[1, 3, 7, 9]] * (ndigits - 2) + [[3, 7]]
      for ds in cartesian_product(*digit_groups):
        x = num_from_digits(ds)
        if is_prime(x) and all(is_prime(num_from_digits(ds[n:])) and
            is_prime(num_from_digits(ds[:-n])) for n in range(1, len(ds))):
          yield x
  return sum(take(11, truncatable_get_primes()))

def problem0038():
  """What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""
  def pandigital_concatenated_product(number):
    products = ireduce(operator.add, (digits_from_num(number * x)
      for x in count(1)))
    candidate_digits = first(ds for ds in products if len(ds) >= 9)
    if len(candidate_digits) == 9 and is_pandigital(candidate_digits):
      return num_from_digits(candidate_digits)
  # 987654321 is the maximum (potential) pandigital, so 9876 is a
  # reasonable upper bound
  return first(compact(pandigital_concatenated_product(n)
    for n in xrange(9877, 0, -1)))

def problem0039():
  """if p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, for which value of p < 1000 is the number of solutions maximized?"""
  def get_sides_for_perimeter(perimeter):
    return ((a, b, c) for (a, b, c) in candidates if a + b + c == perimeter)
  # Perimeter for 1st pythagorean triplet is 12, so take 84
  # (1000 / 12 = 83.3) rounds of 16 elements, total (84 * 16) 1344.
  candidates = list(take(1344, pythagorean_triplets()))
  return max(xrange(120, 1000), key=compose(ilen, get_sides_for_perimeter))

def problem0040():
  """An irrational decimal fraction is created by concatenating the positive integers: If dn represents the nth digit of the fractional part, find the value of the following expression: d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000"""
  def count_digits():
    """Like itertools.count, but returns digits instead. Starts at 1"""
    for n in count(1):
      for d in map(int, digits_from_num(n)):
        yield d
  # Indexed 0-based instead of 1-based
  indexes = set([0, 9, 99, 999, 9999, 99999, 999999])
  decimals = (d for (idx, d) in enumerate(count_digits())
      if idx in indexes)
  return product(take(len(indexes), decimals))

def problem0041():
  """What is the largest n-digit pandigital prime that exists?"""
  # 7 digits is the n-digit posible prime (using 3 divisibility)
  candidates = (num_from_digits(digits)
      for ndigits in range(7, 1, -1)
      for digits in permutations(range(ndigits, 0, -1), ndigits))
  return first(x for x in candidates if is_prime(x))

def problem0042():
  """Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?"""
  dictionary = dict((c, n + 1) for (n, c)
      in enumerate(string.ascii_uppercase))
  words = open('problem0042.txt').read().replace('"', '').split(',')
  return ilen(word for word in words if is_triangle(sum(dictionary[c]
    for c in word)))

def problem0043():
  """The number 1406357289 is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property. Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following: d2d3d4=406 is divisible by 2, d3d4d5=063 is divisible by 3, d4d5d6=635 is divisible by 5, d5d6d7=357 is divisible by 7, d6d7d8=572 is divisible by 11, d7d8d9=728 is divisible by 13, d8d9d10=289 is divisible by 17. Find the sum of all 0 to 9 pandigital numbers with this property."""
  # Begin from the last 3-digits and backtrack recursively
  def get_numbers(divisors, candidates, acc_result=()):
    if divisors:
      for candidate in candidates:
        new_acc_result = candidate + acc_result
        if num_from_digits(new_acc_result[:3]) % divisors[0] == 0:
          new_candidates = [(x,) for x in set(range(10)) - set(new_acc_result)]
          for res in get_numbers(divisors[1:], new_candidates, new_acc_result):
            yield res
    else:
      d1 = candidates[0]
      if d1: # d1 is the most significant digit, so it cannot be 0
        yield num_from_digits(d1 + acc_result)
  return sum(get_numbers([17, 13, 11, 7, 5, 3, 2], permutations(range(10), 3)))

def problem0044():
  """Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk - Pj| is minimised; what is the value of D?"""
  pairs = ((p1, p2) for (n1, p1) in ((n, pentagonal(n)) for n in count(0))
      for p2 in (pentagonal(n) for n in xrange(1, n1))
      if is_pentagonal(p1 - p2) and is_pentagonal(p1 + p2))
  p1, p2 = first(pairs)
  return p1 - p2

def problem0045():
  """It can be verified that T285 = P165 = H143 = 40755. Find the next triangle number that is also pentagonal and hexagonal."""
  # Hexagonal numbers are also triangle, so we'll check only whether they are pentagonal
  hexagonal_candidates = (hexagonal(x) for x in count(144))
  return first(x for x in hexagonal_candidates if is_pentagonal(x))

def problem0046():
  """What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""
  # primes will be iterated over and over and incremently, so better use a cached generator
  primes_ = persistent(primes())
  def satisfies_conjecture(x):
    test_primes = takewhile(lambda p: p < x, primes_)
    return any(is_integer(sqrt((x - prime) / 2)) for prime in test_primes)
  odd_composites = (x for x in take_every(2, count(3)) if not is_prime(x))
  return first(x for x in odd_composites if not satisfies_conjecture(x))

def problem0047():
  """Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?"""
  grouped_by_4factors = groupby(count(1), lambda x: len(set(prime_factors(x))) == 4)
  matching_groups = (list(group) for (match, group) in grouped_by_4factors if match)
  return first(grouplst[0] for grouplst in matching_groups if len(grouplst) == 4)

def problem0048():
  """Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000"""
  return sum(x**x for x in xrange(1, 1001)) % 10**10

def problem0049():
  """The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another. There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence. What 12-digit number do you form by concatenating the three terms in this sequence?"""
  def ds(n):
    return set(digits_from_num(n))
  def get_triplets(primes):
    for x1 in sorted(primes):
      for d in xrange(2, (10000 - x1) / 2 + 1, 2):
        x2 = x1 + d
        x3 = x1 + 2 * d
        if x2 in primes and x3 in primes and ds(x1) == ds(x2) == ds(x3):
          yield (x1, x2, x3)
  primes_ = set(takewhile(lambda x: x < 10000, primes(1000)))
  solution = index(1, get_triplets(primes_))
  return num_from_digits(flatten(digits_from_num(x) for x in solution))

def problem0050():
  """Which prime, below one-million, can be written as the sum of the most consecutive primes?"""
  def get_max_length(primes, n, max_length=0, acc=None):
    if sum(take(max_length, drop(n, primes))) >= 1e6:
      return acc
    accsums = takewhile(lambda acc: acc<1e6, accsum(drop(n, primes)))
    new_max_length, new_acc = max((idx, acc) for (idx, acc) in 
      enumerate(accsums) if is_prime(acc))
    if new_max_length > max_length:
      return get_max_length(primes, n+1, new_max_length, new_acc)
    else:
      return get_max_length(primes, n+1, max_length, acc)
  primes_ = persistent(primes())
  return get_max_length(primes_, 0)

def problem0054():
  """The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner."""
  hands = []
  for line in open('problem0054.txt').readlines():
    cards = line.strip().split()
    p1, p2 = cards[:5], cards[5:]
    break
  return None

def problem0058():
  """Starting with 1 and spiralling anticlockwise in the following way, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?"""
  diagonal_primes = 0
  number = 1
  size = 3
  while True:
    for _ in xrange(4):
      number += size - 1
      if is_prime(number):
        diagonal_primes += 1
    # 2 * (size - 1) + 1 is the total number of diagonal numbers
    if 10 * diagonal_primes < 2 * (size - 1) + 1:
      break
    size += 2
  return size

def problem0079():
  """A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317. The text file, keylog.txt, contains fifty successful login attempts. Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length."""
  return None













