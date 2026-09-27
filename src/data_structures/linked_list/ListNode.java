package data_structures.linked_list;

public class ListNode {
    public int val;
    public ListNode next;
    ListNode() {}
    public ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    public void printOnward()
    {
        if (this.next == null) System.out.println(this.val);
        else
        {
            System.out.print(this.val + "->");
            this.next.printOnward();
        }
    }
}
