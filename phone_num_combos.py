def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        string, digits 2-9 

        s = "435"

            [ghi] [def] [jkl]

            gdj, gdk, gdl

        s = "323"

            [def] [abc] [def]

        O(4^n * n)
        max of 4 choices (in worst case where every number in digits is 9 or 7)
        n digits in digits
        n time to construct the string
        
        """
        if not digits:
            return []

        digit_to_letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def dfs(path, idx):
            if idx == len(digits):
                res.append("".join(path))
                return

            for letter in digit_to_letter[digits[idx]]:
                dfs(path + [letter], idx + 1)

        dfs([], 0)

        return res