# cnt = 0
#
# a=s= input()
#
# #언제는 세개 체크하고 언제는 두개 체크해야되고 언제는 하나 체크해야됨 -> 하나씩 보는 방법으로는 해결이 안됨
#
# if 'dz=' in s:
#     cnt += s.count('dz=')
#     a=s.replace('dz=','')
# if 'z=' in s:
#     cnt += s.count('z=')
#     a=s.replace('z=','')
#     print(cnt)
# if 'c=' in s:
#     cnt += s.count('c=')
#     a=s.replace('c=','')
# if 'c-' in s:
#     cnt += s.count('c-')
#     a=s.replace('c-','')
# if 'd-' in s:
#     cnt += s.count('d-')
#     a=s.replace('d-','')
# if 'lj' in s:
#     cnt += s.count('lj')
#     a=s.replace('lj','')
# if 'nj' in s:
#     cnt += s.count('nj')
#     a=s.replace('nj','')
# if 's=' in s:
#     cnt += s.count('s=')
#     a=s.replace('s=','')
#
# for i in a:
#     cnt += 1
# print(cnt)

##정답
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i,'*')
print(len(word))

##문자열을 변경해주면서 남은 문자열끼리 모였을 때 크로아디아 알파벳이 되어버리네 => a랑 s를 같이 하면서 계산

##중복된 경우 하나만 올라가네 -> 개수 세어서 그만큼 cnt 올려줘야 될 듯?

#'dz=' 이랑 'z=' 겹쳐서 문제가 생겼네 dz= 을 세고 없애도 if 로 묶이면 중복으로 세게 됨  elif 로 묶이면 안세긴 하는데 dz= 과 z=이 같이 있는 케이스에서 아무것도 못함


# if문으로 노가다했는데 결국 못풀었다 그냥 생각나는대로 풀었는데 그대로 풀면 생각지도 못한 에러가 많이 난다. 남은거 끼리 다시 문자로 엮이고 겹치는걸 중복해서 세었다

## -> 문자열을 다루는 문제인 경우 적극적으로 문자열 관련된 함수를 이용할 수 있어야 한다.

