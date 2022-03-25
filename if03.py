def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    
    mx=a
    mn=a
    if b>mx:
        mx=b
    if c>mx:
        mx=c

    if b<mn:
        mn=b
    if c<mn:
        mn=c
    sum_digit=a+b+c
    ls=sum_digit-(mx+mn)
    return ls            
print(main(18,7,10))