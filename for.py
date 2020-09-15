patterns = {'가위', '보', '보', '가위', '가위', '가위', '보', '가위', '바위', '보'}
for pattern in patterns:
    print(pattern)


for a in range(5):  # = [0, 1, 2, 3, 4]
    print(a)

names = ['철수', '영희', '바둑이', '귀도', '나리']
for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))

print('\n')

for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))#위와 같은 결과


for i in range(11172):
    print(chr(44032 + i), end='')