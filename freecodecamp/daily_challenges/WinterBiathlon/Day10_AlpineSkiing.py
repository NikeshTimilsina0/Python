def get_hill_rating(drop, distance, hill_type):
    """2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25"""
    steepness=drop/distance
    print(steepness)
    if hill_type=='Downhill':
        adjustedsteepness=steepness*1.2
    elif hill_type=='Slalom':
        adjustedsteepness=steepness*0.9
    else:
        adjustedsteepness=steepness*1.0
    print(adjustedsteepness)
    if adjustedsteepness<=0.1:
        return 'Green'
    elif adjustedsteepness>0.1 and adjustedsteepness<=0.25:
        return 'Blue'
    else:
        return 'Black'
print(get_hill_rating(95, 900, "Slalom"))
print(get_hill_rating(620, 2800, "Downhill"))
print(get_hill_rating(420, 1680, "Giant Slalom"))