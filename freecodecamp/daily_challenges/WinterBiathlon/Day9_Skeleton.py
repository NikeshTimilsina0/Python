"""2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment
Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200"""
def get_difficulty(track):
    total=0
    for i in range(len(track)):
        # print(i)
        if i+1>=len(track):#if the next index is more than the length of track it might go out of bounds so handling it.
                break
        if track[i]=='S':
            total+=0
        if track[i]=='L':
            #if turn add 15 else 5
            if track[i+1]=='R':
                total+=15
            else:
                total+=5
        if track[i]=='R':
            #if turn add 15 else 5
            if track[i+1]=='L':
                total+=15
            else:
                total+=5
    print(total)
    if total>0 and total<=100:
        return 'Easy'
    if total>100 and total<=200:
        return "Medium"
    if total>200:
        return 'Hard'
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))
print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))