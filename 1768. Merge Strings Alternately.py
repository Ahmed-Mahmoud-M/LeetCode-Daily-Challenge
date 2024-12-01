class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        p1,p2 = 0,0

        for _ in range(max(len(word1),len(word2))):
            
            
          
            
           

                if p1 < len(word1):
                    result.append(word1[p1])
                    p1 = p1 + 1
                
                if p2 < len(word2):
                    result.append(word2[p2])
                    p2 = p2 + 1

        
        return "".join(result)



def main():
    sol = Solution()
    result = sol.mergeAlternately("abc","pqr")
    print(result)


if __name__ == '__main__':
    main()
    
