def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word = ""
    answer = ""
    x = range(0, len(phrase))
    for i in x :
        word = word + phrase[i]
        if phrase[i] == " ":
            word = word.lower()
            word = word.capitalize()
            answer = f"{answer}{word}"
            word = ""
        if i == x[-1]:
            word = word.lower()
            word = word.capitalize()
            answer = f"{answer}{word}"
    return answer