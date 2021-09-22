import sys
import random
import ranks

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

def get_rank( hand):
    best_rank = 10000
    for i in gCOMBIN_7_5:
        lst= [ hand[i[0]],hand[i[1]],hand[i[2]],hand[i[3]],hand[i[4]]]
        key= card_key(lst)
        tmp = ranks.ranks[key]
        if( tmp < best_rank):
            best_rank= tmp
            best_key= key
            best_comb = i

    return best_rank, best_key, best_comb

############## start of main program ##################

i=0

for m in range(0,7):
    for n in range(m+1,7):
        for p in range(n+1,7):
            for q in range(p+1,7):
                for r in range(q+1,7):
                    gCOMBIN_7_5.append([m,n,p,q,r])
                    i=i+1


print( "size of DICT:", sys.getsizeof(ranks.ranks))


gCards = [ x for x in range(1,53)]

random.shuffle(gCards)

player_a = [ gCards[0], gCards[2], gCards[4], gCards[5], gCards[6], gCards[7], gCards[8]]
player_b = [ gCards[1], gCards[3], gCards[4], gCards[5], gCards[6], gCards[7], gCards[8]]

player_a.sort( reverse= True)
player_b.sort( reverse= True)

print( "Player A:", card_lst(player_a))

print( "Player B:", card_lst(player_b))

rnk_a = get_rank( player_a)
rnk_b = get_rank( player_b)

print( "Rank:", rnk_a,"vs", rnk_b)