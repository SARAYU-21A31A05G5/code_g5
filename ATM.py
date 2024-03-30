def ATM(index):
    print("enter password:")
    c=3
    while(c!=0):
        pw=input()
        if(pw==password[index]):
            print("enter your choice:")
            print("press 1 for Withdrawl")
            print("press 2 for deposit")
            print("press 3 to check balance")
            print("press 4 to change password")
            choice=[1,2,3,4]
            while(1):
                ch=int(input())
                if(ch in choice):
                    if(ch==1):
                        print("enter pin:")
                        p=int(input())
                        if(p==pin[index]):
                           print("enter withdrawl amount:")
                           wa=int(input())
                           if(wa<=balance[index]):
                               print("Amount collected")
                               print("Balance:",balance[index]-wa)
                               print("End")
                               exit()                      
                           else:
                               print("Insufficient Balance")
                               print("End")
                               exit()    
                        else:
                           print("Invalid Pin")
                           print("End")
                           exit()
                    elif(ch==2):
                        print("Enter pin:")
                        p1=int(input())
                        if(p1==pin[index]):
                            print("Enter amount to be deposited:")
                            deposit=int(input())
                            print("Amount deposited")
                            print("Balance:",deposit+balance[index])
                            print("End")
                            exit()
                        else:
                            print("Invalid Pin")
                            print("End")
                            exit()
                    elif(ch==3):
                        print("Enter pin:")
                        p2=int(input())
                        if(p2==pin[index]):
                            print("Your balance is:",balance[index])
                            print("End")
                            exit()
                        else:
                            print("Invalid Pin")
                            print("End")
                            exit()
                    elif(ch==4):
                        print("Enter pin:")
                        p3=int(input())
                        if(p3==pin[index]):
                            print("Enter current password:")
                            s=3
                            while(s!=0):
                                cp=input()
                                if(cp==password[index]):
                                    print("Enter new password:")
                                    np=input()
                                    if(cp==np):
                                        print("new password should not match with current password")
                                        print("Re-enter current password")
                                    else:
                                        print("Re-enter new password:")
                                        rp=input()
                                        if(rp==np):
                                            print("password changed successfully")
                                            password[index]=np
                                            print("End")
                                            exit()
                                        else:
                                            print("Password not matched")
                                            print("Re-enter current password:")

                                else:
                                    s=s-1
                                    if(s==0):
                                        print("Wrong Password")
                                        print("No more attempts left","Account Blocked")
                                        print("End")
                                        exit()
                                    print("Wrong password",s,"More attempts left") 
                        else:
                           print("Invalid Pin")
                           print("End")
                           exit()            
                else:
                    print("Wrong Input","Re-enter your choice")                                  
        else:
            c=c-1
            if(c==0):
                print("Wrong Password")
                print("No more attempts left","Account Blocked")
                print("End")
                exit()
            print("wrong password","you have",c,"attempts left")
            print("Re-enter password")

username=['sara','anju','ishu','vasu']
password=['sara01','anju08','ishu10','vasu05']
pin=[1111,2222,3333,4444]
balance=[25000,30000,25000,18000]
print("enter username:")
user=input()
if(user not in username):
    print("Invalid user")
    print("End")
    exit()
else:
    for i in range(len(username)):
        if(username[i]==user):
            ATM(i)