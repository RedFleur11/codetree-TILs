def max_min_distance(seats):
    n = len(seats)
    
    # 1. 현재 채워진 자리들('1'의 위치)를 저장
    filled_positions = [i for i in range(n) if seats[i] == '1']
    
    # 2. 모든 가능한 빈 자리들 중에서 두 자리를 선택하여 채워보는 방법
    max_distance = 0
    
    for i in range(n):
        if seats[i] == '0':
            for j in range(i+1, n):
                if seats[j] == '0':
                    # 3. 두 자리 i와 j를 채운 후, 가장 가까운 두 사람 간의 거리를 계산
                    test_seats = seats[:i] + '1' + seats[i+1:j] + '1' + seats[j+1:]
                    max_distance = max(max_distance, calculate_min_distance(test_seats))
    
    return max_distance

def calculate_min_distance(seats):
    n = len(seats)
    prev_person = -1
    min_distance = float('inf')
    
    for i in range(n):
        if seats[i] == '1':
            if prev_person != -1:
                min_distance = min(min_distance, i - prev_person)
            prev_person = i
    
    return min_distance

# 입력 받기
N = int(input().strip())
seats = input().strip()

# 결과 출력
print(max_min_distance(seats))