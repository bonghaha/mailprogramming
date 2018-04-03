def recurse(ans, cur, open, close, n):
    if len(cur) == n * 2:
        ans.append(cur)
        return
    if open < n:
        recurse(ans, cur + "(", open + 1, close, n)
    if close < open:
        recurse(ans, cur + ")", open, close + 1, n)


def parenthesisPairs(n):
    ans = []
    recurse(ans, "", 0, 0, n)
    return ans


print(parenthesisPairs(3))
