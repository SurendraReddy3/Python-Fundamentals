def combination(n):
    if n==0 or n== 1:
        return 1
    else:
        combinations=[[i,j,k] for i in range(n+1) for j in range(n+1) for k in range(n+1) if i+j+k <n]
    return combinations
def main():
    n=int(input("Enter n value:"))
    print(combination(n))

if __name__=="__main__":
    main()