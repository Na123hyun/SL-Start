'''
2023-06-14
김나현
#문제 정의
    숫자 추측 게임 만들기
#문제 분석
    사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값(1~30)을 비교한다.
    몇 번만에 맞혔는 지 알려준다.
    
    사용자에게 힌트를 준다.
    사용자가 입력한 값이 랜덤 값보다 크면 숫자는 작다. 라고 한다.
    사용자가 입력한 값이 랜덤 값보다 작으면 숫자는 크다. 라고 한다.

    사용자가 값을 입력하여 힌트를 받을 때마다 count를 증가한다.

    게임은 한번만 한다.
    게임은 0을 입력하면 종료한다. <
    게임은 사용자가 y를 입력하면 시작한다.
#알고리즘
    1. import 랜덤 모듈 선언
    2. 게임을 할 것인지 묻는다.
        게임을 하지 않으면
            프로그램 종료
        2-1 컴퓨터 랜덤 수 생성
    3. 사용자로부터 정수 입력 받기
    4. 입력 받은 수와 컴퓨터 수가 같으면
        몇 번만에 맞혔다. 
        프로그램 종료 
    5. 컴퓨터 수가 크다면
        힌트
    6. 사용자 수가 크다면
        힌트

'''

import random #impot 랜덤 모듈 선언

game = 'y' #답 

print("게임을 시작하시겠습니까?") #묻기
while game == 'y' : #답 받기
    i = random.randint(1,30) #컴퓨터 랜덤 수 생성
    print("게임을 시작합니다.") #스타트

    count = 1 #초기화
    while True : #무한 반복
        num = int(input("추측한 숫자를 입력하십시오. : ")) #정수 입력 받기

        if num == i : #조건문 
            print("{}번 만에 맞혔습니다. 대단하시군요.",format(count)) #오? 대단한 걸??
            break #무한 반복 종료
        elif i > num : #음 ~ 틀렸어 다시 생각해봐^^
            print("제가 가지고 있는 숫자가 더 큽니다.")
        elif i < num : #음 ~ 틀렸어 다시 시작해봐^^
            print("제가 가지고 있는 숫자가 더 작습니다")

        count += 1 #count = count + 1 #conut는 1씩 증가

        game = input("게임을 다시 시작하시겠습니까? (y or n ) : ") #또 할겨? 묻기


    
