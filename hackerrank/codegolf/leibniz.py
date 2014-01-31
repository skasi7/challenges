t=input()
while t>0:
 n=input()
 print '%.15f'%sum([(-1.0)**i/(2*i+1) for i in xrange(n)])
 t-=1
