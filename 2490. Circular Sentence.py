

""" 
    the algorithm : follows the hints

   1. Check the character before the empty space and the character after the empty space.
   2. Check the first character and the last character of the sentence.


"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            #print("entered")
            return False
        
        for i in range(len(sentence)):
            if sentence[i] == " ":
              #  print("there is a space ")
                if sentence[i-1] != sentence[i+1]:
                    
                    return False
            
        


        return True
    



# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.isCircularSentence("eetcode"))
    

    
