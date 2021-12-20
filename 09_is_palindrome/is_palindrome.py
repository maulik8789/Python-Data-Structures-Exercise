def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    
    reverse = ""
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    x = range(len(phrase) -1, -1, -1 )
    
    for i in x:
        reverse = reverse + phrase[i] 
    if reverse == phrase:
        return True
    else:
        return False 
