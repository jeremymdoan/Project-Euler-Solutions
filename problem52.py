# https://projecteuler.net/problem=52

num = 100000
while num < 200000:
    num_multiples = []
    num_array = sorted(str(num))
    num_array_len = len(num_array)
    for i in range(6, 1, -1):
        num2 = num*i
        num_multipe_array = sorted(str(num2))
        num_multipe_array_len = len(num_multipe_array)
        if num_multipe_array_len > num_array_len:
            num = 10**(num_array_len)
            break
        if num_array == num_multipe_array:
            num_multiples.append(num2)
    if len(num_multiples) == 5:
        break
    else:
        num+=1
print(num,num_multiples)