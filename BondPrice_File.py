def getBondPrice(y, face, couponRate, m, ppy):
    periods=m*ppy
    cf=face*couponRate/ppy
    pvsum=0
    for i in range(1,periods+1):
        discount=(1+y/ppy)**(-i)
        pvsum=pvsum+cf*discount

    pvsum += face*(1+y/ppy)**(-periods)
    return(pvsum)
    

