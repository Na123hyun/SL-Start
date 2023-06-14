'''
2023-06-14
김나현
#문제 정의
    리스트를 만들고 반복문을 출력한다.
'''
import random #import 랜덤 모듈 선언

num1 = list(range(1,10)) #리스트 반복문
print("num1 : ",num1) #결과 출력

for i in num1 : #반복문
    print(i, end=', ') #결과 출력

print() #줄 바꿈

'''
1~100 사이의 정수 중 랜덤으로 10개의 수를 뽑아서 리스트에 저장
'''

num2 = [] #빈 리스트 생성
for i in range(10) : #반복문
    num2.append(random.randint(1, 100)) #랜덤 수 #append() 추가하기
print("생성된 리스트 : ",num2) #결과 출력