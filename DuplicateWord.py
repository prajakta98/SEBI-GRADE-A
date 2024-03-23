#WAP to remove duplicate word from a sentence(10M)

s = input("Enter a sentence")
l = s.split()
k = []
for i in l:
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))

#I/P- my name is abc is
#O/P- my name is abc (when i>=1 is written)
#O/P- is(when i>1 is written)
#O/P- my name abc (when i=1 is written)