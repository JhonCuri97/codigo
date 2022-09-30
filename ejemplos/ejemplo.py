
a_lis=['aaa','bb','ll','aba','vcd']


m = max(a_lis,key=len)
a=[]   
for i in a_lis:
        if len(a_lis)==m:
            i+=i         
            a+=a
        else:
            break

print(a)