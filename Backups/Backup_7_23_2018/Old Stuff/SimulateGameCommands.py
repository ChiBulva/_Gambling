def main():
	print("Worked!")

def AddGameFile(filenameGames):
    Games = []
    
    print("Adding: "+str(filenameGames))
    
    GamesFile = open(filenameGames, 'r')
    
    Games1 = GamesFile.read()
    GamesFile.close()

    
    print_array = []
    counter = 0
    with open('Games','r') as f:
        for line in f:
            print_array.append(line)
            Games.append(line)
            print("PrintArray["+str(counter)+"]: "+str(print_array[counter]))
            counter = counter + 1



    return Games

def ParseGamesFile(GamesFile):
    print("Entering ParseGamesFile: \n")
    Games = []
    for num in range(len(GamesFile)):
#        print(num)
        Games.append(GamesFile[num][5])
        Games.append(GamesFile[num][8])
        Games.append(GamesFile[num][12])


    return Games

def PrintGames(Games):
    #print(len(Games))

    for num in range(0,len(Games),3):
        print("Game #"+Games[num]+" --> "+Games[num+1]+" vs "+Games[num+2])

    print("\n\n")

