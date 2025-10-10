
sum=0
print("Integers between 100 and 200 that are divisible by 9")
for i in range (100,200):
    if i%9==0:
        print(i)
        sum+=i

print("Sumof all integer between 100 and 200 that are divisible by 9",sum)
