'''
2023-06-16
컴퓨터공학부 202395004 김나현
#문제 정의
    키와 몸무게로 비만도 계산하기
'''

with open("info.txt","r") as file :
    for line in file :              #strip() 공백 제거, split(",") 구분자
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height) :
            continue #이름이 없고 몸무게가 없고 키가 없으면 컨티뉴하라

    bmi = int(weight) / ((int(height) / 100) ** 2) #비만도 계산하기

    if bmi >= 25 :
        result = "과체중"
    elif bmi >= 18.5 :
        result = "정상채중"
    else :
        result = "저체중"

    print("\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {:.2f}", "결과 : {}"]).format(name,weight,height,bmi,result))
                                                                #:.2f 소수점 넣기
print()