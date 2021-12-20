def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel = 'aeiou'
    answer = {}
    phrase = phrase.lower()
    x = range(0, len(phrase))
    for i in x:
        if phrase[i] in vowel:
            answer[phrase[i]] = answer.get(phrase[i], 0) + 1
    return answer