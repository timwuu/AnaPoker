# AnaPoker [WIP]
Texas Hold'em Poker Utility Tools

---------------------------
anapoker.py  --  Generate 5-card ranking data

calcWinRate.py - Calculate the winning rate of players

Notes:
  * card number from 52 to 1 means ♠A, ♥A, ♦A, ♣A to ♠2, ♥2, ♦2, ♣2.
  * the number of ranking is the lower the better.  The (RANK_MIN,RANK_MAX) in ranks.py is (1,7462)
  
Examples:
  * calc_win_rate( [52,51], [46,45], [48,44,40], 10000)
  * calc_win_rate( [52,51], [46,45], [], 10000)
  * calc_win_rate( [52,51], [], [], 10000)
