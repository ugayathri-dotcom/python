a=int(input("Enter Mulitiplication table limit"))
for i in range (1,a+1):
    for j in range (1,11):
        s=i*j
        print(f"{j}*{i}={s}")
    
    print()
