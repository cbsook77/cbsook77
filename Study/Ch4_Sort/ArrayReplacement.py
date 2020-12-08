'''
두 배열의 원소 교체

두개의 배열 A와 B가 있는데 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
최대 K번의 바꿔치기 연산을 수행할 수 있는데 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는
원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다. 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록
하는 것이다.

N,K, 그리고 배열 A와 B의 정보가 주어졌을때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A
의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오

예를 들어 N=5, K=3이고 배열 A,B가 이와같다.
A=[1,2,5,4,3]
B=[5,5,6,6,5]

이 경우 다음과 같이 세번의 연산을 수행할 수 있다.
연산 1) 배열 A의 원소 '1'과 배열 B의 원소 '6'을 바꾸기
연산 2) 배열 A의 원소 '2'와 배열 B의 원소 '6'을 바꾸기
연산 3) 배열 A의 원소 '3'과 배열 B의 원소 '5'를 바꾸기

연산이후의 배열상태는 이렇다.

배열 A=[6,6,5,4,5]
배열 B=[3,5,1,2,5]

따라서 A의 원소 합인 26이 정답

입력 조건
첫 번재 줄에 N,K가 공백으로 구분되어 입력된다.(1<=N<=100000,0<=K<=N)
두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수입니다.

출력 조건
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.

입력예시
5 3
1 2 5 4 3
5 5 6 6 5

출력예시
26
'''

n,k = map(int, input().split()) #N과 K를 입력받기
a=list(map(int,input().split())) #배열 A의 모든 원소를 입력받기
b=list(map(int, input().split()))#배열 B의 모든 원소를 입력받기

a.sort() #배열 A는 오름차순 정렬 수행
b.sort(reverse=True)#배열 B는 내림차순 정렬 수행

# 첫뻔째 인덱스 부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #A의 원소가 B의 원소보다 자근 경우
    if a[i]<b[i]:
        #두 원소를 교체
        a[i],b[i]=b[i],a[i]
    else: #A의 원소가 B의 원소보다 크거나 같을때, 반복문을 탈출
        break

print(sum(a)) #배열 A의 모든 원소의 합을 출력