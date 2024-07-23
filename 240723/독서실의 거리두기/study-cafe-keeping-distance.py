def max_distance(N, seats):
    empty_indices = [i for i, seat in enumerate(seats) if seat == '0']
    
    def can_place_with_distance(d):
        count = 0
        last_position = -d - 1
        for index in empty_indices:
            if index - last_position >= d:
                count += 1
                last_position = index
                if count == 2:
                    return True
        return False
    
    low, high = 1, N
    while low < high:
        mid = (low + high + 1) // 2
        if can_place_with_distance(mid):
            low = mid
        else:
            high = mid - 1
    
    return low

# 입력 받기
N = int(input())
seats = input().strip()

# 결과 출력
print(max_distance(N, seats))