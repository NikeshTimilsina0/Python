def calculate_penalty_distance(rounds):
    #5 targets per round
    #missed target results in 150m penalty loop
    penalty=0

    for num in rounds:
        if (5-num)==0:
            penalty+= 0
        else:
            penalty+=(5-num)*150

    return penalty