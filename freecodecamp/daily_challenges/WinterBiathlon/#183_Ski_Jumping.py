def ski_jump_medal(distance_points, style_points, wind_compensation, k_point_bonus):
    my_score = distance_points + style_points + wind_compensation + k_point_bonus
    other_scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    better_than_me = [s for s in other_scores if s > my_score]
    rank = len(better_than_me) + 1
    
    if rank == 1:
        return "Gold"
    elif rank == 2:
        return "Silver"
    elif rank == 3:
        return "Bronze"
    else:
        return "No Medal"

test_cases = [
    (125.0, 58.0, 0.0, 6.0),
    (119.0, 50.0, 1.0, 4.0),
    (122.0, 52.0, -1.0, 4.0),
    (118.0, 50.5, -1.5, 4.0),
    (124.0, 50.5, 2.0, 5.0),
    (119.0, 49.5, 0.0, 3.0)
]

results = [ski_jump_medal(*tc) for tc in test_cases]
print(results)