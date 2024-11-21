def inputdata():
    n= int (print("n="))
    return n 
def giaithua (n) :
    s=1 
    for i in range(1, n+1):
        s=s*1 
        return s 
def main () :
    n= int (input("n= "))
    s=giaithua (n)
    print ("%d "%n , "!=%d "%s )
if __name__ =="__main__":
    main()

