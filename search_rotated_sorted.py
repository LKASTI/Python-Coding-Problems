def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int

    list of distinct ints sorted in ascending rotated at point k, where k is the max and k+1 is min
    int target in the list

    want to find and return idx of target

    - is target guaranteed in list?
        -1 if not in list
    - could list be empty?
    - unique ints
    - sorted in ascending
    - not guaranteed to be rotated
    - must be O(log n)

    - binary search 
        - only works when list is sorted, we will be searching through unsorted and sorted portions
        - have to guarantee that the values we're searching through is sorted
            - compare mid point value to end point value: [mid] < [val] if sorted
        - if the right side is sorted then we can compare the mid and target, other wise the left side must be sorted
            - if the target is not in the sorted parts then it must be in the unsorted portion

    Plan
        - start, end to get the mid pt
        - compare mid and end to find if the right/left side is sorted:
            if right is sorted, compare mid and target and target to end to find which side will contain the target
            otherwise it must be in left side, unsorted portion

        - special cases:
            - how do we know target is not in the list
                - when we broke out of the loop

        ex: [1 2 3 4 |0|] target = 5



    """
    start, end = 0, len(nums)-1

    while start <= end:
        mid = (start + end)//2

        if nums[mid] == target:
            return mid
        # is the rightside sorted?
        elif nums[mid] <= nums[end]:
            # is target in mid...end
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        # left side is sorted
        else:
            # is target in start...mid
            if target < nums[mid] and target >= nums[start]:
                end = mid - 1
            else:
                start = mid + 1

    return -1