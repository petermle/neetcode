import data_structures.linked_list.ListNode;

public class add_two_numbers
{
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        // set up
        ListNode dummy = new ListNode(0);
        ListNode ptr = dummy;
        int l1_val = 0, l2_val = 0;

        int carry = 0;
        while (l1 != null || l2 != null || carry != 0)
        {
            // assignment
            l1_val = (l1 == null) ? 0 : l1.val;
            l2_val = (l2 == null) ? 0 : l2.val;

            // calculation
            int current_sum = l1_val + l2_val + carry;
            carry = current_sum / 10;

            // building result
            ptr.next = new ListNode(current_sum % 10);

            // moving pointers
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
            ptr = ptr.next;
        }

        return dummy.next;
    }
    
    public static void main(String[] args)
    {
        // setting up test case
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(6);

        // testing
        ListNode result = addTwoNumbers(l1, l2);
        result.printOnward();
    }
}