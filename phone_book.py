n=int(input())
i=0
p_book={}
while i<n:
    p=input()
    name,value=p.split()
    value=int (value)
    p_book[name]=value
    i+=1
i=0
while(i<n):
    k=input()
    if(k in p_book):
        print(k+'='+str(p_book[k]))
    else:
        print('Not Found')
    i+=1
