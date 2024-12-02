class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(ch): 
            return ch in 'aeiou'

        
        current_vowels = sum(1 for i in range(k) if isVowel(s[i]))
        max_vowels = current_vowels

        
        for i in range(k, len(s)):
            if max_vowels == k:  
                return max_vowels
            
            if isVowel(s[i - k]):
                current_vowels -= 1
            
            if isVowel(s[i]):
                current_vowels += 1
            
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
    


def main():
    sol = Solution()
    result = sol.maxVowels("ramadan",2)
    print(result)


if __name__ == '__main__':
    main()
    