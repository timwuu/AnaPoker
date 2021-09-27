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

# --- example 0.1 ---

table_cards = [48,44,40]

pp( player_a, player_b, table_cards, k)

# --- example 1 ---

player_a = [48,47]
player_b = [42,38]

table_cards = []

pp( player_a, player_b, table_cards, k)

# --- example 2 ---

table_cards = [52,46,24]

pp( player_a, player_b, table_cards, k)

# --- example 2.2 ---

table_cards = [52,46,24,26]

pp( player_a, player_b, table_cards, k)

# --- example 3 ---

table_cards = [50,46,24]

pp( player_a, player_b, table_cards, k)

# --- example 4 ---

table_cards = [52,46,22]

pp( player_a, player_b, table_cards, k)

# --- example 4.2 ---

table_cards = [52,46,22,18]

pp( player_a, player_b, table_cards, k)

# --- example 5 ---

table_cards = [46,33,24]

pp( player_a, player_b, table_cards, k)

# --- example 5.2 ---

table_cards = [46,34,24]

pp( player_a, player_b, table_cards, k)

# --- example 6 ---

table_cards = [34,30,24]

pp( player_a, player_b, table_cards, k)
