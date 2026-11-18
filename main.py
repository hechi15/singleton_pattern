from singleton import Singleton

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print("=== 1. 동일 인스턴스 비교 ===")
print("s1 is s2 :", s1 is s2)
print("id(s1)   :", id(s1))
print("id(s2)   :", id(s2))

print()
print("=== 2. 상태 공유 확인 ===")
print("처음 s1.counter :", s1.counter)
s1.counter += 1
s1.counter += 1
print("s1으로 2번 증가 후 s1.counter :", s1.counter)
print("s2로 읽은 s2.counter          :", s2.counter)