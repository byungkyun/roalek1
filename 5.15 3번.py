def roal(roalek):
    if score >= 90 and score <= 100:
        print(roalek,":","A")
    elif score >= 80 and score <= 89:
        print(roalek,":","B")
    elif score >= 70 and score <= 79:
        print(roalek,":","C")
    elif score >= 60 and score <= 69:
        print(roalek,":","D")
    else:
        print(roalek,":","F")
        
score = int(input("점수:"))
if score >=0 and score <= 100:
    roal(score)
else:
    print("입력 가능한 점수 범위는 0~100입니다.")
