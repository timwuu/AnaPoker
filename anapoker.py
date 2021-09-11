# Analuze Poker Scenarios

# constant
CARD_A = 14

def card( num, pattern):
    return num*4 + pattern

def royal_flush():
    col = []
    for i in range(3,-1,-1):
        col.append( ( card(CARD_A,i), card(13,i),card(12,i),card(11,i),card(10,i)))
    return col

def straight_flush():
    col = []
    for j in range(13,4,-1):
        for i in range(3,-1,-1):
            col.append( ( card(j,i), card(j-1,i),card(j-2,i),card(j-3,i),card(j-4,i)) )
    return col

def four_of_a_kind():
    col = []
    for j in range(CARD_A,1,-1):
        for k in range(CARD_A,1,-1):
            for i in range(3,-1,-1):
                if( j != k):
                    col.append( ( card(j,3), card(j,2),card(j,1),card(j,0),card(k,i)) )
    return col

def full_house():
    col = []
    for j in range(CARD_A,1,-1):
        for k in range(CARD_A,1,-1):
                if( j != k):
                    for m in range(3,-1,-1):
                        for n in range(m-1,-1,-1):
                            col.append( ( card(j,3), card(j,2),card(j,1),card(k,m),card(k,n)) )
                            col.append( ( card(j,3), card(j,2),card(j,0),card(k,m),card(k,n)) )
                            col.append( ( card(j,3), card(j,1),card(j,0),card(k,m),card(k,n)) )
                            col.append( ( card(j,2), card(j,1),card(j,0),card(k,m),card(k,n)) )
    return col

# not including straight flush
def flush():
    col = []
    is_straight=False
    for j in range(CARD_A,6,-1): # Case (6,5,4,3,2)
        is_straight=True
        kk = 5 if (j==CARD_A) else 4  # Case (CARD_A,5,4,3,2)
        for k in range(j-1,kk,-1):
            for l in range(k-1,3,-1):
                for m in range(l-1,2,-1):
                    for n in range(m-1,1,-1):
                        if not is_straight:
                            col.append( ( card(j,3), card(k,3),card(l,3),card(m,3),card(n,3)) )
                            col.append( ( card(j,2), card(k,2),card(l,2),card(m,2),card(n,2)) )
                            col.append( ( card(j,1), card(k,1),card(l,1),card(m,1),card(n,1)) )
                            col.append( ( card(j,0), card(k,0),card(l,0),card(m,0),card(n,0)) )
                        else:
                            is_straight=False

    return col

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

def seq2(m,n,p,q,r):

    sum = 2598960
    sum -= comb(m-1,5)
    sum -= comb(n-1,4)
    sum -= comb(p-1,3)
    sum -= comb(q-1,2)
    sum -= r

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
print( seq2(52,51,50,48,1))

print( seq(52,50,49,48,47))
print( seq2(52,50,49,48,47))

print( seq2(5,4,3,2,1))

print( len(royal_flush()))
print( len(straight_flush()))
print( len(four_of_a_kind()))
print( len(full_house()))
print( len(flush()))
'''
print( royal_flush())
print( straight_flush())
print( four_of_a_kind())
'''

#x=(1,2,3,4)
#print( x[0],x[1])

# seq(m,n,p,q,r)  ;ordered

# seq(m,n,p,q,r)
# = base(m,m-1,m-2,m-3,m-4) + diff4(m-1,n) + diff3(n-1,p) + diff2(p-1,q) + diff1(q-1,r)