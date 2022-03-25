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
        idx+=1
    if n3>mx:
        idx+=1
    if n4>mx:
        idx+=1
    if n5>mx:
        idx+=1  
    return idx
   