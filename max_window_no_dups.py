def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int

    string s (could be empty)
    find longest substring without repeating characters
    substring: one char after another (consecutive)

    two pointers (sliding window)
    - valid window: every char is unique
    - want to expand window as much as possible (max)

    - set to store chars in current window
    - if we encounter a char already in our set, we have to move the start of the window forward until the window is valid again
        - as we move start forward, remove all chars along the way from the set

    Plan:
        - track curr size of window, max size, and set of seen chars
        - check if curr char already exists in set
            yes -> 
                remove char at start from set
                decr curr size
                move start ptr forward
        - add char to window, incr size
        - take the max of curr max and curr window size
                

    "abcdc"
        se

    set = (d, c) 
    max = 4
    curr = 2

    """
    start = 0
    seen = set()
    max_size = 0
    size = 0

    for c in s:
        while c in seen:
            seen.remove(s[start])
            size -= 1
            start += 1
        
        seen.add(c)
        size += 1
        max_size = max(size, max_size)

    return max_size