n = input()
ln = len(n)
t = n
s = 0
while n!=0:
    a = int(n)%10
    s = s + a**ln
    n = int(n)//10
if int(t) == s:
    print("Armstrong")
else:
    print("Not Armstrong")
    
