import sys
import numpy as np
import random

def printd(na, fp, first=False, last=False):
    if(not first):
        print('\t', file=fp, end='')
    string=''
    for it in na:
        if(string != ''):
            string += ','
        string += str(it)
    print(string, file=fp, end='')
    if(last):
        print('\n', file=fp, end='')

tid=0
dic={}
for line in sys.stdin:
    psd = (line.rstrip()).split('\t')
    q = psd[0] 
    dic[q] = tid
    tid += 1

## make fake
'''
fp = open('data.csv', 'w')
for i in range(513):
    qsize = random.randrange(1,10) 
    d1size = random.randrange(1,100)
    d2size = random.randrange(1,100)
    positive = np.random.randint(2)
    negative = 1 - positive

    qids = np.random.randint(tid, size=10)
    dids1 = np.random.randint(tid, size=1000)
    dids2 = np.random.randint(tid, size=1000)

    printd(qids, fp, first=True) 
    printd(dids1, fp) 
    printd(dids2, fp) 
    printd(np.array([positive]), fp, last=True)

fp.close()
'''

## make embedding
fp = open('embedding.txt', 'w')
for i in range(tid):
    print(i, file=fp, end='') 
    emb = np.random.randn(100)
    for v in emb:
        print(' %.3f' % v, file=fp, end='') 
    print('\n', file=fp, end='')
fp.close()

