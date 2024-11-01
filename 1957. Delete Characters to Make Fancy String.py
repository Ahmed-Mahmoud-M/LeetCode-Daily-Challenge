
"""  
Algorithm:

1. Build the result string character by character.
2.For each character, check if adding it would create three consecutive identical characters in result.
3.If adding the character is allowed, append it to result; otherwise, skip to the next character.

"""



class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        
        for i in range(len(s)):
            x = s[i]
            if self.feasible(result, x):
                result += x
        
        return result

    def feasible(self, result, x):
        
        if len(result) >= 2 and result[-1] == x and result[-2] == x:
            return False
        return True

        
    





# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.makeFancyString("leeetcode"))