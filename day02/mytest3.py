# 국어점수를 입력하시오 90
# 영어점수를 입력하시오 80
# 수학점수를 입력하시오 70
# 당신의 총점은 240점이고 평균은 80점입니다

kor = input("국어점수를 입력하세요")
eng = input("영어점수를 입력하세요")
math = input("수학점수를 입력하세요")

sum = int(kor) + int(eng) + int(math)
avg = (int(kor) + int(eng) + int(math))/3

print("당신의 총점은 "+str(sum)+"이고 평균은 "+str(avg)+"입니다")