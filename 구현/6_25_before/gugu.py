# 1. 구구단
# def gugu(num):
#     for i in range(1,10):
#         list.append(num*i)
#     return list
#
# list=[]
#
# print(gugu(2))
#2. 3과 5의 배수 합하기
# number = int(input())
# list = []
# sum=0
# for i in range(number):
#     if i % 3 == 0:
#         list.append(i)
#     elif i % 5 ==0:
#         list.append(i)
#     # if i% 3 ==0 or i % 5 ==0: 이렇게 개선하는게 더 깔끔함
#       result += i
#
# for i in list:
#     sum += i
#
# print(sum)

#3. 게시판 페이징 하기
# m,n = map(int,input().split())
# def GetTotalPage():
#     if m%n == 0:
#         page= int(m/n)
#     else:
#         page= int(m/n)+1
#     return page
# print(GetTotalPage())

#4. 간단한 메모장 만들기
# import sys
#
# option = sys.argv[1]
# memo = sys.argv[2]

## 11주차
## 실습1
numbers = list(map(int, input().split()))
sum=0

for i in numbers:
    sum += i
print(sum/len(numbers))
print(max(numbers))
print(min(numbers))

## 실습2
