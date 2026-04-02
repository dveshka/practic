n = -1
if type(n) != int:
    print(-1)
if n == 0 or n == 1:
   print(1)
if n < 0:
   print(-1)
a = 0
b = 1
while(a < n):
    a = a + 1
    b = b * a
print(b)
