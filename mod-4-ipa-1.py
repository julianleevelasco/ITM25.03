'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #TRUE-OR-FALSE
    First_Statement = to_member in social_graph[from_member]['following'] 
    Second_Statement = from_member in social_graph[to_member]['following']
    #IF-STATEMENTS
    if First_Statement == 1 and Second_Statement == 1:
        status = 'friends'.title()
    elif First_Statement == 1 and Second_Statement == 0:
        status = 'follower'.title()
    elif First_Statement == 0 and Second_Statement == 1:
        status = 'followed'.title() + ' ' + 'by'
    elif First_Statement == 0 and Second_Statement == 0:
        status = 'no relationship'.title()
    #RELATIONSHIP-STATUS
    return status

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    x_win = ['X'] * len(board)
    o_win = ['O'] * len(board)
    slant1 = []
    slant2 = []
    test = []
    row = []
    #HORIZONTAL
    for i in board:
        test.append(i)
    #SLANT
    i = 0
    while i < len(board):
        slant1.append(board[i][i])
        i += 1
    test.append(slant1)
    ###
    i = 0
    j = len(board[i]) - 1
    while i < len(board):
        slant2.append(board[i][j])
        i += 1
        j -= 1
    test.append(slant2)
    #VERTICAL
    for i in board:
        row.extend(i)
    for i in range(len(board)):
        test.append(row[i::len(board)])
    #FINAL
    if x_win in test:
        winner = "X"
    elif o_win in test:
        winner = "O"
    else:
        winner = "NO WINNER"
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    final_time = 0
    if (first_stop, second_stop) in route_map:
        travel_time = route_map[(first_stop, second_stop)]["travel_time_mins"]
        final_time = travel_time
    else:
        keys = route_map.keys()
        key_list = list(keys)
        for i in range(0,len(route_map)):
            if key_list[i][0] is first_stop:
                travel_time = route_map[key_list[i]]["travel_time_mins"]
                final_time += travel_time
                i += 1
                if i >= len(route_map):
                    i = 0
                while key_list[i][1] is not second_stop:
                    travel_time = route_map[key_list[i]]["travel_time_mins"]
                    final_time += travel_time
                    i += 1
                    if i >= len(route_map):
                        i = 0
            elif key_list[i][1] is second_stop:
                travel_time = route_map[key_list[i]]["travel_time_mins"]
                final_time += travel_time
    return final_time