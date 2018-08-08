User uses a listing of upcoming games:


takes in a "bet()/3":

  Example: 

    Given Pools:

	gamePools(Game 1(Team 1 vs Team 2),
		  Game 2(Team 3 vs Team 4),
		  Game 3(Team 5 vs Team 6))

Win
	Bet 1: bet(wallet id: "11"	, bet ammount: "10"	, Game 1, Team 1);	 
	Bet 2: bet(wallet id: "12"	, bet ammount: "20"	, Game 2, Team 3);
	Bet 3: bet(wallet id: "13"	, bet ammount: "30"	, Game 3, Team 6);
	Bet 4: bet(wallet id: "14"	, bet ammount: "40"	, Game 1, Team 1);	 
	Bet 5: bet(wallet id: "15"	, bet ammount: "50"	, Game 2, Team 4);
	Bet 6: bet(wallet id: "16"	, bet ammount: "60"	, Game 3, Team 5);
	Bet 7: bet(wallet id: "17"	, bet ammount: "70"	, Game 1, Team 2);	 
	Bet 8: bet(wallet id: "18"	, bet ammount: "80"	, Game 2, Team 4);
	Bet 9: bet(wallet id: "19"	, bet ammount: "90"	, Game 3, Team 6);

  Winnings for this round

	Game 1 =	$120 = (Team 1($10 + $40) + Team 2($70)) = $50 + $70
	Game 2 =	$150 = (Team 3($20) + Team 4($50 + $80)) = $20 + $130
	Game 3 =	$180 = (Team 5($60) + Team 6($30 + $90))  = $60 + $120

	Total  = $450

	Bet Worth:)

          Payouts:

	    Game 1 Bets:  NOTE: Team 1 favored 3/2 over team 2.	

		Team 1: ($50 / $120))) = 0.416666667 = 41.6666667% 

		  Bet 1: gets $10 / $50 = 20% of (58.3333333% of $120) = $70 * .20 = $14 + $10 	= $24  - $1.2 = $22.8
		  Bet 4: gets $40 / $50 = 80% of (58.3333333% of $120) = $70 * .80 = $56 + $40 	= $96  - $4.8 = $91.2
												= $120 - $6   = $114
		    Bet 1 profit = 12.8 = 228% increase
		    Bet 4 profit = 51.2 = 228% increase

		    Network profit = $6 = 5% of total game bets

		Team 2: $70 / $120 = 0.583333333 = 58.3333333% 
	
 		  Bet 7: gets $70 / $70 = 100% of (0.41666667% of $120) = $50 * 1.0 = $50 + $70	= $120 - $6   = $114

		    Bet 7 profit = $50 = 171.4285714% increase

		    Network profit = $6 = 5% of total game bets

	    Game 2 Bets:  NOTE: Team 1 favored 3/2 over team 2.	
		
		Team 3: NOTE: ($20 / $150) = .13333333% = 13.333333%
		
 		  Bet 2: gets $20 / $20 = 100% of (86.6666667% of $150) = $130 * 1.0 = $130 + $20= $150 - $7.5 = $142.5
		    
		    Bet 2 profit = $142.5 = 712.5% increase

    		    Network profit = $7.5 = 5% of total game bets

		Team 4: NOTE: ($130 / $150) = 0.866666667 = 86.6666667%

		  Bet 5: gets $50 / $130 = 0.3846% of (13.333333% of $150) = $20 * .3846 = $7.69 + $50 = $57.6 - $2.88 = $54.8074
		  Bet 8: gets $80 / $130 = 0.6154% of (13.333333% of $150) = $20 * .6154 = $12.3 + $80 = $92.3 - $4.6 = $87.6926

		    Bet 5 profit = $54.8074 = 109.6148% increase
		    Bet 8 profit = $87.6926 = 109.6157% increase

  		    Network profit = $7.5 = 5% of total game bets

	    Game 3 Bets:  NOTE: 
			Game 3 =	$180 = (Team 5($60) + Team 6($30 + $90))  = $60 + $120

		Team 3: NOTE: ($60 / $180) = .333333333% = 33.333333%

		  Bet 6: gets $60 / $60 = 100% of (66.66666% of $180) = $120 * 1.0 = $120 + $60 = $180 - $9 = $171

		    Bet 6 profit = $171 = 285%% increase

  		    Network profit = $9 = 5% of total bets

		Team 3: NOTE: ($120 / $180) = .66666666% = 66.666666%

 	  	  Bet 3: gets $30 / $120 = 25% of (33.33333% of $180) = $60 * .25 = $15 + $30 = $45 - $2.25  = $42.75
		  Bet 9: gets $90 / $120 = 75% of (33.33333% of $180) = $60 * .75 = $45 + $90 = $135 - $6.75 = $128.25
												180 - $9   = $171
		    Bet 3 profit = $42.74  = 142.46666% increase
		    Bet 9 profit = $128.25 = 142.77777% increase

  		    Network profit = $9 = 5% of total bets


	Bet tot:  =	$450

	Network Profit:
		
		Game 1: 	$6
		Game 2: 	$7.5
		Game 3: 	$9
			     = 	$22.5 = 5% of $450


