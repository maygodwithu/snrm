import sys

for line in sys.stdin:
    psd = (line.rstrip()).split(' ')
    cnt = psd[-1]	
    q = psd[0] 
    for t in psd[1:-1]:
       q = q + ' ' + t  
    print('%s\t%s\t%s' %(q, cnt, cnt)) 
