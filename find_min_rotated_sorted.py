def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int

    list of sorted ints in ascending and rotated
    want O(log n ) time alg so find min

    - binary search
        - if the right side is sorted then it won't have the min
        - if the right side not sorted then it has the pivot point, which contains min and max adhacent to each other
        and 

    ex:
        [|0 1| 2 3 4]
            mid = 2
            compare mid with end: mid is < end therefore sorted portion
            could be the min but we need to check the left of it to find something smaller
            mid = 1
            compare: mid is < end therefore sorted portion
            check left
            mid = 0
            compare: sorted
            check left
            mid = 0: pointers are same


        [2 3 4| 0 1|]
            mid = 4
            not sorted
            search rightside
            mid = 0
            rightside is sorted
            check left
            mid = 0: pointers are equal


        [5 0 1 2 3 4]

    - how do we know we've hit the min?
        - left most value in sorted portion
    - compare mid with end
        - mid always <= end in sorted portion

    """

    start, end = 0, len(nums)-1

    while start < end:
        mid = (start + end)//2

        # compare mid and end values
        if nums[mid] <= nums[end]:
            # sorted portion, search left including mid
            end = mid
        else:
            # non-sorted potion contains pivot, search right not including mid
            start = mid + 1

    return nums[start]