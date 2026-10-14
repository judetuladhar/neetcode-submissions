class ListNode {
    public:
        int val;
        ListNode* next;

        ListNode(int val) :
        val(val), next(nullptr){}

        ListNode(int val, ListNode* next) :
        val(val), next(nullptr){}
};

class LinkedList {
    private:
        ListNode* head;
        ListNode* tail;

    public:
        LinkedList() {
            head = new ListNode(-1);
            tail = head;
        }

        int get(int index) {
            ListNode* n = head->next;
            for (int i = 0; i < index; i++){
                if (n == nullptr) return -1;
                n = n->next;
            }
            if (n == nullptr) return -1;
            return n->val;
        }

        void insertHead(int val) {
            ListNode* n = new ListNode(val);
            n->next = head->next;
            head->next = n;
            if (n->next == nullptr){
                tail = n;
            }
        }
        
        void insertTail(int val) {
            tail->next = new ListNode(val);
            tail = tail->next;
        }

        bool remove(int index) {
            ListNode* n = head->next;
            ListNode* prev = head;
            for (int i = 0; i < index; i++){
                if (n == nullptr){
                    return false;
                }
                prev = n;
                n = n->next;
            }
            if (n == nullptr){
                return false;
            }
            if (n == tail){
                tail = prev;
                prev->next = nullptr;
                delete n;
                return true;
            }
            prev->next = n->next;
            delete n;
            return true;
        }

        vector<int> getValues() {
            vector<int> res;
            ListNode* curr = head->next;
            while (curr != nullptr){
                res.push_back(curr->val);
                curr = curr->next;
            }
            return res;
        }
};
