a, b = 1, 1
y = a + b
n = int(input())  # n번째 피보나치 수를 구하려면

for k in range(3, n + 1):
    c = a + b  # 현재 두 수의 합을 구함
    y = c  # 새로운 피보나치 수를 y에 할당
    a = b  # a는 b로 갱신
    b = c  # b는 c로 갱신

print(y)  # 마지막 계산된 피보나치 수 출력
