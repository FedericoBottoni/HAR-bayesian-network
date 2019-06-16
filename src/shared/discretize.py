 
def discretize(val, rng):
    if val % rng != 0:
        if val < 0:
            discVal = val + (rng - (val % rng))
        else:
            discVal = val - val % rng
    else:
        discVal = val
    return discVal