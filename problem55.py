

def reverseNum(num):
    return int(str(num)[::-1])

def addReverse(num):
    return num + reverseNum(num)

def isPalindrome(num):
    return num == reverseNum(num)

nums = [i for i in range(10001)]
lychrel_nums = []
for n in nums:
    s = n
    is_lychrel = True
    for i in range(50):
        s = addReverse(s)
        if isPalindrome(s):
            is_lychrel = False
            break
    if is_lychrel:
        lychrel_nums.append(n)

print(len(lychrel_nums), lychrel_nums)