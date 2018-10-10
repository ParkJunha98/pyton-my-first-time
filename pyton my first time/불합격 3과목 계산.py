kor=float(input('국어성적 입력;'))
eng=float(input('영어성적 입력;'))
math=float(input('수학성적 입력;'))

avg=(kor+eng+math)/3
if avg>=60 and kor >=50 and eng>=50 and math>=50:
    print('성적 평균은 ',avg,'이며, 과락과목도 없기 때문에 합격입니다.')
else:
    if avg>=60:
        print('성적 평균은',avg,'이며 불합격입니다.')
    else:
        print('성적 평균은',avg,'이며 불합격입니다.')
        
