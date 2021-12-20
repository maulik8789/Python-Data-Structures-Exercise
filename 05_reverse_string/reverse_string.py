def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse = ""
    x = range(len(phrase) -1, -1, -1)
    for i in x:
        reverse = reverse + phrase[i]
    return reverse
