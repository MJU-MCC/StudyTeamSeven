#좌표압축.py

N = int(input())  # 좌표 개수
coordinates = list(map(int, input().split()))  # 좌표 리스트

# 좌표 압축을 위한 정렬과 딕셔너리 사용
sorted_coordinates = sorted(list(set(coordinates)))
coordinate_dict = {sorted_coordinates[i]: i for i in range(len(sorted_coordinates))}

# 결과 출력
result = [coordinate_dict[coordinate] for coordinate in coordinates]
print(*result)