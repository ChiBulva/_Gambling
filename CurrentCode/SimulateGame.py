def PlayGame():
    print("Simulating Multi Game")
 
    Ans = 'W'
    while(Ans!=0 and Ans!=1 and Ans!=2):
        Ans = input("Current Simulation Over, what would you like to simulate now?\ntype '0' to exit\n type '1' to Simulate random again\ntype '2' to simulate the 2018 NFL season\n: ")
        if(Ans=='0'):
            print("You chose to exit the simulation!!!\n\n<----")
            exit()

        elif(Ans=='1'):
 
            Games = []
            NumGames = input("How many Games??\n: ")
            #NumGames = 1
            #NumTeams = (NumGames * 2)

            #Assign Number of Bets
            Bets = []
            print("**NOTE: Bets ammounts will be limited to a max of $100\n for this simulation, Minimum of 1")
            NumBets = input("How many Bets do you want??\n: ")
            Ammount = input("What is the highest bet ammount??\n: ")

            Games = InitilizeRandomGame(NumGames) #Simulate Random Teams
            Bets = InitilizeRandomBets(NumBets, Games, Ammount)
            PrintBets(Bets)
            SimulateGamePlayed(Games, Bets)

        elif(Ans=='2'):
            print("Simulate the Season!\n\n")

            #Assigns Team names by game in order of week
            Games = ReturnTeamsInWeekOrder() #Simulate NFL 2018
            
            #Assign Number of Bets
            Bets = []
            print("**NOTE: Bets ammounts will be limited to a max of $100\n for this simulation, Minimum of 1")
            NumBets = input("How many Bets do you want??\n: ")
            
            Ammount = input("What is the highest bet ammount??\n: ")

            Bets = InitilizeRandomBets(NumBets, Games, Ammount)
            PrintBets(Bets)
            SimulateGamePlayed(Games, Bets)
            

            exit()



def InitilizeRandomBets(NumBets, Games, Max):
    from random import randint
    Bets = []

    idNum = 1
    Ammounts = []
    for num in range(int(NumBets)):
        #Ammount = randint(1,10)*10
        Ammount = randint(1,int(Max))
        #   print("Len Games: "+str(len(Games)))
        Game = randint(0,len(Games)-1)
        Team = randint(0,1)
        #   print("trying: Ammount: "+str(Ammount)+" | Game: "+str(Game+1)+" | Team: "+str(Team))
        #   print("-->Bet #"+str(num+1)+": "+str(Ammount)+" on "+str(Games[Game][Team])+"\n")
        Bets.append((str(Games[Game][Team]),Ammount,idNum))
        #Bets.append((str(Games[randint(0,len(Games))][Team]),Ammount,idNum))
        idNum = idNum+1
    return Bets
 
def InitilizeRandomGame(NumGames):
    from random import randint
    Games = []
    TeamsUsed = []
    for num in range(int(NumGames)):
        num1 = 0
        num2 = 0
        
        while(num1==num2):
            trigger = 0
            while(trigger==0):
                num1 = randint(1,int(NumGames)*2)
                num2 = randint(1,int(NumGames)*2)
                #print("Trying: "+str(num1)+" & "+str(num2))
                if((num1!=num2) and (num1 not in TeamsUsed) and (num2 not in TeamsUsed)):
                    TeamsUsed.append(num1)
                    TeamsUsed.append(num2)
                    trigger = 1

            Team1 = PickRandomName(num1)
            Team2 = PickRandomName(num2)
        Games.append((Team1,Team2))
    return Games
############################################################
#   
#  Variable Structures: 
#
#   ListOfGames -> formats -> x ([Team 1 Name],[Team 2 Name])
#
#                      3 games -> 0 ("Elk","Portland Trail Blazers")
#                                 1 ("Cats","Geese")
#                                 2 ("Mice","No Name")
#   
#   ListOfBets -> format -> x ([<"Name"> or <spot in Game Array>],[$ Ammount of Bet],[Wallet ID])
#
#                     8 Bets -> 0 ("Geese"                  , $20   , "xx0001"  )
#                               1 ("Portland Trail Blazers" , $10   , "xx0002"  )
#                               2 ("Elk"                    , $100  , "xx0003"  )
#                               3 ("Fish"                   , $70   , "xx0004"  )
#                               4 ("No Name"                , $50   , "xx0005"  )
#                               5 ("No Name"                , $20   , "xx0006"  )
#                               6 ("Humans"                 , $10   , "xx0006"  )
#                                                              ^   
#                                                           TotalPool
#
#  Creates: 
#
#    List of Current Betting Payouts
#      Payuouts -> ()
#
#  Returns: NOTE: same length as FullListOfBets
#
#    PayoutTable -> format -> x ([Wallet ID], [Payout ammount])
#   
#   
def SimulateGamePlayed(ListOfGames, ListOfBets):
    PayoutTable = []
    PayoutTable = InitilizePayoutTable(PayoutTable, len(ListOfGames), ListOfGames)
    Total = 0
    #for num in range(len(PayoutTable)):
    #    print(PayoutTable[num])

    print("\nStarting Time Line of Bets!!!\n")
    #Run through Bets and add ammounts to PayoutTable
    for bet in range(len(ListOfBets)):
        
        Total = Total + ListOfBets[bet][1]
        for game in range(len(ListOfGames)):

            if(ListOfGames[game][0]==ListOfBets[bet][0]):
                PayoutTable[game][0][1] = PayoutTable[game][0][1]+ListOfBets[bet][1]
#                print("Bet made for "+str(ListOfBets[bet][1])+" on the "+str(PayoutTable[game][0]))
            elif(ListOfGames[game][1]==ListOfBets[bet][0]):
                PayoutTable[game][1][1] = PayoutTable[game][1][1]+ListOfBets[bet][1]
#                print("Bet made for "+str(ListOfBets[bet][1])+" on the "+str(PayoutTable[game][1]))

    #print("Total Ammount Bet on "+str(PayoutTable[game][0]))
    #print("Bet made for "+str(ListOfBets[bet][1])+" on the "+str(PayoutTable[game][1]))

    #    PrintPayoutTable(PayoutTable, Total)
    Payout = DetermineBetPayout(ListOfBets, PayoutTable)

    #input("Press Enter to print PayouTable and Equations: ")
    #PrintPayoutTable(PayoutTable, Total)
    SavePayoutTable(PayoutTable, Total)
    #PrintPayoutEquations(Payout)
    SavePayoutResults(Payout)

def AddBet(Bets):
    input("Team name you would like to bet for: ")

def DetermineBetPayout(Bets, PayoutTable):
    #PrintThis(PayoutTable)
    #print(CurBet)
    FinalGameTotal1 = 0
    FinalGameTotal2 = 0
    FinalPayouts = []
    percent = 0
    for bet in range(len(Bets)):
        for num in range(len(PayoutTable)):
            if(PayoutTable[num][0][0]==Bets[bet][0] or PayoutTable[num][1][0]):
                if(PayoutTable[num][0][0]==Bets[bet][0]):
                    #print("Bet Matches Team 1 of Game: ")
                    GameTotal = PayoutTable[num][0][1]+PayoutTable[num][1][1]
                    #print(str(Bets[bet]) + " Won")                    
                    if(PayoutTable[num][1][1]!=0):
                        FinalBefore1 = (Bets[bet][1]/PayoutTable[num][0][1])
                        FinalP = Bets[bet][1]+((Bets[bet][1]/PayoutTable[num][0][1])*PayoutTable[num][1][1])
                        percent = FinalP*.95
                    else:
                        FinalBefore1 = 0
                        FinalP = 0
                    #print(str(Bets[bet][1])+" + ( "+str(Bets[bet][1])+" / "+str(PayoutTable[num][0][1])+") = ("+str(FinalBefore1)+" * "+str(PayoutTable[num][1][1])+") = "+str(FinalP))
                    equation = (str(Bets[bet][1])+" + ( "+str(Bets[bet][1])+" / "+str(PayoutTable[num][0][1])+") = ("+str(FinalBefore1)+" * "+str(PayoutTable[num][1][1])+") = "+str(FinalP)+" = "+str(FinalP)+" * .95 --> Payout of "+str(percent)+" | Profit of: +"+str(percent-Bets[bet][1]))
                    FinalGameTotal1 = FinalGameTotal1 + FinalP
                    FinalPayouts.append((Bets[bet][2],Bets[bet][1],Bets[bet][0],FinalP,equation))
                    break

                elif(PayoutTable[num][1][0]==Bets[bet][0]):
                    #print("Bet Matches Team 2 of Game: ")
                    GameTotal = PayoutTable[num][0][1]+PayoutTable[num][1][1]
                    #print(str(Bets[bet]) + " Won") 
                    if(PayoutTable[num][0][1]!=0):
                        FinalBefore2 = (Bets[bet][1]/PayoutTable[num][1][1])
                        FinalP2 = Bets[bet][1]+((Bets[bet][1]/PayoutTable[num][1][1])*PayoutTable[num][0][1])
                        percent = FinalP2*0.95
                    else:
                        FinalBefore2 = 0
                        FinalP2 = 0
                        percent = FinalP2*0.95
                    #print(str(Bets[bet][1])+" + ( "+str(Bets[bet][1])+" / "+str(PayoutTable[num][1][1])+") = ("+str(FinalBefore2)+" * "+str(PayoutTable[num][0][1])+") = "+str(FinalP2))
                    equation = (str(Bets[bet][1])+" + ( "+str(Bets[bet][1])+" / "+str(PayoutTable[num][1][1])+") = ("+str(FinalBefore2)+" * "+str(PayoutTable[num][0][1])+") = "+str(FinalP2)+" -> "+str(FinalP2)+" * .95 --> Payout of "+str(percent)+" | Profit of: +"+str(percent-Bets[bet][1]))
                    #FinalGameTotal = GameTotal + FinalP
                    
                    FinalGameTotal2 = FinalGameTotal2 + FinalP2
                    FinalPayouts.append((Bets[bet][2],Bets[bet][1],Bets[bet][0],FinalP2,equation))
                    break

    if(FinalGameTotal2-1<=FinalGameTotal1 and FinalGameTotal2+1>=FinalGameTotal1):
        print("\nNOTE: Should be +- 1 of each other")
        print("BetSumBefore: "+str(FinalGameTotal2)+" | BetSumAfter: "+str(FinalGameTotal1))

        print("\nToatal ammount dispersed: "+str(FinalGameTotal2))
        print(str("Network Profit  5%   $"+str(FinalGameTotal1*.05))+"\n")
        print(str("Network Profit  7%   $"+str(FinalGameTotal1*.07))+"\n")
        print(str("Network Profit: 9%   $"+str(FinalGameTotal1*.09))+"\n")
        print(str("Network Profit  10%  $"+str(FinalGameTotal1*.10))+"\n")
        print(str("Network Profit: 15%  $"+str(FinalGameTotal1*.15))+"\n")
        
    else:
        print("FinalGameTotal2: "+str(FinalGameTotal2)+" | FinalGameTotal1: "+str(FinalGameTotal1))
        print("Check your code, ammounts at end not equal")

    return FinalPayouts

def InitilizePayoutTable(PayoutTable, NumGames, Games):
    for num in range(NumGames):
        PayoutTable.append([[str(Games[num][0]),0],[str(Games[num][1]),0]])
    return PayoutTable

def PickRandomName(x):
    if(x==1):
        return "Elk"
    elif(x==2):
        return "Blazers"
    elif(x==3): 
        return "Geese"
    elif(x==4):
        return "Fish"
    elif(x==5):
        return "Humans"
    elif(x==6):
        return "No Name"
    else:
        return ("Team"+str(x))

def PrintGames(Games):
    count = 1
    count2 = 2
    print(" ______________________________________________________\n/\n|")
    print("| Games Table: -> Games: "+str(len(Games))+" | Number of Teams: "+str(len(Games)*2)+"\n|")
    for num in range(len(Games)):
        print("|   Game "+str(num+1)+": \n|\tTeam "+str(count)+": "+str(Games[num][0])+ "\t\tvs\t\tTeam "+str(count2)+": "+str(Games[num][1]))
        count = count + 2
        count2 = count2 + 2
    print("|\n|\n\___________________________________________________")

def PrintBets(Bets):
    print(" ______________________________________________________\n/\n|")
    print("| All Bets: -> Total of #"+str(len(Bets))+" Bets\n|")
    for num in range(len(Bets)):
        print("|   Bet #"+str(num+1)+": "+str(Bets[num]))
    print("|\n|\n\___________________________________________________")

def PrintPayoutTable(PayoutTable, Total):
    #PrintThis(PayoutTable)
    print(" ______________________________________________________\n/\n|")
    print("| Payouts: -> Total of $ in Pool: "+str(Total)+"\n|")
    for num in range(len(PayoutTable)):
        GameTotal = PayoutTable[num][0][1]+PayoutTable[num][1][1]
        if(GameTotal!=0):
            Odds1 = (PayoutTable[num][0][1]/GameTotal)*100
            Odds2 = (PayoutTable[num][1][1]/GameTotal)*100
        else:
            Odds1 = 0
            Odds2 = 0

        print("|   Game #"+str(num+1)+" total $ in game: "+str(GameTotal)+"\n|      "+str(PayoutTable[num][0][0])+": "+str(PayoutTable[num][0][1])+" or "+str(Odds1)+"%\t\t"+str(PayoutTable[num][1][0])+": "+str(PayoutTable[num][1][1])+" or "+str(Odds2)+"%")
    print("|\n|\n\___________________________________________________")

def SavePayoutTable(PayoutTable, Total):
    #PrintThis(PayoutTable)
    filename = open("PayoutsTable.out",'w')
    filename.write(" ______________________________________________________\n/\n|")
    filename.write("| Payouts: -> Total of $ in Pool: "+str(Total)+"\n|")
    for num in range(len(PayoutTable)):
        GameTotal = PayoutTable[num][0][1]+PayoutTable[num][1][1]
        if(GameTotal!=0):
            Odds1 = (PayoutTable[num][0][1]/GameTotal)*100
            Odds2 = (PayoutTable[num][1][1]/GameTotal)*100
        else:
            Odds1 = 0
            Odds2 = 0

        filename.write("|   Game #"+str(num+1)+" total $ in game: "+str(GameTotal)+"\n|      "+str(PayoutTable[num][0][0])+": "+str(PayoutTable[num][0][1])+" or "+str(Odds1)+"%\t\t"+str(PayoutTable[num][1][0])+": "+str(PayoutTable[num][1][1])+" or "+str(Odds2)+"%")
    filename.write("|\n|\n\___________________________________________________")


def PrintThis(x):
    for num in range(len(x)):
        print(x[num])
    
def PrintPayout(Payout):
    for num in range(len(Payout)):
        print("Wallet ID: "+str(Payout[num][0])+" bet "+str(Payout[num][1])+" on Team "+str(Payout[num][2])+" payout was "+str(Payout[num][3]))

def PrintPayoutEquations(Payout):
    for num in range(len(Payout)):
        print("Bet #"+str(Payout[num][0])+" equation: "+str(Payout[num][4]))

def SavePayoutResults(Payout):
    filename = open("Payouts.out",'w')
    filename2 = open("PayoutEquations.out",'w')
    for num in range(len(Payout)):
        filename2.write("Bet #"+str(Payout[num][0])+" equation: "+str(Payout[num][4])+"\n")
        filename.write("Bet #"+str(Payout[num][0])+" equation: "+str(Payout[num][4])+"\n")

    filename.close()
    filename2.close()

#
################################
#NFL 2018 functions
#
def ReturnTeamsInWeekOrder():

    Games = []
    #Open Teams All file and Read Teams into an Array
    #
    FileArray = []
    Count = 0
    with open("../NFL2018Schedule/NFLScheduleByWeek/All/allGames.txt") as f:
        for line in f:
            FileArray.append(line.rstrip('\n'))
            #print("NFL @"+str(Count)+": "+str(FileArray[Count])) 
            Count = Count + 1
            # Do something with 'line'


    Team1 = []
    Team2 = []
    x = int(len(FileArray))
    for num in range(0,x,2):
        Team1.append(FileArray[num])
        Team2.append(FileArray[num+1])
        #        print(Team1[num])
        #        print(Team2[num+1])

    for num in range(len(Team1)):
        Games.append((Team1[num],Team2[num]))

    PrintGames(Games)
    return Games
'''
##########################################
#Tools:

Open file and read in line by line.
with open(...) as f:
        for line in f:
                # Do something with 'line'
'''
