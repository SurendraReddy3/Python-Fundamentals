def Factroial(num1,num2):
    factorial={}
    for val in range(num1,num2+1):
        fact=1 
        for i in range(1,val+1):
            fact=fact*i
        #print(f"Factorial of {val} is {fact}")
        factorial[val]=fact 
    
    print(factorial)
def main():
    num1=int(input("Enter the start number"))
    num2=int(input("Enter the end number"))
    Factroial(num1,num2)

if __name__=="__main__":
    main()



    
    
    