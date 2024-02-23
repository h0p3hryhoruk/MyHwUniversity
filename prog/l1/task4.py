klas1 = int(input("Кількість учнів у першому класі: "))
klas2 = int(input("Кількість учнів у другому класі: "))
klas3 = int(input("Кількість учнів у третьому класі: "))

total_students = klas1 + klas2 + klas3 
total_desks = (total_students + 1)  // 2

print("Потрібно закупити {} парт(и)", total_desks)

