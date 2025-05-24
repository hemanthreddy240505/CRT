'''a=~(-7)
print(a)'''
#LEAP YEAR
'''
n=int(input('Enter the year:'))
if(n%4==0):
    if(n%4==0 and n%100==0 and n%400==0):
        print('leap year')
    else:
        print('Not a leap year')
'''
#DATATYPES
'''
name="charan"
print(type(name))
print(dir(name))
'''
#OPERATORS IN THE LIST
'''
a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*2+b)
print(a<b)'''
#THE CAT CODE PROGRAM
'''def catfood(n,c,u,arr):
    if n==0:
        return 0
    cf=0
    rf=c*u
    for i in range(n):
        cf=cf+arr[i]
        if c>=rf:
            return i+1
    if cf<rf:
        return -1
n=int(input())
c=int(input())
u=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(catfood(n,c,u,arr))'''
#THE MISSING DIGITS
'''def missingDigits(num):
    number=str(num)
    missing_digits=[]
    for i in range(10):
        if str(i) not in number:
            missing_digits.append(i)
    return missing_digits
num=int(input())
print(missingDigits(num))'''
#MISSING DIGITS OR
'''def missingDigits(num):
    li=[False]*10
    while num:
        li[num%10]=True
        num=num//10
    return li
num=int(input())
result=missingDigits(num)
for i in range(10):
    if not result[i]:
        print(i,end=" ")'''
#SQUARING THE ELEMENTS IN THE LIST
'''a=[1,2,3,4,5]
sq=[]
for i in a:
    sq.append(i*i)
print(sq)
'''
#OR
'''print([a*a for a in range(1,6)])'''
'''print([x*x for x in range(1,16) if x%2==1 if x%3==0])'''
'''n=int(input())
print(['fizzzz' if i%n==0 else 'buzz' for i in range(1,6)])'''
#COPY METHOD
a=[1,2,3]
b=a.copy()
b.append(21)
print(b)
print(a)