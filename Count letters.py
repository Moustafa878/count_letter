def count_letters(str):
    maxword =""
    maxnum=0

    max=[]
    words=str.split()
    for i in words:
        maxletter = 0
        for j in i:
            counter = 0
            for k in i:
              if j==k:
                  counter+=1
              if maxletter<counter:
                  maxletter=counter
        max.append(i)
        max.append(maxletter)
    for i in range(1,len(max),2):
            if maxnum<max[i]:
                maxnum=max[i]
                maxword=max[i-1]
    if maxnum==1:
        return -1
    else:
        return maxword
print(count_letters("Today, is the greatest day ever!"))