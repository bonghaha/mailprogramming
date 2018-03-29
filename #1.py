def solution(arr):
    maxSum = arr[0]
    currentSum = arr[0]
    for i in range(1, len(arr)):
        # print("arr[i] : %s" % i)  # 1, 2, 3, 4
        currentSum = max(currentSum + arr[i], arr[i])
        # print("currentSum : %s" % currentSum)
        maxSum = max(currentSum, maxSum)
        # print("maxSum : %s" % maxSum)
    return maxSum


list = [-5, -3, -1]
print(solution(list))
