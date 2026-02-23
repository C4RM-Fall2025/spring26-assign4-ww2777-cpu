def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    cf = face * couponRate/ppy
    pvsum=0
    wtsum=0
    for i in range(1,periods+1):
        discount=(1+y/ppy)**(-i)
        pvsum += cf * discount
        wtsum += cf * discount * i
    pvsum += face * (1+y/ppy)**(-periods)
    wtsum += face * (1+y/ppy)**(-periods) * periods
    return((wtsum/pvsum)/ppy)

    

