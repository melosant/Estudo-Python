# Programa 6 - Tabuada 

num = int(input("Digite um número : "))
i = 0

print("\nusando while:\n")
# loop para tabuada usando while
while i < 11:
    print(f"{num} x {i} = ", num * i)
    i += 1

print("\nusando for:\n")
# loop para tabuada usando for
for i in range(11):
    print(f"{num} x {i} = ", num * i)