def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if not isinstance(num, int) or num < 0:
        return None
    elif num == 0:
        return ""    
    else:
        answer = ""
        x = range(0, num)
        for i in x :
            answer = answer + phrase
        return answer    
