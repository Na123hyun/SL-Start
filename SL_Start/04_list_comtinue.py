'''
2023-06-14
컴퓨터공학부 202395004 김나현
#문제 정의
    continue #계속되다 / 반복의 처음으로 돌아간다.
'''

#리스트의 값 10개 중에서 10보다 큰 수를 출력하시오.

numbers =[19, 12, 25, 64, 63, 5, 3, 11, 18, 38, 28] #리스트

print("리스트 값 중 10보다 큰 수 - 반복문 사용") #출력

for i in numbers : #반복문
    if i >= 10 : #조건문
        print(i, end=', ') #결과 출력

print() #줄 바꿈

print("리스트 값 중 10보다 큰 수 - contnue 사용") #출력

for i in numbers : #반복문
    if i < 10 : #조건문
        continue #계속된다 #반복문을 제어하기 위한 것
    print(i, end=', ') #결과 출력

print()

#1~30 사이의 수 중에서 7의 배수만 출력하시오. ~ continue 사용
#7로 나누어 나머지가 0인 수

print("1~30 사이의 수 중에서 7의 배수 출력 - 반복문")

for i in range(1,31) :
    if i % 7 == 0 :
        print(i, end=', ')
print()


print("1~30 사이의 수 중에서 7의 배수 출력 - continue")

for i in range(1,31) :
    if i % 7 != 0 :
            continue
    print(i, end=', ')




