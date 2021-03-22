n = int(input())
num = 0
while n!=0:
    rem = n%10
    num = num*10 + rem
    n = n//10
print(num)
