# cook your dish here
N=int(input())
if ((N%5==0)&(N%11!=0))|((N%5!=0)&(N%11==0)):
    print("ONE")
elif ((N%5==0)&(N%11==0)):
    print("BOTH")
else :
    print("None")