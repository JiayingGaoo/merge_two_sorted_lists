# merge two sorted list: solution with array

def merge_two_sorted_lists(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1

    l_merge = []
    for var in l1:
        l_merge.append(var)

    j = 0
    while 1:
        cur_l2_val = l2[j]
        print("cur_l2_val = ", cur_l2_val)
        print("cur_l_merge:", l_merge)

        # look the potential position of cur_l2_val in l_merge
        at_the_edge = False
        if cur_l2_val < l_merge[0]:
            l_merge.insert(0, cur_l2_val)
            at_the_edge = True
        elif cur_l2_val > l_merge[-1]:
            l_merge.append(cur_l2_val)
            at_the_edge = True

        if not at_the_edge:
            pre_l1_val = l_merge[0]
            i = 1
            while 1:
                cur_l1_val = l_merge[i]
                if cur_l2_val >= pre_l1_val and cur_l2_val <= cur_l1_val:
                    l_merge.insert(i, cur_l2_val)
                    break
                pre_l1_val = cur_l1_val
                i = i + 1

        j = j + 1
        if j == len(l2):
            break
    return l_merge


test_l1 = [1, 3, 5, 10]
test_l2 = [2, 3, 1000]
test_merge = merge_two_sorted_lists(test_l1, test_l2)
print(test_merge)



