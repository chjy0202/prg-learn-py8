def rotate(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result

def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len,lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True
    
def solution(key,lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0 for _ in range(n * 3)] for _ in range(n *3)]
    # new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    print(new_lock)
    
    for rotation in range(4):
        key = rotate(key)
        for x in range(n - m + 1, n * 2):
            for y in range(n - m + 1, n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False