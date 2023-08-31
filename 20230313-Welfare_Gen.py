import random
print('This is a two-color ball Lottery Generator.')
while True:
    go_on=False
    num=int(input('Please enter the number of Lottery tickets: '))
    if num>=1:
        break
    else:
        go_on=False
for num in range (1,num+1):
    print(f'{random.sample(range(1,33),6)} {random.sample(range(1,16),1)}')
    #Note: if using statement'randint(1,33,size=6)' it may generate 6 duplicated random numbers.



