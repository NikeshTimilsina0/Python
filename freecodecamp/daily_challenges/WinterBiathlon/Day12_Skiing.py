def check_eligibility(athlete_weights, sled_weight):
    """2026 Winter Games Day 12: Bobsled
Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by itself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team
The total weight of the bobsled (athletes plus sled) must not exceed:

247 kg for a 1-person team
390 kg for a 2-person team
630 kg for a 4-person team
Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements."""
    team_size=len(athlete_weights)
    total_weight=sum(athlete_weights)+sled_weight
    print((team_size,total_weight))
    print(athlete_weights,sled_weight)
    requirements={
        1:(162,247),
        2:(170,390),
        4:(210,630)
    }
    if team_size not in requirements:
        return 'Not Eligible'
    min_sled,max_weight=requirements[team_size]
    print(min_sled,max_weight)
    if sled_weight>=min_sled and total_weight<=max_weight:
        return "Eligible"
    return 'Not Eligible'
print(check_eligibility([110, 102, 90, 106], 222))
print(check_eligibility([106, 99, 103, 96], 227))