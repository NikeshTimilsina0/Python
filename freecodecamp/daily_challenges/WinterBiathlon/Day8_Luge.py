"""2026 Winter Games Day 8: Luge
Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.

The track is divided into the following segments:

Segment 1: 320 meters
Segment 2: 280 meters
Segment 3: 350 meters
Segment 4: 300 meters
Segment 5: 250 meters
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.

To calculate the speed (in meters per second) for a segment, divide the distance by the time.

Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, rounded to two decimal places, and Y is the segment number where the fastest speed occurred."""
def get_fastest_speed(times):
    segments=[320,280,350,300,250]
    speed=[]
    for i in range(len(times)):
        diff=segments[i]/times[i]
        speed.append(diff)
    print(speed)
    return f"The luger's fastest speed was {max(speed):.2f} m/s on segment {speed.index(max(speed))+1}."
print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))
print(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]))