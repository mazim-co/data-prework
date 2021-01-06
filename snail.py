well_height = 125
daily_distance = 30
nigthly_distance = -20
snail_postion = 0

days = 0

total_distance_per_day = daily_distance + nigthly_distance
snail_not_done = True
while snail_not_done:
    snail_postion += total_distance_per_day
    days += 1
    if snail_postion >= well_height:
        snail_not_done = False
print("The snail needs", days, "days to finish the wall.")