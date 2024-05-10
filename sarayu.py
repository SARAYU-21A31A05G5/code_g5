#1
def mean():
    a=list(map(int,input().split()))
    n=len(a)
    avg=sum(a)/n
    print("Mean=",avg)
#2
def median():
    a=list(map(int,input().split()))
    s=sorted(a)
    n=len(a)
    m=0
    if(len(a)%2==0):
        m=(s[int(n/2)]+s[int(n/2 +1)])/2
    else:
        m=s[int(n/2)]  
    print("Median=",m)
#3
def palindrome():
    a=input()
    if(a[:]==a[::-1]):
        print("palindrome")
    else:
        print("not palindrome")          
#4
def mean_of_odd():
    a=list(map(int,input().split()))
    s=[]
    m=0
    for i in a:
        if(i%2==1):
            s.append(i)
            m=m+i
    k=m/len(s)
    print("Mean of odd numbers is:",k)
#5
def mean_of_even():
    a=list(map(int,input().split()))
    s=[]
    m=0
    for i in a:
        if(i%2==0):
            s.append(i)
            m=m+i
    k=m/len(s)
    print("Mean of even numbers is:",k)
#6
def Kth_min():
    a=list(map(int,input().split()))
    s=sorted(a)
    k=int(input())
    if(k>=len(a)):
        print("Invalid input")
    else:
        print("Kth min is:",s[k])
#7
def Kth_max():
    a=list(map(int,input().split()))
    m=sorted(a)
    s=m[::-1]
    k=int(input())
    if(k>=len(a)):
        print("Invalid input")
    else:
        print("Kth max is:",s[k])
#8
def combination():
    a=list(map(int,input().split()))
    s=[]
    for i in range(len(a)):
        n=a[i]
        c=1
        while(n>0):
            c=c*n
            n=n-1    
        s.append(c) 
    k=a[0]-a[1]
    v=1
    while(k>0):
        v=v*k
        k=k-1
    s.append(k)
    com=s[0]/(s[1] * s[2])
    print(com)    
#9
def permutation():
    a=list(map(int,input().split()))
    s=[]
    n=a[0]
    c=1
    while(n>0):
        c=c*n
        n=n-1    
    s.append(c) 
    k=a[0]-a[1]
    v=1
    while(k>0):
        v=v*k
        k=k-1
    s.append(k)
    per=s[0]/s[1]
    print(per)  
#10
def sum_of_squares():
    a=list(map(int,input().split()))
    s=0
    for i in a:
        s=s+(i*i)
    print("Sum of sqaures=",s)
        

        


                


       



