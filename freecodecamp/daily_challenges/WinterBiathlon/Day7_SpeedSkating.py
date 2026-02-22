"""2026 Winter Games Day 7: Speed Skating
Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.

The first element of each array corresponds to lap 1, the second to lap 2, and so on."""
def largest_difference(skater1, skater2):
    skater=[]
    for i in range(len(skater1)):
        diff=abs(skater1[i]-skater2[i])
        skater.append(diff)
    
    print(max(skater))
    print(skater)
    max_index=skater.index(max(skater))
    print(max_index+1)
    return max_index+1
largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30])
largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95])