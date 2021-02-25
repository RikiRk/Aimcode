def search(seq,key):
    input(seq)
    lo=0
    hi= len(seq)-1
    while hi>=lo:
        mid=lo+(hi-lo)
        if seq[mid]<key: 
             lo=mid+1
        elif seq[mid]>key:
            lo=mid-1
        else:
            return mid
    return False             