#include <iostream>
#include <string>


class Solution {
public:
    std::string compressedString(std::string word) {
        std::string comp  = "";


        while(word.size() > 0) {
            char firstchar = word[0];
           // std::cout << firstchar <<std::endl;
                int count  = 0;
            for(char c : word){
                if (count == 9) {
                    break;
                }else if (firstchar == c) {
                    count++;
                }else {
                    break;
                }

            }
        comp.append(std::to_string(count)+""+firstchar);
        word.erase(0,count);
        }

        return comp;
    }


};



int main(int argc, char const *argv[])
{
    Solution sol;
   std::string result = sol.compressedString("aaaaaaaaaaaaaabb");
   std::cout << result << std::endl;

    return 0;
}
