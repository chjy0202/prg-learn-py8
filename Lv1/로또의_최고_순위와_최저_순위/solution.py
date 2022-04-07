def solution(lottos, win_nums):
    award = [6,6,5,4,3,2,1]
    
    count_0 = lottos.count(0)
    count = 0
    for num in lottos:
        if num in win_nums:
            count += 1
            
    return [award[count+count_0], award[count]]