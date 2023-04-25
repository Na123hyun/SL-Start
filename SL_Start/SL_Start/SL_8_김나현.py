'''
2023-04-21
김나현
태어난 년도를 입력 받아 띠를 출력하는 프로그램을 작성하시오.
띠 순서는 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양띠이다.
'''

year = int(input("태어난 년도를 입력하시오. : "))
birth_year = year%12

if birth_year == 0 :
    print("원숭이 띠입니다.")
elif birth_year == 1 :
    print("닭 띠입니다.")
elif birth_year == 2 :
    print("개 띠 입니다.")
elif birth_year == 3 :
    print("돼지 띠입니다.")
elif birth_year == 4 :
    print("쥐 띠 입니다.")
elif birth_year == 5 :
    print("소 띠입니다.")
elif birth_year == 6 :
    print("범 띠 입니다.")
elif birth_year == 7 :
    print("토끼 띠입니다.")
elif birth_year == 8 :
    print("용 띠 입니다.")
elif birth_year == 9 :
    print("뱀 띠입니다.")
elif birth_year == 10 :
    print("말 띠 입니다.")
else :
    print("양 띠입니다.")