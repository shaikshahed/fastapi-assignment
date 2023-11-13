d={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
t={'grey':0.05,'violet':0.10,'blue':0.25,'green':0.5,'brown':1,'red':2,'gold':5,'silver':10}
band=int(input())
if band==1:
    print(d['black'])
elif band==3:
    s1,s2,s3=input(),input(),input()
    print(d[s1],d[s2],d[s3]*'0')
elif band==4:
    s1,s2,s3,s4=input(),input(),input(),input()
    if s3=='black':
        print(d[s1],d[s2],'ohms',t[s4],'% tolerance')
    elif s3=='orange':
        print(d[s1],d[s2],'kiloohms',t[s4])
    elif s3=='blue':
        print(d[s1],d[s2],'megaohms',t[s4])
    else:
        print(d[s1],d[s2],d[s3]*'0',t[s4],'% tolerance')
elif band==5:
    s1,s2,s3,s4,s5=input(),input(),input(),input(),input()
    if s4=='black':
        print(d[s1],d[s2],d[s3],t[s5])
    elif s4=='blue':
        print(d[s1],d[s2],d[s3],'M',t[s5])

