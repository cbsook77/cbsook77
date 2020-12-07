# 거스름돈 문제

n=1260 #1260원
count =0 #동전의 갯수

# 큰 단위의 화폐부터 차례대로 확인
coin_types={500,100,50,10} #동전의 종류

for coin in coin_types:
    count +=n //coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 // 연산자 : 소숫점 이하를 버림
    n%= coin

print(count) # 동전의 갯수 출력 ex)1260원 결과값 : 14