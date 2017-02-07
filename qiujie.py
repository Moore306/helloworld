#-*-coding:utf-8 -*-
import numpy as np
import time
start = time.clock()
def yueshu(a):
    b=[]
    for i in range(1,10):
        if i not in a:
            b.append(i)
    return b
 #确定某一位置可填的数字
def keyi(a,b,c):
  d=[]
  a=yueshu(a)
  b=yueshu(b)
  c=yueshu(c)
  for i in range(len(a)):
      m = a[i]
      if m<>0:
        n = 1 + b.count(m) + c.count(m)
        if n==3:
            d.append(m)
  return d
print '复制处理函数\n*************************************************************'
def shuaxin(shudu):
    a=shudu
    c = np.zeros((9, 9))
    for m in range(3):
        for n in range(3):
            for i in range(3):
                for j in range(3):
                    c[m * 3 + n][i * 3 + j] = shudu[i + 3 * m][j + 3 * n]
    b = shudu.T
    return [a,b,c]
print "开始扫描填入vub\n*********************************************************"
print "***********************************************************8"
def zuiduo(shudu):
    number = np.zeros((1 * 9))
    for k in range(9):
        i = 0
        for m in range(9):
            for n in range(9):
                if shudu[m][n] == k+1:
                    i = i + 1
        number[k] = i
    bb=number
    for z in range(len(bb)):
        if bb[z]==9:
            bb[z]=-1
    cc=np.where(bb==bb.max())
    nn=9-bb.max()
    mm=cc[0]+np.ones(len(cc[0]))
    if bb.max()==-1:
        mm[0]=100
        nn=100
    return [mm,n]
    #找出出现次数最多的数字mm,0除外,填满返回100
def jishu(h,o):
    mn=0
    for i in range(len(h)):
        if h[i]==o:
            mn=mn+1
    return mn
#定义约束条件函数
def yueshu1(shudu):
    ys=0
    [a,b,c]=shuaxin(shudu)
    [m,n]=zuiduo(shudu)#n是数字空缺的个数
    if n<>100:
        ks=[]
        for km in m:
            for i in range(9):
                if km not in a[i]:
                    k=0
                    liebiao=[]
                    for j in range(9):
                        if a[i][j]==0:
                            k=k+1
                            liebiao.append(j)
                    ks.append([km,i,k,liebiao])
    # ks是返回一个【km,i，k】组成的列表，km是目标数字（出现比较多的数），i是第i+1行，k是空的个数
    #np.array(ks)
    if n==1:
        for i in range(len(m)):
            shudu[ks[i][1]][ks[i][3][0]]=m[i]
        [a,b,c]=shuaxin(shudu)
        ys=1
    else:
        for x in range(len(ks)):
            i=ks[x][1]
            for y in ks[x][3]:
                paichu=np.ones(ks[x][2])*2
                nn=0
                 #2代表可以填，0代表不可以填
                for z in ks[x][3]:
                    if z<>y:
                        j=z
                        g=(i/3)*3+j/3
                        if ks[x][0] not in keyi(a[i],b[j],c[g]):
                            paichu[nn]=0
                    nn=nn+1
                if jishu(paichu,2)==1:
                    kt=np.where(paichu==2)[0][0]
                    shudu[i,ks[x][3][kt]]=ks[x][0]
                    print '排除法：i=',i,' j=',ks[x][3][kt],' 填入',ks[x][0]
                    #print shudu
                    [a,b,c]=shuaxin(shudu)
                    ys=1#ys=1代表成功使用本方法
                    break
    return ys
def yueshu3(shudu):
    ys=1
    while(ys==1):
        ys=yueshu1(shudu)
def yueshu2(shudu):
    ys2=1
    while(ys2==1):
        ys2=0
        for i in range(9):
            for j in range(9):
                if shudu[i][j] == 0:
                    m = (i / 3) * 3 + j / 3
                    [a, b, c] = shuaxin(shudu)
                    shitan = keyi(a[i], b[j], c[m])
                    if len(shitan) == 1:
                        #print shitan, i, j
                        shudu[i][j] = shitan[0]
                        print '正向确定法：i=',i,', j=',j,'填入',shitan[0]
                        ys2=1
    return ys2
def qiujie(shudu):
    while(0 in shudu):
        yueshu2(shudu)
        yueshu3(shudu)
    print 'jieshuh@@@@@@@@@@@@@@@$$$$$%$%$$$$%%$%$' \
          'Y&Y&&&&&&&&&&&&&&&&&&'
    print shudu
    end = time.clock()
    print 'emd=',end
    print '用时：',end-start