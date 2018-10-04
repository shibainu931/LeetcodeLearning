def carFleet(pos, speed, target):
    times = [float((target - p))/s for p, s in sorted(zip(pos, speed)) ]
    res = 0 
    curr = 0 
    for t in times[::-1]:
        if t > curr:
            curr = t 
            res += 1
    return res 