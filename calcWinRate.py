import sys
import random
import ranks

gCOMBIN_7_5 = []

def card( num, pattern):
    return num*4 + pattern - 7

def card_pattern( n):
   
    s = card_no(n)
      
    return ('S','C','D','H')[n%4] + '.' + s

def card_no(n):

    return ('1','2','3','4','5','6','7','8','9','T','J','Q','K','A')[(n+3)//4]

def card_is_same_suit(lst):
    s = lst[0]%4
    if( s== lst[1]%4 and s== lst[2]%4 and s== lst[3]%4 and s==lst[4]%4):
        return True
    return False

def card_key(lst):
    key = map( card_no, lst)
    if card_is_same_suit(lst):
        return ''.join(key)+'s'

    return ''.join(key)

def card_lst(lst):
    result = map( card_pattern, lst)
    return list(result)

def get_rank( hand):
    best_rank = ranks.RANK_MAX
    for i in gCOMBIN_7_5:
        lst= (hand[i[0]],hand[i[1]],hand[i[2]],hand[i[3]],hand[i[4]])
        key= card_key(lst)
        tmp = ranks.ranks[key]
        if( tmp < best_rank):
            best_rank= tmp
            best_key= key
            best_comb = i

    return best_rank, best_key, best_comb

def calc_win_rate( player_a, player_b, table_cards, k=10000):

    cards = [ x for x in range(1,53)]

    for i in player_a:
        cards.remove(i)

    for i in player_b:
        cards.remove(i)

    for i in table_cards:
        cards.remove(i)

    n = 5 - len(table_cards)

    win_a = 0
    win_b = 0

    for i in range(k):
        s = random.sample( cards, k=n)

        pl_a = player_a + table_cards + s
        pl_b = player_b + table_cards + s

        pl_a.sort( reverse= True)
        pl_b.sort( reverse= True)

        rnk_a = get_rank( pl_a)
        rnk_b = get_rank( pl_b)

        if(rnk_a < rnk_b):
            win_a += 1
        elif( rnk_b < rnk_a):
            win_b += 1

    return ( win_a/k, win_b/k)




############## start of main program ##################

i=0

for m in range(0,7):
    for n in range(m+1,7):
        for p in range(n+1,7):
            for q in range(p+1,7):
                for r in range(q+1,7):
                    gCOMBIN_7_5.append([m,n,p,q,r])
                    i=i+1
