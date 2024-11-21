G=[] ; P=[]
const = 10
def CreateQ(open):
    for i in range (const):
        open.append([])
        for i in range (2):
            open[i].append(0)

def emptyQ(open):
    return len(open) - open.count(open[0])==0
def addQ(open,n,value,index):
    n=n+1
    open[n][0]=value
    open[n][1]=index
    i=n
    while i>1:
        j=int(i/2)
        if open[i][0] < open[j][0]:
            temp=open[i]
            open[i]=open[j]
            open[j]=temp
        i=j
    return n 
def removeQ(open):
    value=open[1][0]
    index=open[1][1]
    n=len(open) - open.count(open[0])
    open[1][0]=open[n][0]
    open[1][1]=open[n][1]
    open[n][0]=0 ; open[n][1]=0
    n=n-1 ; i=1
    while i<= int (n/2):
        j=1*2;
        if j < n:
            if open[j][0]>open[j+1][0]:
                j=j+1
                if open [1][0]>open[j][0]:
                    open[i],open[j]=open[j],open[1]
        else :
            if open [i][0] > open[j][0]:
                     open [i],open[j]=open[j],open[i]
        i=i+1
    return value , index , n 

def split(string):
    k=string.index(' ')
    a=int (string[0:k])
    m=string.index(' ',k+1,-1)
    b=int(string[k+1:m])
    c=int(string[m+1:len(string)])
    return a,b,c

def init(path,G):
    f=open(path)
    string=f.readline()
    n,a,z =split(string.replace('\t',' '))

    for i in range(n+1):
        G.append([])
        for i in range(n+1):
            G[i].append(0)
    while True:
        string=f.readline()
        if not string :
            break
        i,j,x = split(string.replace('\t',' '))
        G[i][j]=G[j][i]=int (x)
    f.close()
    return n,a,z

def algorithm_for_tree(G,P,n,s,g):
    resul = 0 ; close=[]; o=[]
    for i in range(const):
        close.append(0)
        o.append(0)
        P.append(0)
    open=[]
    CreateQ(open)
    m=addQ(open,0,resul,s)
    o[n]=i ; P[s]=s
    while not emptyQ(open):
        value ,u ,m=removeQ(open)
        if u ==g:
            resul=value
        for v in range(1,n+1):
            if G[u][v] !=0 and 0[v]==0 and close[v]==0:
                x=value + G[u][v]
                m=addQ[open,m,x,v]
                o[v]= i; P[v]=u
        close[u]=1 
        o[u]=0
    return resul

def print(P,n,s,g):
    path=[]
    for i in range(0,n+1):
        path.append(0)
    print(" duong di tu %d" % s,"den %d" % g,"la\npath:",end =' ');
    path[0]=g

    i=P[g]
    k=1
    while i !=s:
        path[k]=i
        k=k+1
        i=P[i]
    path[k]=s
    for j in range (0,k+1):
        i=k-j
        if i >0:
            print ("%d =>"% path[i],end =' ')
        else:
            print("%d" %path[i],end=' ')

def  main():
    n,s,g=init("graph6.inp", G)
    resul =algorithm_for_tree(G,P,n,s,g)
    print(P,n,s,g)
    print("\nresul: %d" %resul , end='\n')
if __name__=="__main__":
    main()

    




