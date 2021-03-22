n = int(input())
t = n
s = 0
while n!=0:
    a = n%10
    s = s + a**3
    n = n//10
if t == s:
    print("Armstrong")
else:
    print("Not Armstrong")
    
