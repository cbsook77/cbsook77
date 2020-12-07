# 좀더 자세하게 풀기
# 큰수의 법칙 : 다양한 수로 이루어진 배열이 있을때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징

# ex)2,4,5,4,6 M=8 K=3 6+6+6+5+6+6+6+5=46

# N, M , K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 1]  # 두번째로 큰수

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result=0
result += (count)*first #가장 큰 수 더하기
result += (m-count)*second #두번째로 큰 수 더하기

print(result)#최종 답안 출력