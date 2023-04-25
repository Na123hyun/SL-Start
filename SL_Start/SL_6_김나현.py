'''
2023-04-21
김나현
년도를 입력 받아 윤년인 지 아닌 지 여부를 판단하라.
'''
year = int(input("연도를 입력하시오. : "))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
    print("{}년은 윤년입니다.".format(year))
else :
    print("{}년은 윤년이 아닙니다.".format(year))