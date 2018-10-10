mon=int(input('월을 입력하세요:'))
if mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12:
    print('31일까지')

elif mon==2:
    print('28일 또는 29일까지')

elif mon==4 or mon==6 or mon==9 or mon==11:
    print('30일 까지')

else:
    print('입력오류')
    
