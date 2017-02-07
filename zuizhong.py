# -*- coding:utf-8  -*-
import numpy as np
import random
import qiujie
sd=np.zeros((9,9))
print "数独初始化\n******************************************"
i=0fffffffffffffffffff
j=0
while(i<=8):
    while(j<=8):
        m=(i/3)*3+j/3
        [a,b,c]=qiujie.shuaxin(sd)
        kx=qiujie.keyi(a[i],b[j],c[m])
        if kx:
            sd[i,j]=random.choice(kx)
            j=j+1
            print i,j
        else:
            i=0
            j=0
    i=i+1
    j=0

