
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

faktorials = 1

for i in range(1, ievaditais_skaitlis + 1):
    faktorials *= i

print(f"Faktoriāls no {ievaditais_skaitlis} ir: {faktorials}")
