def max_min_distance_after_placement(n, seats):
    # 현재 사람들의 위치 파악
    current_positions = [i for i, seat in enumerate(seats) if seat == '1']
    
    # 비어있는 자리 파악
    empty_positions = [i for i, seat in enumerate(seats) if seat == '0']
    
    max_min_distance = 0
    
    # 모든 빈 자리 중 두 자리를 선택하는 조합
    for i in range(len(empty_positions)):
        for j in range(i + 1, len(empty_positions)):
            new_positions = current_positions + [empty_positions[i], empty_positions[j]]
            new_positions.sort()
            
            # 가장 가까운 두 사람 간의 거리 계산
            min_distance = float('inf')
            for k in range(1, len(new_positions)):
                distance = new_positions[k] - new_positions[k - 1]
                min_distance = min(min_distance, distance)
            
            # 가능한 가장 가까운 두 사람 간의 거리의 최대값 갱신
            max_min_distance = max(max_min_distance, min_distance)
    
    return max_min_distance

# 입력 처리
n = int(input())
seats = input().strip()

# 결과 출력
print(max_min_distance_after_placement(n, seats))