# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print_list_node_object(self, l1: ListNode):
        print('[', end='')
        if l1 is None:
            print('')
        else:
            while 1:
                print(l1.val, end=' ')
                if l1.next is not None:
                    l1 = l1.next
                else:
                    print(']')
                    break

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        merge_head = l1
        # enum the elements in l2
        while 1:
            print('step:')
            cur_node_l2 = ListNode(x=l2.val)
            print('cur_node_l2_val: ', cur_node_l2.val)
            print('need to be merged into->:', end=' ')
            self.print_list_node_object(merge_head)

            # enum each elements in l_merge for its update
            # obtain the first and last value for the current merge
            at_the_edge = False
            if cur_node_l2.val <= merge_head.val:
                # print('insert to start')
                p = cur_node_l2
                p.next = merge_head
                self.print_list_node_object(merge_head)
                merge_head = p
                self.print_list_node_object(merge_head)
                at_the_edge = True

            if not at_the_edge:
                p = merge_head
                while 1:
                    if p.next is not None:
                        p = p.next
                    else:
                        break
                if cur_node_l2.val >= p.val:
                    p.next = cur_node_l2
                    at_the_edge = True

            if not at_the_edge:
                p = merge_head
                while 1:
                    cur_node = ListNode(x=p.val)
                    next_node = ListNode(x=p.next.val)
                    if cur_node_l2.val >= cur_node.val and cur_node_l2.val <= next_node.val:
                        # insert the new node cur_node_l2 between p and p.next
                        cur_node_l2.next = p.next
                        p.next = cur_node_l2
                        break
                    p = p.next

            # update l_merge
            print('merge_result:', end='')
            self.print_list_node_object(merge_head)
            l2 = l2.next
            if l2 is None:
                return merge_head

# definition of test_l1_chain_list
test_l1_node_a = ListNode(1)
test_l1_node_b = ListNode(2)
test_l1_node_c = ListNode(4)
test_l1_node_a.next = test_l1_node_b
test_l1_node_b.next = test_l1_node_c
test_l1_node_c.next = None

# definition of test_l2_chain_list
test_l2_node_a = ListNode(1)
test_l2_node_b = ListNode(3)
test_l2_node_c = ListNode(4)
test_l2_node_a.next = test_l2_node_b
test_l2_node_b.next = test_l2_node_c
test_l2_node_c.next = None

Sol = Solution()
# Sol.print_list_node_object(test_l1_node_a)
# Sol.print_list_node_object(test_l2_node_a)

test_merge = Sol.mergeTwoLists(test_l1_node_a, test_l2_node_a)