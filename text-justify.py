import textwrap

length=int(input())
text=textwrap.wrap(text=input(),width=length)
i=0
result=[]
while i<len(text):
    list_words=text[i].split()
    spaces=length-len(text[i])
    if spaces>0 and i!=len(text)-1:
        for j in range(1,len(list_words)):
            list_words[j]=" "+list_words[j]
        k=1
        while spaces>0 and k<len(list_words):
            list_words[k]=" "+list_words[k]
            spaces-=1
            k+=1
            if k>=len(list_words):
                k=1
        result.append("".join(list_words))
    else:
        result.append(text[i])
    i+=1
for line in result:
    print(line)
