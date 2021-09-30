import calcWinRate as cwr

def pp( a, b, table, k):

    result = cwr.calc_win_rate( a, b, table, k)

    print( "{} vs {} with {}".format( cwr.card_lst(a), cwr.card_lst(b), cwr.card_lst(table)))

    print( "{:2.2%} vs {:2.2%}\n".format(result[0], result[1]))


k= 10000 # simulate k times

# --- example 0 ---

# --- 1-draw straight vs 4-card flush
player_a = [51,43]  #AQ
player_b = [52,48]  #AKs
table_cards = [47,40,28] #K,J,8

pp( player_a, player_b, table_cards, k)

# --- straight vs 4-card flush
player_a = [51,43]  #AQ
player_b = [52,48]  #AKs
table_cards = [47,40,28,33] #K,J,8,T

pp( player_a, player_b, table_cards, k)

# --- straight vs three of kind
player_a = [51,43]  #AQ
player_b = [47,46]  #KK
table_cards = [48,40,26,33] #K,J,8,T

pp( player_a, player_b, table_cards, k)

# --- straight vs two pairs
player_a = [51,43]  #AQ
player_b = [47,39]  #KJs
table_cards = [48,40,26,33] #K,J,8,T

pp( player_a, player_b, table_cards, k)
