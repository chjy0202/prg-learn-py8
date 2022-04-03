# 소수인지 판별하는 함수
def is_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def solution(n, q):
    count = 0
    num_str = ''

    # q진수로 변환하는 방법
    while n > 0:
        n, mod = divmod(n, q)
        num_str += str(mod)

	  # str을 역으로 리턴하는 방법
    num_lst = num_str[::-1].split('0')

    num_lst = [v for v in num_lst if v]
    for n in num_lst:
        if n != '1' and is_prime(int(n)):
            count += 1
    print(num_lst, count)
    return count
    
