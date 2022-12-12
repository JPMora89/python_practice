def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> 

        >>> 
        10

        >>> sum_range(nums, 1)
        9

        >>> 
        6

        >>> 
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    if end == None:
        end = len(nums)
    return sum(nums[start:end + 1])
