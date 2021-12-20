def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    l1  = []
    l2 = []
    l1[:0] = f"{num1}" 
    l2[:0] = f"{num2}"
    n1 = {}
    n2= {}

    for i in l1:
        n1[i] = n1.get(i, 0) + 1
    
    l1[:0] = f"{num2}"
    for i in l2:
        n2[i] = n2.get(i, 0) + 1

    if n1 == n2:
        return True
    else: 
        return False

    