'''
2023-06-14
컴퓨터공학부 202395004 김나현
#문제 정의
    학생 이름과 점수를 입력 받아 리스트에 저장하고
    학생 점수의 총점과 평균을 출력하시오.
#알고리즘
    0. 빈 학생 리스트 생성
    1. 학생 수 입력 받기
    2. 학생 수 만큼 반복하면서
        2-1. 학생 이름과 점수 저장 - 리스트
        2-2. 점수 합계 계산
    3. 리스트에 저장된 학생 정보 출력
    4. 총점과 평균 출력
'''

student = [] #빈 학생 리스트 생성
sum = 0 #초기화

num = int(input("학생 수 입력 : ")) #학생 수 입력 받기

for i in range(num) : #반복문
    print("<", i+1, "번째 학생 정보 입력") #결과 출력

    name = input("학생 이름 입력 : ") #입력 받기
    score = int(input("%s의 점수 입력 : "%name)) #%s 스트림, 문자열

    student.append([num, score]) #추가하라

    sum = sum + score #sum은  sum + score

for info in student : #반복문
    print("이름 : ",info[0], "점수 : ",info[1]) #결과 출력 리스트 인덱스

print("학생 점수 합계 : ",sum) #결과 출력
print("학생 점수 평균 : {:.2f}",format(sum/num)) #결과 출력