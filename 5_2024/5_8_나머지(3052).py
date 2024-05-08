#집합을 활용하는 문제
rest = set()

for i in range(10):
    number = int(input())
    rest.add(number % 42)
print(len(rest))

#집합을 활용해서 푼 것은 처음인데 쉬운 문제 만나서 잘 됐다.
#add()
#메서드와 함수의 차이
#     메서드는 다른 클래스에 있는 함수를 호출해 특정 객체에 대해 쓰이는 것이지만 함수는 해당 클래스에서 그냥 쓰는 것임. 그래서 사용방법이 다르다. 메서드는 .으로 접근해야 함
#   집합에서는 append가 아니라 add를 써야하고