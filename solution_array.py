# merge two sorted list: solution with array

def merge_two_sorted_lists(l1, l2):
    l_merge = []
    for var in l1:
        l_merge.append(var)

    for j, cur_l2_val in enumerate(l2):
        for i, cur_l1_val in enumerate(l1):
            print(i, j)
            if i == 0:
                pre_l1_val = cur_l1_val
                if cur_l2_val <= cur_l1_val:
                    l_merge.insert(0, cur_l2_val)
            if i > 0:
                if cur_l2_val > pre_l1_val and cur_l2_val < cur_l1_val:
                    l_merge.insert(i, cur_l2_val)
                if cur_l2_val > cur_l1_val:
                    l_merge.append(cur_l2_val)
    return l_merge

test_l1 = [1, 2, 10, 56, 73, 100]
test_l2 = [2, 8, 89, 101, 400]
test_merge = merge_two_sorted_lists(test_l1, test_l2)
print(test_merge)



