class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp_list = s.copy()

        for i in range(1,len(s)+1):
            s[i-1] = temp_list[-i]
