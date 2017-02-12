# this is based on the tic_tac_toe game I made, but the method of locating each cell on the grid is based on matrix,
# so that the grid can technically be unlimited (something else need to be changed)

def win_checker(player_name):
    global game_record
    global win_checker_handler
    global runner

    winner = ""

    # i represents columns; j represents rows
    for i in range(3):
        for j in range(2):
            if game_record[i][j] == game_record[i+1][j] == game_record[i+2][j] == game_record[i+3][j] and game_record[i][j] != " ":
                win_checker_handler = True
                runner = False
                break
            elif game_record[i][j] == game_record[i][j+1] == game_record[i][j+2] == game_record[i][j+3] and game_record[i][j] != " ":
                win_checker_handler = True
                runner = False
                break
            elif game_record[i][j] == game_record[i+1][j+1] == game_record[i+2][j+2] == game_record[i+3][j+3] and game_record[i][j] != " ":
                win_checker_handler = True
                runner = False
                break
            elif game_record[i][j+3] == game_record[i+1][j+2] == game_record[i+2][j+1] == game_record[i+3][j] and game_record[i][j+3] != " ":
                win_checker_handler = True
                runner = False
                break
            else:
                continue

    if win_checker_handler == True:
        winner = player_name
        print "\nThe winner is " + winner + "! Congratulations!"


def playagain ():
    global play_again_handler
    while True:
        play_again = raw_input("\nDo you want to play again?(y or n)")
        if play_again == "n":
            play_again_handler = False
            break
        elif play_again == "y":
            break
        else:
            continue


def print_location():
    global game_record

    print "--- " * 7
    print " %d   %d   %d   %d   %d   %d   %d" % (1, 2, 3, 4, 5, 6, 7)
    print "--- " * 7
    print " %s | %s | %s | %s | %s | %s | %s" % (game_record[0][5], game_record[1][5], game_record[2][5], game_record[3][5], game_record[4][5], game_record[5][5], game_record[6][5])
    print "--- " * 7
    print " %s | %s | %s | %s | %s | %s | %s" % (game_record[0][4], game_record[1][4], game_record[2][4], game_record[3][4], game_record[4][4], game_record[5][4], game_record[6][4])
    print "--- " * 7
    print " %s | %s | %s | %s | %s | %s | %s" % (game_record[0][3], game_record[1][3], game_record[2][3], game_record[3][3], game_record[4][3], game_record[5][3], game_record[6][3])
    print "--- " * 7
    print " %s | %s | %s | %s | %s | %s | %s" % (game_record[0][2], game_record[1][2], game_record[2][2], game_record[3][2], game_record[4][2], game_record[5][2], game_record[6][2])
    print "--- " * 7
    print " %s | %s | %s | %s | %s | %s | %s" % (game_record[0][1], game_record[1][1], game_record[2][1], game_record[3][1], game_record[4][1], game_record[5][1], game_record[6][1])
    print "--- " * 7
    print " %s | %s | %s | %s | %s | %s | %s" % (game_record[0][0], game_record[1][0], game_record[2][0], game_record[3][0], game_record[4][0], game_record[5][0], game_record[6][0])

def make_a_move(player_name, draw):
    global game_record
    global runner
    global round_counter
    global row_conunter

    player_input = ""
    input_checker = False

    if runner == True:
        while input_checker == False:
            while True:
                player_message = raw_input("\n"+player_name + ", what column do you want to draw an " + draw + "? (1~7)")
                if player_message not in ["1", "2", "3", "4" ,"5", "6", "7"]:
                    print "\nNot a number. Please put in a number\n"
                else:
                    player_input = int(player_message) - 1
                    break
            while True:
                if " " not in game_record[player_input]:
                    print "\nThe position is already taken.\n"
                    player_message = raw_input("\n"+player_name + ", what column do you want to draw an " + draw + " ? (1~7)")
                    break
                else:
                    input_checker = True
                    break
        round_counter += 1
        #the first index is the column, the second index is the current row.
        game_record[player_input][row_counter[player_input]] = draw
        row_counter[player_input] +=1
        print_location()
        win_checker(player_name)
        if win_checker_handler == True:
            playagain()
            runner = False


def game():

    global game_record
    global win_checker_handler
    global play_again_handler
    global runner
    global round_counter
    global row_counter

# reset game_data
    round_counter = 0
    row_counter = 0
    win_checker_handler = False
    # game_record is the status of how each cell
    game_record = [[" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "]]
    # if player makes a move, the column input's will change the value of its index of the row_counter
    row_counter = [0, 0, 0, 0, 0, 0, 0]
    play_again_handler = True
    # control the game running status, in order to break out nested loops
    runner = True


    print "\nCONNECT FOUR"

    print_location()

    print "\n"

    player_a_name = raw_input("\nIf you want to go first, tell me your name?")

    print "\nwelcome, " + player_a_name + "!\n"

    player_b_name = raw_input("\nwhat's the second player's name?")

    print "\nwelcome, " + player_b_name + "!\n"

    print_location()

    while runner == True:

        if runner == True:
            make_a_move(player_a_name, "O")

        if runner == True:
            if round_counter >= 42:
                print " \nNobody won. Game Over!"
                playagain()
                runner = False
                break

        if runner == True:
            make_a_move(player_b_name, "X")


        if runner == True:
            if round_counter >= 42:
                print " \nNobody won. Game Over!"
                playagain()
                runner = False
                break

play_again_handler = True

while True:
    if play_again_handler == True:
        game()
    if play_again_handler == False:
        print "Bye!"
        break
