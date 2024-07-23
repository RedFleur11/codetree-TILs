def max_min_distance_after_placement(n, seats):
    current_positions = [i for i, seat in enumerate(seats) if seat == '1']
    
    if len(current_positions) == 0:
        return (n - 1) // 2
    
    # 모든 빈 자리(0)를 포함하는 연속된 구간을 찾기
    max_distance = 0
    max_distances = []
    prev_position = -1
    
    for i in range(n):
        if seats[i] == '1':
            if prev_position == -1:
                max_distances.append(i)
            else:
                max_distances.append((i - prev_position) // 2)
            prev_position = i

    max_distances.append(n - 1 - current_positions[-1])
    
    max_distances.sort()
    
    # 가장 큰 두 개의 간격에서 두 명을 배치하는 경우가 최적
    if len(max_distances) == 1:
        return max_distances[0]
    else:
        return max(max_distances[-1], max_distances[-2])

# 입력 처리
n = int(input())
seats = input().strip()

# 결과 출력
print(max_min_distance_after_placement(n, seats))