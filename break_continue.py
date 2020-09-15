list = [1,2,3,4,5,6,7,8,9,10]

"""
for i in range(10):
    if i % 2 != 0:
        print(i)
        print(i)
        print(i)
        print(i)
"""

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i) #위와 같은 결과