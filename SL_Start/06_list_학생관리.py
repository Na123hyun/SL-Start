'''
2023-06-14
컴퓨터공학부 202395004 김나현
#문제 정의
    "학생 관리" 프로그램을 작성
    이 프로그램은 종료 시킬 때까지 무한 반복된다.
    - "작업 선택 : " 에서 0 입력 시 프로그램이 종료된다.
    - "작업 선택 : " 에서 1 입력 시 관리하는 학생의 목록이 조회된다.
    - "작업 선택 : " 에서 2 입력 시 학생을 추가할 수 있다.
    - "작업 선택 : " 에서 3 입력 시 학생을 삭제할 수 있다.
    이때 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며
    목록에 없는 학생을 삭제하고자 할 때는
    '삭제할 학생이 없습니다. 다시 입력하세요!'를 화면에 출력한다.
'''

student = [] #빈 리스트

print("::: 학생 관리 :::")
print("     0. 종료")
print("     1. 학생 조회")
print("     2. 학생 추가")
print("     3. 학생 삭제")
print("====================")

'''
num = input("학생을 입력하시요 : ")

while True : #무한 반복
    if  student == '0' :
        break

    elif student == '1' :
        print("학생 목록이 조회됩니다.")

    elif student == '2' :
        print("학생을 추가할 수 있습니다.")
        student.append(num)

    elif student == '3' :
        print("학생을 삭제할 수 있습니다.")
        student.remove(num)
'''

while True : #무한 반복
    menu = int(input("작업 선택 : ")) #입력 받기
    if menu == 1 : #조건
        print("1. 학생의 조회 : ",student) #출력
    
    elif menu == 2 : #조건
        student.append(input("2. 학생 추가 : ")) #추가하라

    elif menu == 3 : #조건
        del_student = input("3. 삭제할 학생 입력 : ") #입력 받기

        if student.count(del_student) : #세워본다
            print("삭제할 학생이 없습니다.")
            continue #돌아가다
        
        else : 
            student.remove(del_student) #삭제하다
    elif menu == 0 : #조건
        print("프로그램을 종료합니다.") #출력
        break #무한 반복 종료