import math

def time_record(t1, t2):
    h1, m1 = t1.split(':')
    h2, m2 = t2.split(':')
    
    return (int(h2) * 60 + int(m2)) - (int(h1) * 60 + int(m1))
    
def solution(fees, records):
    answer = []
    cars = {}
    times = {}

    for record in records:
        time, car, state = record.split(' ')
        if state == 'IN':
            cars[car] = time
        else:
            if car in times:
                times[car] += time_record(cars[car], time)
            else:
                times[car] = time_record(cars[car], time)
            del cars[car]
            
    if cars:
        for car, time in cars.items():
            if car in times:
                times[car] += time_record(cars[car], '23:59')
            else:
                times[car] = time_record(cars[car], '23:59')
    
    # 키 값으로 정렬하되 튜플 형태로 반환해준다
    times = sorted(times.items())
    for t in times:
        print(t[1])
        if t[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((t[1] - fees[0]) / fees[2]) * fees[3])  
            
    return answer