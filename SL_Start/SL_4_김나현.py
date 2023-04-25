'''
2023-04-21
김나현
컴퓨터, 영어 과목의 점수를 입력 받아 두 과목 중 한 과목의 성적이 95점 이상이거나, 두 과목의 합이 170점 이상이면 "합격입니다."를 출력하고, 아니면 "불합격입니다."를 출력하는 프로그램 작성.
'''

computer = int(input("컴퓨터 과목 입력 : "))
english = int(input("영어 과목 입력 : "))
total = computer + english

if computer >= 95 or english >= 95 :
    print("합격입니다.")
elif total >= 170 :
    print("합격입니다.")
else :
    print("불합격입니다.")