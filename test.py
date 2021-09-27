import timeit
import ranks
import calcWinRate as cwr

def pp( a, b, table, k):

    result = cwr.calc_win_rate( a, b, table, k)

    print( "{} vs {} with {}".format( cwr.card_lst(a), cwr.card_lst(b), cwr.card_lst(table)))

    print( "{:2.2%} vs {:2.2%}\n".format(result[0], result[1]))


k= 10000 # simulate k times

# --- example 0 ---

player_a = [52,51]
player_b = [46,45]

table_cards = []

pp( player_a, player_b, table_cards, k)

table_cards = [48,44,40]

pp( player_a, player_b, table_cards, k)

#print( timeit.timeit("calcWinRate.get_rank_b([52,51,50,49,48,47,46])", setup="import calcWinRate", number=100000))

#print( timeit.timeit("calcWinRate.get_rank([52,51,50,49,48,47,46])", setup="import calcWinRate", number=100000))

# "AKQJTs":1
print ( ranks.rank_tree[12][11][10][9][8][1])

# "AKQJT":1600
print ( ranks.rank_tree[12][11][10][9][8][0])

# "32222":166
print ( ranks.rank_tree[1][0][0][0][0][0])
