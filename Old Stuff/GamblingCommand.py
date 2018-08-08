import SimulateGameCommands

### List of Commands to simulate a Game or series of games
#
#   Finished Commands:
#           
#   Working on: LoadGames(Filename, ...), 
#
#_________________________________________________________
SimulateGameCommands.main()

### Variables that will hold information of the Simulated Network 
#
#   Games: Array that will hold 
#           
#   Working on: 
#
#_________________________________________________________

##Games: Null
Games = []  ##Games: Null
Bets = []   #List of integers to add to find current Bet ammount
BetsR = []  #List of integers to add to find current Bet ammount for Right Team
BetsL = []  #List of integers to add to find current Bet ammount for Left  Team

ExitOrNahh = 1 #used to exit or nahh
while(ExitOrNahh==1):
    print("Would you like to...\nType: '1' to Enter a file name\nType: '2' to Enter a game manually\nType '0' to exit")
    #Choice
    choice = raw_input(":")
    if(choice=='1'):
        print("\nWhat is the Filename?")
        filename = raw_input(":")
        GamesFile = SimulateGameCommands.AddGameFile(filename)
        Games = SimulateGameCommands.ParseGamesFile(GamesFile)
#        print("\nGames:\n"+str(Games))
        SimulateGameCommands.PrintGames(Games)

    elif(choice=='2'):
        print("\nEntered Manually")
    
    elif(choice=='0'):
        ExitOrNahh = 0 
    else:
        print("Else!!!\n\n")
