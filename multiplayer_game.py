
choices = []
for pos in range(0,9):
    choices.append(str(pos+1))

#creating the boolean variable
Is_Current_One = True #default player is player X

#at first we don't have any winner
won = False

while not won:
    #first move is done by player X
    print('\n')
    print('|{}|{}|{}'.format(choices[0],choices[1],choices[2]))
    print('-----------------------')
    print('|{}|{}|{}'.format(choices[3],choices[4],choices[5]))
    print('-----------------------')
    print('|{}|{}|{}'.format(choices[6],choices[7],choices[8]))

    if Is_Current_One:
        print("Player X")
    else:
        print("Player O")

    #checking the input whether player is entering string    
    try:
        choice = int(input("Enter any Number 0-8 > "))
    except:
        print("Please enter only valid fields from board (0-8)")
        continue

    #checking position is already occupied by other users
    if choices[choice-1] != str(choice):
        print("This {} position is already Occupied by {}, please choose another Position ".format(choice,choices[choice-1])) 
        continue
    
    if Is_Current_One:
        choices[choice-1] = 'X'
    else:
        choices[choice-1] = 'O'

    Is_Current_One = not Is_Current_One

    #logic to make the player to winner
    for pos_x in range(0,3):
        pos_y = pos_x * 3

        #for row conditition
        if(choices[pos_y] == choices[(pos_y +1)]) and (choices[pos_y] == choices[(pos_y + 2)]):
            #code to change win True
            won = True #while loop will break

        #for column conditition 
        if(choices[pos_x] == choices[(pos_x + 3)]) and (choices[pos_x] == choices[(pos_x + 6)]):
            won = True

        #For Diagonal condition here
        if((choices[0] == choices[4]) and (choices[0] == choices[8])) or ((choices[2] == choices[4]) and (choices[2] == choices[6])):
                won = True
            
#print Who is winner
print("Player " +str( int(Is_Current_One + 1) ) + " Won, Congratulation!")
