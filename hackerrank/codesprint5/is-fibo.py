
def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    # Precompute
    fibos = list()
    for fibo in fibo_gen():
        if fibo > 10**10:
            break;
        fibos.append(fibo)
    # Challenge code
    t = input()
    for _ in xrange(t):
        n = input()
        print (n in fibos) and 'IsFibo' or 'IsNotFibo'

