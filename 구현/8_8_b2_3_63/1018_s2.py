# ## 무슨 기준으로 8*8 판을 선택을 하지?
# ## 8*8 판을 선택한 후 어떻게 개수를 체크하지? 일단 8*8 판에서 칠해야 할 정사각형 개수 판단하는 코드  --> 문자열은 불변객체라 바꿀 수 없다..
# N,M = map(int,input().split())
# result = 0
# ## 2차원배열로 받음
# arr = [[0 for col in range(N)] for row in range(M)]
# ## 반복
# for i in range(N-8) :
#     for j in range(M-8) :
#         # i , j 를 시작점으로 하는 8 x 8 보드판 가져옴
#
#
#
#
#
# # 8 x 8 보드판에서 몇개 바꿔야하는 지 계산 코드 -> 함수로 구현 ==> 잘못구현했네 아예 갈아엎어야 할듯.
# # 내가 짠 코드는 그냥 문자열을 리스트로 바꿔서 이전 값과 다르다면 바꿔주는 코드. 문제에서 요구한건 위 아래도 맞물려야 함 수정해서 개선이 되려나 ?
# def board():
#     global result
#     global postFirst
#     for _ in range(8):
#         wb = list(input())
#         a = -1
#         for i in wb:
#             ## 한줄에서 연속해서 같은게 나오면 연속 제거해주는 코드
#             if i == wb[a]:
#                 if i == 'B':
#                     wb[a + 1] = 'W'
#                 else:
#                     i = 'B'
#                 a += 1
#                 result += 1
#             ## 연속해서 같은게 나오지 않는 코드
#             else:
#                 a += 1
#                 continue
#         print(wb)
#
# print(result)