def merge_bookings(B1,B2):
    n1,n2,i1,i2 = len(B1),len(B2),0,0
    B = []
    x = 0
    while i1+i2<n1+n2:
        if i1<n1:
            k1, s1, t1 = B1[i1]
        else:
            k1, s1, t1 = 0,0,0
        if i2<n2:
            k2, s2, t2 = B2[i2]
        else:
            k2, s2, t2 = 0,0,0
        if i1 == n1:
            k,s,x = k2,max(s2,x),t2
            i2 += 1
        elif i2 == n2:
            k,s,x = k1,max(s1,x),t1
            i1 += 1
        else:
            if x < min(s1,s2):
                x = min(s1,s2)
            if t1 < s2:
                k,s,x = k1,max(x,s1),t1
                i1 += 1
            elif t2 < s1:
                k,s,x = k2,max(x,s2),t2
                i2 += 1
            elif x < s1:
                k,s,x = k2,x,s1
            elif x < s2:
                k,s,x = k1,x,s2
            else:
                k,s,x = k1+k2,x,min(t1,t2)
                if x ==t1: i1 += 1
                if x ==t2: i2 += 1
        if s != x:
            B.append((k,s,x))
            
    B_ = [B[0]]
    for k,s,t in B[1:]:
        k_,s_,t_ = B_[-1]
        if k_ == k and t_ == s:
            B_.pop()
            s = s_
        B_.append((k,s,t))
    return B_
            
def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
              
    '''
    B = []
    if len(R) == 1:
        s,t = R[0]
        return ((1, s, t),)
    m = len(R) // 2
    Rl = R[:m]
    Rr = R[m:]
    Bl = satisfying_booking(Rl)
    Br = satisfying_booking(Rr)
    B = merge_bookings(Bl,Br)
    
    return tuple(B)
