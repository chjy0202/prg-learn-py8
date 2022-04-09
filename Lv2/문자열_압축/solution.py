def solution(data):
    result = len(data)

    for step in range(1, len(data) // 2 + 1):
        compressed = ''
        prev = data[:step]
        count = 1

        for i in range(step, len(data), step):
            if prev == data[i:step + i]:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = data[i:step + i]
                count = 1
        compressed += str(count) + prev if count > 1 else prev
    
        result = min(result, len(compressed))
    
    return result