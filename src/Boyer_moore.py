
def boyer(board,pattern,avail_move,priority_score):

    num_board = len(board)
    num_pattern = len(pattern)

    j = num_pattern -1 # text index

    #count how many matches made
    match_count = 0

    #count how many indexes were matched
    counter = 0

    #stop loop by changing to True as certain condition met
    stop_loop = False

    # set move
    shift_move = avail_move



    if shift_move:
        #resets pattern index
        i = num_pattern -1 # pattern index
        counter = 0

        # if board not big enough to fit in pattern list, break the loop
        if num_pattern*2 >= num_board:
            return -1

        # if match while there's still elements to match
        # shift the board index to match the
        while i >=0 and pattern[i] == board[shift_move+i]:
            counter += 1
            #print("match counter: ",counter , "element:",pattern[i])
            i -=1

            # #stop loop as it matches last two index
            ## [0][any number*]
            # first col = empty hole
            # second col = seeds to grab
            if counter == 2:
                stop_loop = True

        # if ran out of pattern index to move, return where shift_move is
        if i < 0 or stop_loop:
            #return shift_move
            return priority_score

        #if can continue
        else:
            # skip to matched index between pattern and board
            if board[shift_move+num_pattern-1] in pattern:
                shift_move+= num_pattern - pattern.index(board[shift_move+num_pattern -1]) -1

            # skip entire indexes of board list same length as pattern length
            else:
                shift_move+=num_pattern

        match_count+=1

    #if no matches found, return -1
    return -1



# use pattern matching to see if seeds will be allocated to player board, or back to opponent's
def check_next_row(board,pattern,avail_move):

    num_board = len(board)
    num_pattern = len(pattern)

    j = num_pattern -1 # text index

    # set move
    shift_move = avail_move

    if shift_move:
        #resets pattern index

        i = num_pattern -1 # pattern index

        # if ran out of pattern index to move, return where shift_move is
        # print("num pat:",num_pattern+avail_move)
        # print("half board",num_board/2)

        #check if seeds allocated to player side
        if num_pattern+avail_move > num_board/2 and num_pattern+avail_move < num_board:
            return 5

        # check if seeds allocated to player side
        if num_pattern+avail_move > num_board/2:
            return 6

        # fill any possible 0 seeds hole
        if board[num_pattern+avail_move] == 0:
            return 7

        # if board not big enough to fit in pattern list
        if num_pattern*2 >= num_board:
            return 7

        #if can continue
        else:
            # skip to matched index between pattern and board
            if board[shift_move+num_pattern-1] in pattern:
                shift_move+= num_pattern - pattern.index(board[shift_move+num_pattern -1]) -1

            # skip entire indexes of board list same length as pattern length
            else:
                shift_move+=num_pattern

    #if large index found, return 6
    return 1


# if __name__ == '__main__':
#
#     board   = [1,2,4,6,5,3,3,3,0,3,3]
#     pattern = [1,0,3]
#
#     #pattern = [1,1,1,0,3]
#
#
#     print(' %s' % board)
#     p = boyer(board,pattern,7)
#     print(' %s%s' % ('*.*'*p,pattern))
#     print(p)
