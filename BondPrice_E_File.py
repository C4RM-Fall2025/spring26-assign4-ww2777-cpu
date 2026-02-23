def getBondPrice_E(face, couponRate, m, yc):
    cf=face*couponRate
    pvsum=0
    ycc=list(yc)
    for t, rate in enumerate(ycc):
        discount=(1+rate)**(-(t+1))
        pvsum += cf*discount
    pvsum += face*(1+ycc[-1])**(-m)
    return(pvsum)

