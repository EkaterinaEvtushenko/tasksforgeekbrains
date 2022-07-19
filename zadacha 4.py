num = int(input())
total = 0
while num!= 0:
   a = num//10
   b = num%10
   num = a
   total += b
print(total)