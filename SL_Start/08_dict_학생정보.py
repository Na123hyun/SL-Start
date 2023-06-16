'''
2023-06-16
컴퓨터공학부 20239504 김나현
#문제 정의
    학생 정보를 사전에 저장하고 (학번, 이름)
    특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.

#알고리즘
    1. 학생 정보 저장 사전 만들기 - 빈 사전 만들기
    2. 학생 정보 입력 (z 키를 누르면 종료 - 무한 반복)
    3. 학번으로 검색하여 학생 찾기 (학번 빈칸이면 검색 종료 - 무한 반복)
'''

'''
print(":: 학생 정보 입력 ::")
while True : 
    #stuName = input("추가할 학생의 이름을 입력하시오 (종료는 z를 입력) : ")
    #if stuName == 'z' :
        #break
    #stuId = input("학번을 입력하세요 : ")
    infor = {}
    infor['학번'] = input('학번을 입력하시요 : ')
    if infor['학번'] == 'Z':
        break
    infor['학과'] = input('학과를 입력하시오 : ')
    if infor['학과'] == 'Z':
        break
    infor['이름'] = input('이름을 입력하시오 : ')
    if infor['이름'] == 'Z':
        break

    student[infor['학번']] = infor

while True:
'''

student = {}

print("::학생 정보 입력::")
while True : #무한 반복
    student_id = input("추가 하실 학생의 학번을 입력하시오 : ") #입력 받기
    if student_id == 'z': #키
        print("입력 종료") 
        break #무한 반복 종료
    student_name = input("추가 하실 학생의 이름을 입력하시오 : ") #입력 받기
    if student_name == 'z': #키
        print(student)
        print("입력 종료") 
        break #무한 반복 종료
    student[student_id] = student_name

print("학생 검색")
while True : #무한 반복
    student_id = input("찾으실 학생의 학번을 입력하시오 : ") #입력 받기
    if student_id == '':  
        print("프로그램 종료")
        break #무한 반복 종료
    elif student_id in student:
        print('찾으시는 학생의 정보는 : {}'.format(student[student_id]))
    else :
        print("찾으시는 학생이 없습니다.")
