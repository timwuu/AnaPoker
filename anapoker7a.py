# Analuze Poker Scenarios

# combination: C(52,5)=2,598,960
# ranks: 7,462

# ROYAL_FLUSH: 4
# STRAIGHT_FLUSH: 36
# FOUR_OF_A_KIND: 624
# FULL_HOUSE: 3,744
# FLUSH: 5,108
# STRAIGHT: 10,200
# THREE_OF_A_KIND: 54,912
# TWO_PAIR: 123,552
# ONE_PAIR: 1,098,240
# HIGH_CARD: 1,302,540

import sys

# constant
CARD_A = 14

# global variables

gRANK = 0
gLST_RANK = [ 0 for i in range(2598960+1)]
gDICT_RANK = {}

gCOMBIN_7_5 = []

def card( num, pattern):
    return num*4 + pattern - 7

def card_pattern( n):
    m=n-1
    num = m//4+1
    if( num==13):
        s = 'A'
    elif( num==12):
        s = 'K'
    elif( num==11):
        s = 'Q'
    elif( num==10):
        s = 'J'
    elif( num==9):
        s = 'T'
    else:
        s = str(num+1)

    suit = m%4
    if( suit==3):
        return 'S.'+s
    elif( suit==2):
        return 'H.'+s
    elif( suit==1):
        return 'D.'+s
    else:
        return 'C.'+s

def card_no(n):
    m=n-1
    num = m//4+1
    if( num==13):
        s = 'A'
    elif( num==12):
        s = 'K'
    elif( num==11):
        s = 'Q'
    elif( num==10):
        s = 'J'
    elif( num==9):
        s = 'T'
    else:
        s = str(num+1)
    
    return s

def card_is_same_suit(lst):
    s = lst[0]%4
    if( s== lst[1]%4 and s== lst[2]%4 and s== lst[3]%4 and s==lst[4]%4):
        return True
    return False

def card_key(lst):
    result = map( card_no, lst)
    if card_is_same_suit(lst):
        return ''.join(result)+'s'

    return ''.join(result)

def card_lst(lst):
    result = map( card_pattern, lst)
    return list(result)
    
def index( lst):

    sum = 2598960
    sum -= comb(lst[0]-1,5)
    sum -= comb(lst[1]-1,4)
    sum -= comb(lst[2]-1,3)
    sum -= comb(lst[3]-1,2)
    sum -= lst[4]

    return sum+1

def add_rank( rnk, m, n, p, q, r):
    global gLST_RANK
    lst = [m,n,p,q,r]
    lst.sort( reverse=True)
    idx=index(lst)
    gLST_RANK[idx] = rnk

    key= card_key(lst)

    if key not in gDICT_RANK:
        gDICT_RANK[key]=rnk
        #print( rnk, key)

    #print( rnk, card_lst(lst), idx)

def get_rank( hand):
    best_rank = 10000
    for i in gCOMBIN_7_5:
        lst= [ hand[i[0]],hand[i[1]],hand[i[2]],hand[i[3]],hand[i[4]]]
        key= card_key(lst)
        tmp = gDICT_RANK[key]
        if( tmp < best_rank):
            best_rank= tmp
            best_key= key
            best_comb = i

    return best_rank, best_key, best_comb

def royal_flush():
    global gRANK
    gRANK= gRANK+1
    col = []
    for i in range(3,-1,-1):
        col.append( ( card(CARD_A,i), card(13,i),card(12,i),card(11,i),card(10,i)))
        add_rank( gRANK, card(CARD_A,i), card(13,i),card(12,i),card(11,i),card(10,i))

    return col

def straight_flush():
    global gRANK
    col = []
    for j in range(13,5,-1):
        gRANK= gRANK+1
        for i in range(3,-1,-1):
            col.append( ( card(j,i), card(j-1,i),card(j-2,i),card(j-3,i),card(j-4,i)) )
            add_rank( gRANK, card(j,i), card(j-1,i),card(j-2,i),card(j-3,i),card(j-4,i))

    gRANK= gRANK+1
    for i in range(3,-1,-1):
        col.append( ( card(5,i), card(4,i),card(3,i),card(2,i),card(CARD_A,i)) )
        add_rank( gRANK, card(5,i), card(4,i),card(3,i),card(2,i),card(CARD_A,i))

    return col

def four_of_a_kind():
    global gRANK
    col = []
    for j in range(CARD_A,1,-1):
        for k in range(CARD_A,1,-1):
            if( j != k):
                gRANK= gRANK+1
                for i in range(3,-1,-1):
                    col.append( ( card(j,3), card(j,2),card(j,1),card(j,0),card(k,i)) )
                    add_rank( gRANK, card(j,3), card(j,2),card(j,1),card(j,0),card(k,i))
                    
    return col

def full_house():
    global gRANK
    col = []
    for j in range(CARD_A,1,-1):
        for k in range(CARD_A,1,-1):
            if( j != k):
                gRANK= gRANK+1
                for m in range(3,-1,-1):
                    for n in range(m-1,-1,-1):
                        col.append( ( card(j,3), card(j,2),card(j,1),card(k,m),card(k,n)) )
                        col.append( ( card(j,3), card(j,2),card(j,0),card(k,m),card(k,n)) )
                        col.append( ( card(j,3), card(j,1),card(j,0),card(k,m),card(k,n)) )
                        col.append( ( card(j,2), card(j,1),card(j,0),card(k,m),card(k,n)) )
       
                        add_rank( gRANK, card(j,3), card(j,2),card(j,1),card(k,m),card(k,n)) 
                        add_rank( gRANK, card(j,3), card(j,2),card(j,0),card(k,m),card(k,n)) 
                        add_rank( gRANK, card(j,3), card(j,1),card(j,0),card(k,m),card(k,n)) 
                        add_rank( gRANK, card(j,2), card(j,1),card(j,0),card(k,m),card(k,n))
    return col

# not including straight flush
def flush():
    global gRANK
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
                            gRANK= gRANK+1
                            for i in range(3,-1,-1):
                               col.append( ( card(j,i), card(k,i),card(l,i),card(m,i),card(n,i)) )
                               add_rank( gRANK, card(j,i), card(k,i),card(l,i),card(m,i),card(n,i))
                        else:
                            is_straight=False

    return col

# not including straight flush
def straight():
    global gRANK
    col = []
    for j in range(CARD_A,5,-1):
        gRANK=gRANK+1
        for i1 in range(3,-1,-1):
            for i2 in range(3,-1,-1):
                for i3 in range(3,-1,-1):
                    for i4 in range(3,-1,-1):
                        for i5 in range(3,-1,-1):
                            if( not (i1==i2 and i1==i3 and i1==i4 and i1==i5)):
                                col.append( ( card(j,i1), card(j-1,i2),card(j-2,i3),card(j-3,i4),card(j-4,i5)) )
                                add_rank( gRANK, card(j,i1), card(j-1,i2),card(j-2,i3),card(j-3,i4),card(j-4,i5))
                                

    gRANK=gRANK+1
    for i1 in range(3,-1,-1):
        for i2 in range(3,-1,-1):
            for i3 in range(3,-1,-1):
                for i4 in range(3,-1,-1):
                    for i5 in range(3,-1,-1):
                        if( not (i1==i2 and i1==i3 and i1==i4 and i1==i5)):
                            col.append( ( card(5,i1), card(4,i2),card(3,i3),card(2,i4),card(CARD_A,i5)) )
                            add_rank( gRANK, card(5,i1), card(4,i2),card(3,i3),card(2,i4),card(CARD_A,i5))

    return col

def three_of_a_kind():
    global gRANK
    col = []
    for j in range(CARD_A,1,-1):
        for s in range(CARD_A,1,-1):
            for t in range(s-1,1,-1):
                if( not (j==s or j==t)):
                    gRANK= gRANK+1
                    for m in range(3,-1,-1):
                        for n in range(3,-1,-1):
                            col.append( ( card(j,3), card(j,2),card(j,1),card(s,m),card(t,n)) )
                            col.append( ( card(j,3), card(j,2),card(j,0),card(s,m),card(t,n)) )
                            col.append( ( card(j,3), card(j,1),card(j,0),card(s,m),card(t,n)) )
                            col.append( ( card(j,2), card(j,1),card(j,0),card(s,m),card(t,n)) )

                            add_rank( gRANK, card(j,3), card(j,2),card(j,1),card(s,m),card(t,n)) 
                            add_rank( gRANK, card(j,3), card(j,2),card(j,0),card(s,m),card(t,n)) 
                            add_rank( gRANK, card(j,3), card(j,1),card(j,0),card(s,m),card(t,n)) 
                            add_rank( gRANK, card(j,2), card(j,1),card(j,0),card(s,m),card(t,n)) 
    return col

def two_pair():
    global gRANK
    col = []
    for j in range(CARD_A,1,-1):
        for k in range(j-1,1,-1):
            for s in range(CARD_A,1,-1):
                if( not (s==j or s==k)):
                    gRANK=gRANK+1    
                    for m in range(3,0,-1):
                        for n in range(m-1,-1,-1):
                            for p in range(3,0,-1):
                                for q in range(p-1,-1,-1):
                                        for i in range(3,-1,-1):
                                            col.append( ( card(j,m), card(j,n),card(k,p),card(k,q),card(s,i)) )
                                            add_rank( gRANK, card(j,m), card(j,n),card(k,p),card(k,q),card(s,i))
    return col

def one_pair():
    global gRANK
    col = []
    for j in range(CARD_A,1,-1):
        for s in range(CARD_A,1,-1):
            for t in range(s-1,1,-1):
                for u in range(t-1,1,-1):
                    if( not (j==s or j==t or j==u)):
                        gRANK+= 1
                        for l in range(3,-1,-1):
                            for m in range(3,-1,-1):
                                for n in range(3,-1,-1):
                                    col.append( ( card(j,3), card(j,2),card(s,l),card(t,m),card(u,n)) )
                                    col.append( ( card(j,3), card(j,1),card(s,l),card(t,m),card(u,n)) )
                                    col.append( ( card(j,3), card(j,0),card(s,l),card(t,m),card(u,n)) )
                                    col.append( ( card(j,2), card(j,1),card(s,l),card(t,m),card(u,n)) )
                                    col.append( ( card(j,2), card(j,0),card(s,l),card(t,m),card(u,n)) )
                                    col.append( ( card(j,1), card(j,0),card(s,l),card(t,m),card(u,n)) )

                                    add_rank( gRANK, card(j,3), card(j,2),card(s,l),card(t,m),card(u,n))
                                    add_rank( gRANK, card(j,3), card(j,1),card(s,l),card(t,m),card(u,n))
                                    add_rank( gRANK, card(j,3), card(j,0),card(s,l),card(t,m),card(u,n))
                                    add_rank( gRANK, card(j,2), card(j,1),card(s,l),card(t,m),card(u,n))
                                    add_rank( gRANK, card(j,2), card(j,0),card(s,l),card(t,m),card(u,n))
                                    add_rank( gRANK, card(j,1), card(j,0),card(s,l),card(t,m),card(u,n))

    return col

def high_card():
    global gRANK
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
                            gRANK+=1
                            for i1 in range(3,-1,-1):
                                for i2 in range(3,-1,-1):
                                    for i3 in range(3,-1,-1):
                                        for i4 in range(3,-1,-1):
                                            for i5 in range(3,-1,-1):
                                                if( not (i1==i2 and i1==i3 and i1==i4 and i1==i5) ):
                                                    col.append( ( card(j,i1), card(k,i2),card(l,i3),card(m,i4),card(n,i5)))
                                                    add_rank( gRANK, card(j,i1), card(k,i2),card(l,i3),card(m,i4),card(n,i5))
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

print( gCOMBIN_7_5)


i=0

for m in range(0,7):
    for n in range(m+1,7):
        for p in range(n+1,7):
            for q in range(p+1,7):
                for r in range(q+1,7):
                    gCOMBIN_7_5.append([m,n,p,q,r])
                    i=i+1

#print(i)
#print(gCOMBIN_7_5)

print( comb(52,5))

'''
print( seq(52,51,50,48,1))
print( seq2(52,51,50,48,1))

print( seq(52,50,49,48,47))
print( seq2(52,50,49,48,47))

print( seq2(5,4,3,2,1))
'''
print( len(royal_flush()))
print( len(straight_flush()))
print( len(four_of_a_kind()))
print( len(full_house()))
print( len(flush()))
print( len(straight()))
print( len(three_of_a_kind()))
print( len(two_pair()))
print( len(one_pair()))
print( len(high_card()))

print( "gRANK:", gRANK)

print( "size of DICT:", sys.getsizeof(gDICT_RANK))


hand = [52, 51, 50, 4, 3, 2, 1]

rnk = get_rank( hand)

print( "rank:", rnk)

#x=(1,2,3,4)
#print( x[0],x[1])

# seq(m,n,p,q,r)  ;ordered

# seq(m,n,p,q,r)
# = base(m,m-1,m-2,m-3,m-4) + diff4(m-1,n) + diff3(n-1,p) + diff2(p-1,q) + diff1(q-1,r)