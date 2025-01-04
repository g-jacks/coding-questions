
val2 = input().lower().split(" ")

def wordSum(val):
    sets = (len(val)//2)
    size=len(val)
    j = 0
    k = -1
    sum = 0
    for i in range(sets):
        sum = sum+((ord(val[j])-96)-(ord(val[k])-96))
        j+=1
        k-=1
    if(size%2):
        sum+=ord(val[(size//2)])-96
    return sum
t_sum=""
for i in val2:
    t_sum+=(str(wordSum(i)))
print(t_sum)



