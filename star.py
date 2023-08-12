"""i=1
while i<=5 :
    print("*\n")
    i=i+1"""
print("enter number of line:")
num=int(input())
nstar=1;
nspace=num-1;
while num>0:
    print(" "*nspace+"*"*nstar+"\t"*nspace+"\n")
    nspace-=1
    nstar+=2
    num-=1