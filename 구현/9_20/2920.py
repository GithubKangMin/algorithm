notes = ['0','C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

vals =list(map(int,input().split()))

if vals == sorted(vals) :
    print("ascending")
elif vals == sorted(vals, reverse=True) :
    print("descending")
else:
    print("mixed")
## 리스트 자체를 수정하지 말고 새로운 리스트를 반환하는 메서드를 써야 한다.