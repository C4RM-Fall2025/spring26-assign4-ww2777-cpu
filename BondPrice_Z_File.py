def getBondPrice_Z(face, couponRate, times, yc):
    cf=face*couponRate
    pvsum=0
    for x,y in zip(times, yc):
        discount=(1+y)**(-x)
        pvsum += cf*discount
    pvsum += face*(1+yc[-1])**(-times[-1])
    return(pvsum)

