result_dict = {
    (True, False): 1,
    (False, True): 2,
    (True, True): 0,
    (False, False): -1
  }
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        line = raw_input().strip()
        first_word, last_word = line.split(' ', 1)[0], line.rsplit(' ', 1)[-1]
        print result_dict[(first_word == 'hackerrank', last_word == 'hackerrank')]

