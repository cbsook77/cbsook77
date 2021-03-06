#2중 반복문 구조를 이용한 숫자카드게임
#여러개 의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
#단 게임의 룰이 있음

#1. 숫자가 쓰인 카드들이 NXM 형태로 놓여있다. 이떄 N은 행의 갯수를 의미하며, M은 열의 갯수를 의미한다.
#2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
#3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야한다.
#4. 따라서 처음에 카드를 골라낼 행을 선택할 때 , 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
#   최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

"""
ex) 33
3 1 2
4 1 4
2 2 2
출력 : 2
"""

#N, M을 공백으로 구분하여 입력받기
n,m= map(int,input().split())

result=0
#한 줄 씩 입력받아 확인
for i in range(n):
    data= list(map(int, input().split()))
    #현재 줄에서 '가장 작은 수 찾기'
    min_value= 10001
    for a in data:
        min_value=min(min_value,a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result=max(result,min_value)

print(result) #최종답안 출력
