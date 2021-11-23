#Q NO. 2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20 ;a+=30;a%=3
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3)and(7<4)or(18==3))and (9>3))
print(True is False)
print(((True==False)or(False>True))and(False<=True))


#Q NO. 3
s1='nice to have it'
s2='here'
print(s1+" "+s2)

#Q NO. 4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Q NO.5
(a.insert(0,s1))
a.insert(7,s2)
print(a)

#Q NO.6
l=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
t=len(l)
for i in range(len(l)):
      if (l[i]%2==0 and l[i]<237):
          print('[',l[i],']',end='')
         

#Q NO.7
color_list_1=set(['white','black','red'])
color_list_2=set(['red','green'])
print(color_list_1-color_list_2)

#Q NO.8
s=input('enter the string ')
s=s.lower()
alphabets='abcdefghijklmnopqrstuvwxyz'
flag=0
for i in alphabets:
     if i not in s:
         flag=1
         break
if flag==1:
     print('false')
else:
     print('true')


#Q NO. 9
n=(input('enter a no. '))
print(int(n+n)+int(n)+int(n+n+n)) 


#Q NO. 10
string=input('enter string ')
l=string.split('#')
l1=l[0].split(' ')
for i in range(len(l1)):
     l1[i]=int(l1[i])
l2=l[1].split(' ')
for i in range(len(l2)):
     l2[i]=int(l2[i])
print(l1)
print(l2)




#Q NO. 11
s=input().split(',')
print(s)
s.sort()
print(s)

#Q NO.12

d={'student':['rahul','kishore','vidhya','rakhi'],'marks':[57,87,67,79]}
large=max(d['marks'])
for i in range(len(d['marks'])):
    if(d['marks'][i]==large):
        j=i
print(d['student'][j])        


#Q NO. 13
s=input()
c=0
d=0
for i in s:
    if i.isalpha():
        c=c+1
    if i.isdigit():
        d=d+1
print('letters=',c)
print('digits=',d)

#Q NO. 14
d={'name':['akash','soniya','vishakha','akshay','rahul','vikas'],'subject':['python','java','python','c','python','java'],'ratings':[8.4,7.8,8,9,8.2,5.6]}
s=input('enter subject ')
l1=d['name']
l2=d['subject']
l3=d['ratings']
l4=[]
l5=[]
l6=[]
for i in range(len(l2)):
    if l2[i]==s:
        l4+=[l1[i]]
        l5+=[l2[i]]
        l6+=[l3[i]]
a={}
a['name']=l4
a['subject']=l5
a['ratings']=l6
print(a)