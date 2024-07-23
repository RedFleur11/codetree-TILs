def max_distance(N, seats):
    # 빈 자리들의 인덱스를 수집
    empty_indices = [i for i, seat in enumerate(seats) if seat == '0']
    if len(empty_indices) < 2:
        return 0  # 빈 자리들이 2개 미만이면 두 명을 배치할 수 없으므로 거리 0
    
    # 현재 차 있는 자리들의 인덱스 수집
    occupied_indices = [i for i, seat in enumerate(seats) if seat == '1']
    
    # 두 사람 간의 거리의 최댓값을 이분 탐색으로 찾기
    def can_place_people(min_distance):
        last_pos = -min_distance - 1  # 첫 번째 사람을 배치할 때의 위치를 -min_distance - 1로 초기화
        count = 0
        for index in empty_indices:
            if index - last_pos >= min_distance:
                count += 1
                last_pos = index
                if count == 2:
                    return True
        return False
    
    # 이분 탐색
    low, high = 0, N
    while low < high:
        mid = (low + high + 1) // 2
        if can_place_people(mid):
            low = mid
        else:
            high = mid - 1
    
    return low

# 입력 받기
N = int(input())
seats = input().strip()

# 결과 출력
print(max_distance(N, seats))