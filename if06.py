def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1=n%10
    n//=10
    n2=n%10
    n//=10
    n3=n%10
    n//=10
    n4=n%10
    n5=n//10
    mx=n1
    idx=1
    if n2>mx:
        mx=n2
        idx+=1
    if n3>mx:
        mx=n3
        idx+=1
    if n4>mx:
        mx=n4
        idx+=1
    if n5>mx:
        mx=n5 
        idx+=1  
    return idx
   