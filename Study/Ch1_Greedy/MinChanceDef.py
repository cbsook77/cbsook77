# 좀더 자세하게 풀기
#최소 횟수 찾기
"""
어떠한 수 N이 1이 될때까지 다음의 두 과정중 하나를 반복적으로 선택하여 수행
1. N에서 1을 뺀다
2. N을 K로 나눈다.

ex) 25, 5
2번과정 25/5=5
2번과정 5/5=1

2번과정 2번으로 1이 되므로 출력값 2

"""
# N,K를 공백으로 구분하여 입력 받기
n, k = map(int ,input().split())
result=0

while True:
    # (N==K 로 나누어 떨어지는 수) 가 될때까지 1씩 빼기
    target=(n//k)*k
    result += (n-target)
    n=target
    # N이 K보다 작을 떄(더이상 나눌수 없을 때) 반복문 탈출
    if n<k:
        break
    #K로 나누기
    result +=1
    n//=k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)