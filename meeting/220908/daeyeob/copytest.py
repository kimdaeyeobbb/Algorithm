a = [[1,2],[3,4,5]]
b = a[:]   # 얖은 복사 수행
print("*** 얕은 복사 테스트 ***")
print("a와 b는 같은가? ", a is b)   # 동일 대상인지 묻는 것
print("a와 b는 같은가? ", a == b)   # 복사하여 같은 값을 가지는 것
print("a[0]와 b[0]는 같은가?", a[0] is b[0])   # 리스트 내 요소들은 동일

print()
a.pop()
print("*** a의 구조 변경 ***")
print("a와 b는 같은가? ",a is b)
print("a와 b는 같은가? ",a == b)

print()
print("*** 깊은 복사 테스트 ***")
import copy
c = copy.deepcopy(a)
