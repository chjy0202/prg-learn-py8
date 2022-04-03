# 소수인지 판별하는 함수
def is_prime(n):
    if n == 1:
        return False
    # 짝지어 제외시킬 수 있기 때문에 제곱근 까지만 판별하는 것이 이득!
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# q 진수로 변환하는 함수
def trans(n, q):
    num = ''
    while n > 0:
        n, mod = divmod(n, q)
        num += str(mod)
    # str을 역으로 리턴하는 방법
    return num[::-1]
    
def solution(n, q):
    count = 0
    num_lst = trans(n, q).split('0')

    for n in num_lst:
        if n != '' and is_prime(int(n)):
            count += 1
    return count