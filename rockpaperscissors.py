
"""
This is a simple user input Rock, Paper, Scissors game.
.upper() is used so that a player can type Rock Paper Scissors in all Capital or lower case or the combination.
"""
# Welcome Message for The Players
print('Hey Players!')
print('Welcome to Rock,Paper, and Scissors game. The rules are simple choose any' +
      ' between Rock, Paper or Scissor and let the other player to choose.'+'\nPlayers first to make 3 wins count is a Ultimate Winner')
print('Rule:')
print('1.Scissors beat Paper.' + '\n2.Paper beats Rock \n3.Rock beats Scissors.')

while True:
    count1 = 0
    count2 = 0
    x = input('Y to proceed and N to exit. ')
    if x == 'N' or x == 'n':
        break
    elif x == 'Y' or x == 'y':
        choiceA = []
        choiceB = []
        while (count1 < 3) and (count2 < 3):
            choice1 = input("Player 1 Make your choice Rock, Paper or Scissors:")
            player1 = choice1
            choice2 = input("Player 2 Make your choice Rock, Paper or Scissors:")
            player2 = choice2
            while (player1.upper() != 'ROCK' and player1.upper() != 'PAPER' and player1.upper() != 'SCISSORS'):
                print(player1)
                player1 = input("Invalid choice. Player 1! Make your choice Rock, Paper or Scissors:")

            while (player2.upper() != 'ROCK' and player2.upper() != 'PAPER' and player2.upper() != 'SCISSORS'):
                print(player2)
                player2 = input("Invalid choice. Player 2! Make your choice Rock, Paper or Scissors:")

            if (player1.upper() == 'ROCK' and player2.upper() == 'SCISSORS') or (player1.upper() == 'PAPER' and player2.upper() == 'ROCK') or (
                    player1.upper() == 'SCISSORS' and player2.upper() == 'PAPER'):
                count1 += 1

            elif (player1.upper() == 'ROCK' and player2.upper() == 'PAPER') or (player1.upper() == 'PAPER' and player2.upper() == 'SCISSORS') or (
                    player1.upper() == 'SCISSORS' and player2.upper() == 'ROCK'):
                count2 += 1

            else:
                print("Draw!")

            print("Number of wins")
            print("Player1 :")
            print(count1)

            print("\nPlayer2 :")
            print(count2)
            choiceA.append(choice1.upper())
            choiceB.append(choice2.upper())
    else:
        print("Invalid Input.")

    if count1 == 3 or count2 == 3:
        print("Player1 wins")
        count1 == 0;
        count2 == 0;
        print("Choices made by Player 1 in order:")
        print(choiceA)
        print("Choices made by Player 2 in order:")
        print(choiceB)
 
print("Thank you for playing.")












