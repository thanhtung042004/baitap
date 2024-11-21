def inputdata ():
    print ("nhap 2 so a,b :\n")
    a= float (input ("a="))
    b= float (input ("b="))
    return a,b
def tong (a,b):
    c=a+b
    return c 
def hieu (a,b):
    c=a-b
    return c 
def tich (a,b):
    c=a*b
    return c 
def thuong (a , b):
    if b==0:
        print ( " division by zero ")
        exit ()
        c=a/b
        return c 
    
def main ():
    a,b= inputdata()
    c= tong (a,b)
    print (a , "+ " , b, "=",c )
    c= hieu ( a,b)    
    print(a , "- " , b, "=",c )
    c=tich (a,b)
    print (a , "* " , b, "=",c )
    c=thuong (a,b)
    print (a , "/" , b, "=",c )
if __name__=="__main__":
    main ()

