print("Gambling Network: Example")

#GamesFileName = raw_input("Name of Games file: ")
GamesFileName = "Games"
fG = open(GamesFileName, 'r')
Games = fG.read()
print(Games)
fG.close()

data_array = []


#for tok in Games:
#    print(tok)

print_array = []
counter = 0
with open('Games','r') as f:
        for line in f:
            print_array.append(line)
            print("PrintArray["+str(counter)+"]: "+str(print_array[counter]))
            counter = counter + 1
'''            
            for word in line.split():
#                    print(counter)
                    if(counter%2==0 or counter%3==0 or counter%5==0):
                        print_array.append(str(word)+", ")
#                    print(counter)
                    counter = 1+counter
#                    print(word)
'''



Ammount_Of_Games = len(print_array)
print("Ammount of games: " + str(Ammount_Of_Games))

Game_Pools = []
count = 1
leftTeams = []
rightTeams = []
leftTeamsAmmount = []
rightTeamsAmmount = []
for target in range(Ammount_Of_Games):
    leftTeams.append(print_array[target][count*8])
    rightTeams.append(print_array[target][count*12])
    leftTeamsAmmount.append(int(0))    
    rightTeamsAmmount.append(int(0))    
#   print("Target at "+str(target)+": "+str("1->"+print_array[target][count*8]+" 2->"+print_array[target][count*12]))

leftTeamsAmmount[0] = 10

count = 1
ammountCount = 0
for target in range(Ammount_Of_Games):
    print("Game 1: Team: "+str(leftTeams[target])+" vs "+str(rightTeams[target]))
    print("     Team "+str(leftTeams[target])+": left->"+str(leftTeamsAmmount[target])+" Team "+str(rightTeams[target])+": right->"+str(rightTeamsAmmount[target]))
    count = count + 1
    ammountCount = ammountCount + 2

#for tok in range(len(print_array)):
#    print(print_array[tok])

'''

#BetFileName = raw_input("Name of Bets file: ")
BetFileName = "Bets"
fB = open(BetFileName, 'r')
Bets = fB.read()
print(Bets)
fB.close()
'''
BetsNum = 1
Gamble = 1
Current = []

while(Gamble==1):
    print("Would you like to make a bet? \nType 'Bet' to make a bet\nType 'File' to add a bunch of bets\nType 'Current' to see current bets\nType anything else for no!!")
    choice = raw_input(": ")
    if(choice=="Bet"):
        print("Current Games")
        print(Games)

        #Current Bet Position for later reference
        Bet = BetsNum
        BetsNum = BetsNum + 1 #Increment for next bet
        #Game to bet on
        Game = raw_input("\nGame (1,2,...,N)   : ")
        #Team to bet on
        Team = raw_input("\nTeam (1,2,...,N)   : ")
        #Ammount to bet
        Ammount = raw_input("\nAmmount (1,2,...,N): ")
        #Wallet id for better
        WalletID = raw_input("\nWalletID(1,2,...,N): ")

        print("Bet: " + str(Bet) + " | Game: " + str(Game) + " | Team: " + str(Team) + " | Ammount: $" + str(Ammount) + " | WalletID: " + str(WalletID) + "\n")


    elif(choice=="File"):
        BetFileName = raw_input("\nBet FileName: ")
        fB = open(BetFileName, 'r')
        Bets = fB.read()
        print(Bets)
        fB.close()
