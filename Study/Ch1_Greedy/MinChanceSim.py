#단순하게 풀기
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
n, k = map(int ,input().split())
result=0

#N이 K이상이라면 K로 계속 나누기
while n>=k:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while  n%k !=0:
        n-=1
        result +=1
    # K로 나누기
    n//=k
    result +=1

#마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -= 1
    result +=1

print(result)

