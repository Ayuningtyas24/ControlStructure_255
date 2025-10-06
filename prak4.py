n = int(input("Enter the maximum value: "))

print("Odd numbers up to", n, ": ")
for i in range(1, n+1, 2): 
     print(i, end=" ")