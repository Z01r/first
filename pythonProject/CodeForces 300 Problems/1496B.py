import math
 
T = int(input())
 
for tc in range(T):
    N, K = [int(k) for k in input().split()]
 
    arr = sorted([int(k) for k in input().split()])
 
    arr_set = set(arr)
 
    cur_cnt = len(arr)
 
    def get_mex(arr):
        for i, n in enumerate(arr):
            if i == n:
                continue
            else:
                return i
        return max(arr) + 1
    
    max_value = max(arr)
    mex_value = get_mex(arr)
 
    # print("max = ", max_value, " mex = ", mex_value, " cur cnt = ", cur_cnt)
    if mex_value > max_value:
        cur_cnt += K
    else:
        if K > 0:
            # when max > mex
            to_add = math.ceil((mex_value + max_value) / 2.0)
            if to_add not in arr_set:
                cur_cnt += 1
 
    print(cur_cnt)
            
