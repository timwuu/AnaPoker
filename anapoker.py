# Analuze Poker Scenarios

def comb(p,q):

    if( q==5):
        return int(p*(p-1)*(p-2)*(p-3)*(p-4)/120)

    if( q==4):
        return int(p*(p-1)*(p-2)*(p-3)/24)

    if( q==3):
        return int(p*(p-1)*(p-2)/6)

    if( q==2):
        return int(p*(p-1)/2)

    if( q==1):
        return p

def seq(m,n,p,q,r):

    sum = 2598960 - comb(m,5)
    sum += comb(m-1,4) - comb(n,4)
    sum += comb(n-1,3) - comb(p,3)
    sum += comb(p-1,2) - comb(q,2)
    sum += q - 1 - r

    return sum+1


i=0

for m in range(7,0,-1):

    for n in range(m-1,0,-1):
        
        for p in range(n-1,0,-1):

            for q in range(p-1,0,-1):

                for r in range(q-1,0,-1):

                    #print( i,':', m,n,p)
                    i=i+1

print(i)

print( comb(52,5))

print( seq(52,51,50,48,1))

print( seq(52,50,49,48,47))

# seq(m,n,p,q,r)  ;ordered

# seq(m,n,p,q,r)
# = base(m,m-1,m-2,m-3,m-4) + diff4(m-1,n) + diff3(n-1,p) + diff2(p-1,q) + diff1(q-1,r)