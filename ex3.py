import calcWinRate as cwr

def pp( a, b, table, k):

    result = cwr.calc_win_rate( a, b, table, k)

    print( "{} vs {} with {}".format( cwr.card_lst(a), cwr.card_lst(b), cwr.card_lst(table)))

    print( "{:2.2%} vs {:2.2%}\n".format(result[0], result[1]))


k= 10000 # simulate k times

# --- example 0 ---

# --- AA pre-flop
player_a = [52,51]  #AA
player_b = []  
table_cards = []

pp( player_a, player_b, table_cards, k)

# --- 72s pre-flop
player_a = [24,4]  #72s
player_b = []  
table_cards = []

pp( player_a, player_b, table_cards, k)

# --- 72 pre-flop
player_a = [24,3]  #72
player_b = []  
table_cards = []

pp( player_a, player_b, table_cards, k)


# --- AA vs 72 pre-flop
player_a = [52,51]  #AA
player_b = [24,3]  #72  
table_cards = []

pp( player_a, player_b, table_cards, k)

# --- AA vs [] with [7,6,2] rainbow
player_a = [52,51]  #AA
player_b = []  
table_cards = [24,19,2]

pp( player_a, player_b, table_cards, k)

# --- 4 card flush vs one pair
# --- AKs vs KQ / Q87
player_a = [52,48]  #AKs
player_b = [47,42]  #KQ  
table_cards = [44,27,24] #Q87

pp( player_a, player_b, table_cards, k)

# -- KsJh vs 6d5ds - 62/37
player_a = [48,39]
player_b = [18,14]  
table_cards = []

pp( player_a, player_b, table_cards, k)

# -- As4h vs KsQh - 62/37
player_a = [52,11]
player_b = [48,43]  
table_cards = [24,31,3,22] #7927J

pp( player_a, player_b, table_cards, k)
