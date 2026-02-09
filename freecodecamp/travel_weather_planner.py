distance_mi=20
is_raining=False
has_bike=True
has_car=True
has_ride_share_app=True

if distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi<=6:
    if not is_raining and not has_bike:
        print(False)
    elif is_raining and not has_bike:
        print(False)
    else:
        print(True)
elif distance_mi>6:
    if has_ride_share_app:
        print(True) 
    elif has_car:
        print(True)
    else:
        print(False)