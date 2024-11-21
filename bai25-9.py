import os
G=[] ; P=[]; n=0
def Split (string):
    k=string.index(' ')
    str=string[0:k]
    a=int(str)
    n=string.index(' ',k+1,-1)
    str=string[k+1:m]
    b= int (str)
    str=string[m+1:len(string)]
    c=int(str)
    return a,b,c 
#-------------------------------------------------------------------------------------------------------#
def Init (path,G):
    f=open(path)
    string=f.readline()
    n,a,z=Split(string.replace(' \t',' ') )
    for i in  range (n+1):
        G.append([])
        for j in range (n+1):
            G[i].append(0)
    while True :
        string =f.readline()
        if not string:
            break
        i,j,x = Split(string.replace('\t',' '))
        G[i][j]=G[j][i]=x
    f.close()
    return n,a,z
def Check(M,n,u):
    for i in range (1,n+1):
        if M[i]==u:
            return True
        return False
def ViewMatrix(G,n):
    for i in range (1,n+1):
        for j in range (1,n+1):
            print("%d" % G[i][j],end =' ' )
        print()
def Detph_First_Search(G,n,s,g,P):
    open=[]; Close =[]
    for j in range (n+3):
        Open.append(0)
        Close.append(0)
        P.append(0)
    top=1;open[top]=s
    P[s]=s;
    while(top>0):
        u=open[top] ; top=top-1
        if u ==g:
            return 1
        for v in range (n,0,-1):
            if G[u][v] !=0 and not Check(Open,n,v) and not Check(Close,n,v):
                top=top+1;open[top]=v
                P[v]=u;
        Close[u]=u
    return 0
def Print(P,n,s,g):
    path=[]
    for i in range(0,n+1):
        path.append(0)
    print("\nDuong di tu %d" % s , "den %d" % g,"la\n",end =' ');
    path[0]=g
    i=P[g];k=1
    while i != s:
        path[k]=i;k=k+1
        i=P[i]
    path[k]=s
    for j in range (0, k+1):
        i=k-j
        if i>0:
            Print("%d=>"%Path[i],end=' ')
        else:
            Print("%d" % path[i],end =' ')
def main ():
    n,s,g=Init("graph.inp" ,G)
    print ("xem ma tran G:%d" %g,end ='\n'); ViewMatrix(G,n)
    Detph_First_Search (G,n,s,g,P); Print(P,n,s,g)
if __name__=="__main__":
    main()  

