#if 조건문

people = 3
apple = 13

if people < apple / 5:
    print('신나는 사과 파티! 배 터지게 먹자!')
else:
    print('사과가 많지 않네')

if apple % people > 0:
    print('몇 개는 쪼개 먹자')

if people > apple:
    print('사람이 너무 많아!')

if True:
    print('아 머리 아프다...')
    print('블로그에 글 올리면서 지원서 써도 늦지 않을 거야..아마도..')
    print('영상은 오늘 밤에 힘들면 그냥 저번에 만든 포폴로 대체하든가 해야지')


scissor = '가위'
rock = '바위'
paper = '보'

win = '승리'
draw = '무승부'
lose = '패배'

mine = '가위'
yours = '바위'

if mine == yours:
    result = draw
else:
    if mine == scissor:
        if yours == paper:
            result = win
        else:
            result = lose
    elif mine == rock:
        if yours == scissor:
            result = win
        else:
            result = lose
    elif mine == paper:
        if yours == rock:
            result = win
        else:
            result = lose
    else:
        print('오류')
    

print(result)