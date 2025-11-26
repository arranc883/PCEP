def count(n):
   if n:
      return n+count(n-1)
   
   else:
      return 0

answer = count(5)

print(answer)