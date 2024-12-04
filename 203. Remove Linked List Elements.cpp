#include <iostream>


  struct ListNode {
       int val;
       ListNode *next;
       ListNode() : val(0), next(nullptr) {}
       ListNode(int x) : val(x), next(nullptr) {}
       ListNode(int x, ListNode *next) : val(x), next(next) {}
   };
 
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        // Create a dummy node to simplify handling the head
        ListNode* dummy = new ListNode(0, head);
        ListNode* current = dummy;

        while (current->next != nullptr) {
            if (current->next->val == val) {
                current->next = current->next->next; // Skip the node
            } else {
                current = current->next; // Move to the next node
            }
        }

        return dummy->next;
    }
};



int main(int argc, char const *argv[])
{
    // Solution sol; 
    return 0;
}
