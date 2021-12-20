def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    r = 0
    x = range(r, len(nums))
    c = 0
    for i in x:
        if i == len(nums) - 3:
            break
        else:
            for j in x:
                if j == len(nums) - 1:
                    break
                else :
                    if nums[i] == nums[j+1] :
                        return nums[i]
            r += 1
            x = range(r, len(nums))