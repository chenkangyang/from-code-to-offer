memo = dict()
def dp(K, N): # 现有鸡蛋，当前楼层：至少扔多少次才能确定导致碎的楼层
    if K == 1: return N
    if N == 0: return 0
    if (K, N) in memo:
        return memo[(K, N)]

    res = float('INF')
    # for i in range():
    #     res = min(res,
    #     max(
    #         dp(K-1,i-1), # 鸡蛋碎了
    #         dp(K, N-i)
    #         )+1
    #     )    

    # 以上py代码超时，用二分搜索解决min(max)形式的解的搜索
    # K 固定时，dp(K, N) 单调增，所以
    # 随着i的增大，dp(K-1,i-1) 越来越大
    # 随着i的增大，dp(K,N-i) 越来越小
    # max(dp(K-1,i-1),dp(K, N-i))是个山谷，min就是求谷底

    lo, hi = 1, N
    while lo <= hi:
        mid = (lo + hi) // 2
        broken = dp(K-1, mid-1)
        unbroken = dp(K, N-mid)
        # res = min(max(碎，没碎) + 1)
        
        if broken > unbroken:
            hi = mid - 1
            res = min(res, broken+1)
        else:
            lo = mid + 1
            res = min(res, unbroken+1)


    memo[(K, N)] = res 
    return res


print(dp(2,6))