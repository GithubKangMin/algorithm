# 바구니 회전시키기 -> 특정 범위를 집어서 기준 앞에걸 뒤로 보냄 범위 외는 그대로 둠.
# 문제풀이 - 일단 N,M 받아서 넣고 리스트에 집어넣은 뒤 슬라이싱 해서 뒤로 보내고 반복문으로 출력하기
# 틀림 -> 인덱스 세밀하게 조절해야 함. 인덱스

# N,M = map(int,input().split())
#
# l = list(range(1,N+1))
#
# for _ in range(M):
#     i,j,k= map(int,input().split())
#     l[i:k] , l[k+1:j+1] = l[k+1:j+1] , l[i:k]
#
# print(l)


N, M = map(int, input().split())

l = list(range(1, N+1))

for _ in range(M):
    i, j, k = map(int, input().split())
    # 리스트 구간 교환 (인덱스 보정 필요)
    l[i-1:j] = l[k-1:j] + l[i-1:k-1]

print(*l)

# N, M = map(int, input().split())
# l = list(range(1, N+1))
#
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     # 구간을 복사하여 처리
#     first_part = l[i-1:k]  # 첫 번째 구간
#     second_part = l[k:j]   # 두 번째 구간
#
#     # 리스트에서 두 구간을 교환
#     l[i-1:i-1+len(second_part)] = second_part
#     l[i-1+len(second_part):j] = first_part
#
# print(*l)